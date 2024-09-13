#!/usr/bin/env python3
""" provides functions that handle personal data """

import re
from typing import List
import logging
from os import getenv
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """returns a log message obfuscated"""
    obfuscated_message = message
    for f in fields:
        message = re.sub(
            f"{f}=.*?{separator}", f"{f}={redaction}{separator}", message
        )
    return message


def get_logger() -> logging.Logger:
    """gets logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    s_handler = logging.StreamHandler()
    s_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(s_handler)
    return logger


def get_db() -> mysql.connector.MySQLConnection:
    """returns a connector to a database"""
    host = getenv("PERSONAL_DATA_DB_HOST", "localhost")
    user = getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = getenv("PERSONAL_DATA_DB_PASSWORD", "")
    database = getenv("PERSONAL_DATA_DB_NAME")
    config = {
        'user': username,
        'password': password,
        'host': host,
        'database': database,
    }
    return mysql.connector.connect(**config)


def main():
    """main"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    headings = [i[0] for i in cursor.description]
    logger = get_logger()

    for row in cursor:
        row_str = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, headings))
        logger.info(row_str.strip())
    cursor.close()
    db.close()


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)
