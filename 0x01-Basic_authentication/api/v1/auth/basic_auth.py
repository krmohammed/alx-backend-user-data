#!/usr/bin/env python3
"""Provides the class BasicAuth"""
from api.v1.auth.auth import Auth
import binascii
import base64


class BasicAuth(Auth):
    """Basic authentication"""

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """Extract the base64 part of the authorization header"""
        if auth_header is None:
            return None
        if not isinstance(auth_header, str):
            return None
        if not auth_header.startswith("Basic "):
            return None
        return auth_header[6:]

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """Decode the base64 authorization header"""
        if b64_auth_header is None:
            return None
        if not isinstance(b64_auth_header, str):
            return None
        try:
            return base64.b64decode(b64_auth_header).decode("utf-8")
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, d_b64_aut_head: str) -> (str, str):
        """Extract user credentials from the base64
        decoded authorization header
        """
        if d_b64_aut_head is None:
            return None, None
        if not isinstance(d_b64_aut_head, str):
            return None, None
        parts = d_b64_aut_head.split(":")
        if len(parts) != 2:
            return None, None
        return parts[0], parts[1]
