#!/usr/bin/env python3
"""Authentication script"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the request requires authentication
        based on the path and excluded paths
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) < 1:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve the authorization header from the request"""
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """Retrieve the current user from the request"""
        return None
