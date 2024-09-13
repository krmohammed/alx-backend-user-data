#!/usr/bin/env python3
""" provides functions that handle personal data """

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """returns a log message obfuscated"""
    obfuscated_message = message
    for field in fields:
        message = re.sub(
            f"{field}=.*?{separator}", f"{field}={redaction}{separator}", message
        )
    return message
