"""
MP09: REST API Client

PCPP Objectives: 4.1, 4.2, 4.3, 4.4

REST client implementation.
"""

from typing import Any, Dict, Optional

import requests


class RESTClient:
    """REST API client for CRUD operations."""
    
    def __init__(self, base_url: str) -> None:
        """Initialize REST client.
        
        Args:
            base_url: Base URL for API
        """
        # TODO: Implement initialization
        pass
    
    def get(self, resource: str, resource_id: Optional[str] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """GET request to fetch data.
        
        Args:
            resource: Resource name (e.g., 'users')
            resource_id: Optional resource ID
            params: Query parameters
            
        Returns:
            Response data as dictionary
        """
        # TODO: Implement GET request
        pass
    
    def create(self, resource: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """POST request to create new resource."""
        # TODO: Implement POST request
        pass
    
    def update(self, resource: str, resource_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """PUT request to update resource."""
        # TODO: Implement PUT request
        pass
    
    def delete(self, resource: str, resource_id: str) -> None:
        """DELETE request to delete resource."""
        # TODO: Implement DELETE request
        pass
