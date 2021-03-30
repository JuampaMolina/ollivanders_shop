from mongoengine import *
from repository.model import Inventory
import click
from flask.cli import with_appcontext
from flask import g
from flask_pymongo import ObjectId


def get_db():
    if 'db' not in g:
        g.db = connect(
            db='ollivanders_shop',
            host='mongodb+srv://admin:admin@ollivanders.8xp7x.mongodb.net/ollivanders_shop?retryWrites=true&w=majority'
        )
        g.Inventory = Inventory
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# Poblar Base de Datos
def init_db():
    db = get_db()

    default_inventory = [
        {
            "_id": ObjectId("605890fbdf7ed8ef465527ee"),
            "name": "Aged Brie",
            "sell_in": 2,
            "quality": 0,
        },
        {
            "_id": ObjectId("6058c0385a343a36b273fd71"),
            "name": "+5 Dexterity Vest",
            "sell_in": 10,
            "quality": 20,
        },
        {
            "_id": ObjectId("6058c0395a343a36b273fd72"),
            "name": "Elixir of the Mongoose",
            "sell_in": 5,
            "quality": 7,
        },
        {
            "_id": ObjectId("6058c0395a343a36b273fd73"),
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": 0,
            "quality": 80,
        },
        {
            "_id": ObjectId("6058c0395a343a36b273fd74"),
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": -1,
            "quality": 80,
        },
        {
            "_id": ObjectId("6058c0395a343a36b273fd75"),
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 15,
            "quality": 20,
        },
        {
            "_id": ObjectId("6058c0395a343a36b273fd76"),
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 10,
            "quality": 49,
        },
        {
            "_id": ObjectId("6058c0395a343a36b273fd77"),
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 5,
            "quality": 49,
        },
        {
            "_id": ObjectId("6058c0395a343a36b273fd78"),
            "name": "Conjured Mana Cake",
            "sell_in": 3,
            "quality": 6,
        },
    ]

    for product in default_inventory:
        Inventory(_id=str(product['_id']), name=product['name'], sell_in=product['sell_in'],
                  quality=product['quality'], ).save()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('¡Base de datos inicializada y poblada!')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
