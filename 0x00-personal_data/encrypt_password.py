#!/usr/bin/env python3
"""provides the hashing function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password"""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password
