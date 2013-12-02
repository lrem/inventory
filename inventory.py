#!/usr/bin/env python
"""
Inventory
=========

Keep track of your attic treasury.
"""

from flask import Flask, g
import sqlite3

#import flask

APP = Flask(__name__)
DATABASE = 'inventory.db'


@APP.before_request
def open_connection():
    """
    Provides database connection for the context object.
    """
    if getattr(g, 'db', None) is None:
        print "Connecting"
        g.db = sqlite3.connect(DATABASE)


@APP.teardown_appcontext
def close_connection(exception):
    """
    Closes the database connection once not needed.
    """
    # pylint: disable=W0613
    # Cause Flask needs me to accept the argument
    if g.db is not None:
        g.db.close()


@APP.route('/')
def list_inventory():
    """
    Show the contents of the database.
    """
    roots = g.db.execute('SELECT * FROM storage WHERE id=parent').fetchall()
    body = ""
    for root in roots:
        body += list_storage(root)
    return body


def list_storage(row):
    """
    List (in html) the contents of storage given by `row`.
    """
    body = '<span class="name">%s</span>' % (row[2])
    if row[3]:
        body += '<p class="description">%s</p>' % (row[3])
    inside = g.db.execute('SELECT * FROM storage WHERE parent=?' +
                          ' AND id!=parent',
                          [row[0]]).fetchall()
    if len(inside) > 0:
        body += '<ul class="storage">'
        for storage in inside:
            body += '<li>%s</li>' % list_storage(storage)
        body += '</ul>'
    return body

if __name__ == '__main__':
    APP.run(debug=True)
