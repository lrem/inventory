"""
Test suite for this small project.
Run with `nosetests`.
"""

import sqlite3

SCHEMA_PATH = 'schema.sql'
CONTENT_PATH = 'test/content.sql'


def test_schema():
    """
    Just see if the schema executes.
    """
    conn = sqlite3.connect(':memory:')
    conn.executescript(open(SCHEMA_PATH).read())
    return conn


def test_content():
    """
    Just see if the example content executes.
    """
    conn = test_schema()
    conn.executescript(open(CONTENT_PATH).read())
    return conn
