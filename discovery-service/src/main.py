import asyncio
import logging
import time
from datetime import datetime
from scanner import NetworkScanner
from reporter import AssetReporter
from config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DiscoveryService:
    def __init__(self):
        self.scanner = NetworkScanner()
        self.reporter = AssetReporter()
        self.running = False
    
    async def run_discovery_cycle(self):
        """
        Run a single discovery cycle
        """
        logger.info("Starting discovery cycle...")
        start_time = time.time()
        
        try:
            # Authenticate with the API
            await self.reporter.authenticate()
            
            discovered_assets = []
            
            # Scan each configured subnet
            for subnet in settings.NETWORK_SUBNETS:
                logger.info(f"Scanning subnet: {subnet}")
                
                if settings.ENABLE_NMAP_SCAN:
                    nmap_results = await self.scanner.nmap_scan(subnet)
                    discovered_assets.extend(nmap_results)
                
                # Additional discovery methods can be added here
                # if settings.ENABLE_WMI_DISCOVERY:
                #     wmi_results = await self.scanner.wmi_discovery(subnet)
                #     discovered_assets.extend(wmi_results)
            
            # Report discovered assets to the API
            if discovered_assets:
                logger.info(f"Found {len(discovered_assets)} assets")
                await self.reporter.report_assets(discovered_assets)
            else:
                logger.info("No assets discovered in this cycle")
            
        except Exception as e:
            logger.error(f"Error in discovery cycle: {str(e)}")
        
        finally:
            duration = time.time() - start_time
            logger.info(f"Discovery cycle completed in {duration:.2f} seconds")
    
    async def start(self):
        """
        Start the discovery service
        """
        logger.info("Starting Discovery Service...")
        logger.info(f"Scanning subnets: {settings.NETWORK_SUBNETS}")
        logger.info(f"Scan interval: {settings.SCAN_INTERVAL_MINUTES} minutes")
        
        self.running = True
        
        while self.running:
            try:
                await self.run_discovery_cycle()
                
                # Wait for the next cycle
                await asyncio.sleep(settings.SCAN_INTERVAL_MINUTES * 60)
                
            except KeyboardInterrupt:
                logger.info("Discovery service stopped by user")
                break
            except Exception as e:
                logger.error(f"Unexpected error: {str(e)}")
                # Wait before retrying
                await asyncio.sleep(60)
    
    def stop(self):
        """
        Stop the discovery service
        """
        logger.info("Stopping Discovery Service...")
        self.running = False


async def main():
    """
    Main entry point
    """
    service = DiscoveryService()
    
    try:
        await service.start()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        service.stop()


if __name__ == "__main__":
    asyncio.run(main())