import asyncio
import logging
import socket
from typing import List, Dict, Any, Optional
from datetime import datetime
import nmap
from config import settings

logger = logging.getLogger(__name__)


class NetworkScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
    
    async def nmap_scan(self, subnet: str) -> List[Dict[str, Any]]:
        """
        Perform nmap scan on the given subnet
        """
        logger.info(f"Starting nmap scan of {subnet}")
        discovered_assets = []
        
        try:
            # Run nmap scan in a thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            scan_result = await loop.run_in_executor(
                None, 
                self._run_nmap_scan, 
                subnet
            )
            
            # Process scan results
            for host in scan_result:
                asset_data = await self._process_host_data(host, scan_result[host])
                if asset_data:
                    discovered_assets.append(asset_data)
            
            logger.info(f"Nmap scan completed. Found {len(discovered_assets)} responsive hosts")
            
        except Exception as e:
            logger.error(f"Error during nmap scan: {str(e)}")
        
        return discovered_assets
    
    def _run_nmap_scan(self, subnet: str) -> Dict:
        """
        Run the actual nmap scan (blocking operation)
        """
        try:
            # Scan for common ports and OS detection
            self.nm.scan(
                hosts=subnet,
                ports='22,23,80,443,135,139,445,3389,5985,5986',
                arguments='-sS -O -sV --max-rtt-timeout 2s --max-retries 1'
            )
            return self.nm.all_hosts()
        except Exception as e:
            logger.error(f"Nmap scan failed: {str(e)}")
            return {}
    
    async def _process_host_data(self, host: str, host_data: Dict) -> Optional[Dict[str, Any]]:
        """
        Process individual host data from nmap scan
        """
        try:
            # Skip hosts that are not up
            if host_data.get('status', {}).get('state') != 'up':
                return None
            
            # Get hostname
            hostname = host_data.get('hostnames', [{}])[0].get('name', '')
            if not hostname:
                hostname = f"host-{host.replace('.', '-')}"
            
            # Determine device category based on open ports and OS
            category = self._determine_category(host_data)
            
            # Get OS information
            os_info = self._extract_os_info(host_data)
            
            # Get MAC address if available
            mac_address = self._extract_mac_address(host_data)
            
            # Create asset data structure
            asset_data = {
                'name': hostname,
                'asset_tag': f"DISC-{host.replace('.', '-')}-{int(datetime.now().timestamp())}",
                'category': category,
                'brand': 'Unknown',
                'model': 'Unknown',
                'serial_number': None,
                'ip_address': host,
                'mac_address': mac_address,
                'operating_system': os_info,
                'status': 'Active',
                'location': 'Discovered via Network Scan',
                'description': f'Automatically discovered device at {host}. Open ports: {self._get_open_ports(host_data)}'
            }
            
            return asset_data
            
        except Exception as e:
            logger.error(f"Error processing host {host}: {str(e)}")
            return None
    
    def _determine_category(self, host_data: Dict) -> str:
        """
        Determine device category based on scan results
        """
        tcp_ports = host_data.get('tcp', {})
        os_matches = host_data.get('osmatch', [])
        
        # Check for common service ports
        if 22 in tcp_ports or 23 in tcp_ports:  # SSH or Telnet
            # Check if it's likely a network device
            if any('cisco' in match.get('name', '').lower() or 
                   'juniper' in match.get('name', '').lower() or
                   'mikrotik' in match.get('name', '').lower()
                   for match in os_matches):
                return 'Network Equipment'
            return 'Server'
        
        if 80 in tcp_ports or 443 in tcp_ports:  # HTTP/HTTPS
            return 'Server'
        
        if 3389 in tcp_ports:  # RDP
            return 'Computer'
        
        if 135 in tcp_ports or 139 in tcp_ports or 445 in tcp_ports:  # Windows services
            return 'Computer'
        
        # Default category
        return 'Network Device'
    
    def _extract_os_info(self, host_data: Dict) -> str:
        """
        Extract operating system information
        """
        osmatch = host_data.get('osmatch', [])
        if osmatch:
            return osmatch[0].get('name', 'Unknown OS')
        return 'Unknown OS'
    
    def _extract_mac_address(self, host_data: Dict) -> Optional[str]:
        """
        Extract MAC address if available
        """
        addresses = host_data.get('addresses', {})
        return addresses.get('mac')
    
    def _get_open_ports(self, host_data: Dict) -> str:
        """
        Get list of open ports as a string
        """
        tcp_ports = host_data.get('tcp', {})
        open_ports = [str(port) for port, port_data in tcp_ports.items() 
                     if port_data.get('state') == 'open']
        return ', '.join(open_ports) if open_ports else 'None'
    
    async def ping_sweep(self, subnet: str) -> List[str]:
        """
        Perform a simple ping sweep to find active hosts
        """
        logger.info(f"Starting ping sweep of {subnet}")
        active_hosts = []
        
        try:
            # This is a simplified implementation
            # In production, you might want to use a more sophisticated approach
            loop = asyncio.get_event_loop()
            scan_result = await loop.run_in_executor(
                None, 
                self._run_ping_scan, 
                subnet
            )
            
            active_hosts = [host for host in scan_result if scan_result[host]['status']['state'] == 'up']
            logger.info(f"Ping sweep completed. Found {len(active_hosts)} active hosts")
            
        except Exception as e:
            logger.error(f"Error during ping sweep: {str(e)}")
        
        return active_hosts
    
    def _run_ping_scan(self, subnet: str) -> Dict:
        """
        Run a simple ping scan
        """
        try:
            self.nm.scan(hosts=subnet, arguments='-sn')  # Ping scan only
            return self.nm.all_hosts()
        except Exception as e:
            logger.error(f"Ping scan failed: {str(e)}")
            return {}