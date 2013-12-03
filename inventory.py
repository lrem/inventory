#!/usr/bin/env python
"""
Inventory
=========

Keep track of your attic treasury.
"""

from flask import Flask, g, render_template, request, flash, redirect, url_for
import sqlite3
import os

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
    roots = g.db.execute('SELECT * FROM storage '
                         'WHERE parent IS NULL').fetchall()
    body = ""
    for root in roots:
        body += list_storage(root)
    return render_template('list.html', body=body)


def list_storage(row):
    """
    List (in html) the contents of storage given by `row`.
    """
    inside = g.db.execute('SELECT * FROM storage WHERE parent=?',
                          [row[0]]).fetchall()
    return render_template('item.html', id=row[0], name=row[2],
                           description=row[3],
                           inside=map(list_storage, inside))


@APP.route('/add/<int:parent>', methods=['GET', 'POST'])
def add(parent):
    """
    Add a new item.
    """
    if request.method == 'POST':
        g.db.execute('INSERT INTO storage (parent, name, description) '
                     'VALUES (?,?,?)', [request.form['parent'],
                                        request.form['name'],
                                        request.form.get('description', None)])
        g.db.commit()
        flash('OK')
        return redirect(url_for('list_inventory'))
    else:
        return render_template('edit.html', parent=parent,
                               options=storage_options())


def storage_options():
    """
    Prepare a list of storage options for `select` tags.
    """
    roots = g.db.execute('SELECT * FROM storage '
                         'WHERE parent IS NULL').fetchall()
    options = []
    for root in roots:
        options_rec(options, root, 0)
    return options


def options_rec(options, row, depth):
    """
    Recursion for gathering the storage options.
    """
    options.append((row[0], '&nbsp;&nbsp;' * depth + row[2]))
    children = g.db.execute('SELECT * FROM storage WHERE parent=?',
                            [row[0]]).fetchall()
    for child in children:
        options_rec(options, child, depth+1)

if __name__ == '__main__':
    APP.secret_key = os.urandom(24)
    APP.run(debug=True)
