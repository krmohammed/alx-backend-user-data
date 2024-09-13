#!/usr/bin/env python3
"""Authentication script"""
from flask import request
from typing import List


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, exluded_paths: List[str]) -> bool:
        """Check if the request requires authentication
        based on the path and excluded paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieve the authorization header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """Retrieve the current user from the request"""
        return None
