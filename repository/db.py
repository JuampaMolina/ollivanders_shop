from mongoengine import *
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = connect(
            db='ollivanders_shop',
            host='mongodb+srv://admin:admin@ollivanders.8xp7x.mongodb.net/ollivanders_shop?retryWrites=true&w=majority'
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()