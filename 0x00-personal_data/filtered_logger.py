#!/usr/bin/env python3
"""filter datum function"""
import re


def filter_datum(fields, redaction, message, separator):
    """filter datum"""
    for field in message.split(separator):
        if field.split('=')[0] in fields:
            message = re.sub(field.split('=')[1], redaction, message)
    print(message)
