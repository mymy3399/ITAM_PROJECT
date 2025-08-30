import asyncio
import logging
import aiohttp
from typing import List, Dict, Any, Optional
from config import settings

logger = logging.getLogger(__name__)


class AssetReporter:
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
        self.access_token: Optional[str] = None
    
    async def authenticate(self) -> bool:
        """
        Authenticate with the API and get access token
        """
        try:
            if not self.session:
                self.session = aiohttp.ClientSession()
            
            # Prepare login data
            login_data = aiohttp.FormData()
            login_data.add_field('username', settings.API_USERNAME)
            login_data.add_field('password', settings.API_PASSWORD)
            
            # Login to get token
            async with self.session.post(
                f"{settings.API_BASE_URL}/auth/login",
                data=login_data,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    self.access_token = data.get('access_token')
                    logger.info("Successfully authenticated with API")
                    return True
                else:
                    error_text = await response.text()
                    logger.error(f"Authentication failed: {response.status} - {error_text}")
                    return False
                    
        except Exception as e:
            logger.error(f"Error during authentication: {str(e)}")
            return False
    
    async def report_assets(self, assets: List[Dict[str, Any]]) -> bool:
        """
        Report discovered assets to the API
        """
        if not self.access_token:
            logger.error("Not authenticated. Cannot report assets.")
            return False
        
        success_count = 0
        error_count = 0
        
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        for asset in assets:
            try:
                success = await self._create_or_update_asset(asset, headers)
                if success:
                    success_count += 1
                else:
                    error_count += 1
                    
                # Small delay between requests to avoid overwhelming the API
                await asyncio.sleep(0.1)
                
            except Exception as e:
                logger.error(f"Error reporting asset {asset.get('asset_tag', 'unknown')}: {str(e)}")
                error_count += 1
        
        logger.info(f"Asset reporting completed. Success: {success_count}, Errors: {error_count}")
        return error_count == 0
    
    async def _create_or_update_asset(self, asset: Dict[str, Any], headers: Dict[str, str]) -> bool:
        """
        Create a new asset or update existing one
        """
        try:
            if not self.session:
                return False
            
            # First, try to find if asset already exists by IP address
            existing_asset = await self._find_asset_by_ip(asset['ip_address'], headers)
            
            if existing_asset:
                # Update existing asset
                asset_id = existing_asset['id']
                async with self.session.put(
                    f"{settings.API_BASE_URL}/assets/{asset_id}",
                    json=asset,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    if response.status == 200:
                        logger.info(f"Updated asset: {asset['asset_tag']} at {asset['ip_address']}")
                        return True
                    else:
                        error_text = await response.text()
                        logger.error(f"Failed to update asset {asset['asset_tag']}: {response.status} - {error_text}")
                        return False
            else:
                # Create new asset
                async with self.session.post(
                    f"{settings.API_BASE_URL}/assets/",
                    json=asset,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    if response.status == 200:
                        logger.info(f"Created new asset: {asset['asset_tag']} at {asset['ip_address']}")
                        return True
                    else:
                        error_text = await response.text()
                        logger.error(f"Failed to create asset {asset['asset_tag']}: {response.status} - {error_text}")
                        return False
                        
        except Exception as e:
            logger.error(f"Error in create_or_update_asset: {str(e)}")
            return False
    
    async def _find_asset_by_ip(self, ip_address: str, headers: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """
        Try to find existing asset by IP address
        """
        try:
            if not self.session:
                return None
            
            # Get all assets and search for matching IP
            # Note: This is not optimal for large datasets. 
            # In production, you might want to add a search endpoint to the API
            async with self.session.get(
                f"{settings.API_BASE_URL}/assets/",
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                if response.status == 200:
                    assets = await response.json()
                    for asset in assets:
                        if asset.get('ip_address') == ip_address:
                            return asset
                            
        except Exception as e:
            logger.error(f"Error searching for asset by IP {ip_address}: {str(e)}")
        
        return None
    
    async def close(self):
        """
        Close the HTTP session
        """
        if self.session:
            await self.session.close()
            self.session = None
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()