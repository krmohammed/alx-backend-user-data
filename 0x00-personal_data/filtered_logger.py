#!/usr/bin/env python3
"""filter datum function"""
import re
from typing import List


def filter_datum(fields: List, redaction: str, message: str, separator: str) -> None:
    """filter datum"""
    for field in message.split(separator):
        if field.split('=')[0] in fields:
            message = re.sub(field.split('=')[1], redaction, message)
    print(message)
