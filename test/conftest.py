import pytest
from flask import g
from mongoengine import connect

from controller.app_factory import create_app
from repository.model import Inventory


@pytest.fixture(autouse=True)
def client():
    app = create_app()
    app.app_context().push()  # Pusheamos el app_context para que sea accesible desde fuera.
    SetupTestDB.init_db()
    return app.test_client()


class SetupTestDB:
    default_inventory = [
        {
            "name": "Aged Brie",
            "sell_in": 2,
            "quality": 0,
        },
        {
            "name": "+5 Dexterity Vest",
            "sell_in": 10,
            "quality": 20,
        },
        {
            "name": "Elixir of the Mongoose",
            "sell_in": 5,
            "quality": 7,
        },
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": 0,
            "quality": 80,
        },
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": -1,
            "quality": 80,
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 15,
            "quality": 20,
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 10,
            "quality": 49,
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 5,
            "quality": 49,
        },
        {
            "name": "Conjured Mana Cake",
            "sell_in": 3,
            "quality": 6,
        },
    ]

    # Para poder acceder a la base de datos mockeada tenemos que pushear el app_context.
    @staticmethod
    def get_db():
        g.db = connect("mongoenginetest", host="mongomock://localhost")
        g.Inventory = Inventory
        return g.db

    @staticmethod
    def init_db():
        db = SetupTestDB.get_db()

        Inventory.drop_collection()  # importante eliminar todos los documentos antes de
        # añadirlos porque el fixture se ejecuta antes de cada test.
        for product in SetupTestDB.default_inventory:
            Inventory(
                name=product["name"],
                sell_in=product["sell_in"],
                quality=product["quality"],
            ).save()
