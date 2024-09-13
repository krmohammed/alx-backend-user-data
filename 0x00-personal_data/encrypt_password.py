#!/usr/bin/env python3
"""provides the hashing function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password"""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
