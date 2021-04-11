import pytest
from flask import g
from mongoengine import connect

from controller.app_factory import create_app
from repository.models import Inventory, Users
from repository.db_engine import default_inventory, default_users


@pytest.fixture(autouse=True)
def client():
    app = create_app()
    app.app_context().push()  # Pusheamos el app_context para que sea accesible desde fuera.
    SetupTestDB.init_mock_db()
    return app.test_client()


class SetupTestDB:

    # Para poder acceder a la base de datos mockeada tenemos que pushear el app_context.
    @staticmethod
    def get_db():
        g.db = connect("mongoenginetest", host="mongomock://localhost")
        g.Inventory = Inventory
        g.Users = Users
        return g.db

    @staticmethod
    def init_mock_db():
        db = SetupTestDB.get_db()

        Inventory.drop_collection()
        Users.drop_collection()  # importante eliminar todos los documentos antes de
        # añadirlos porque el fixture se ejecuta antes de cada test.
        for product in default_inventory:
            Inventory(
                name=product["name"],
                sell_in=product["sell_in"],
                quality=product["quality"],
            ).save()

        for user in default_users:
            Users(
                user_name=user["user_name"],
                email=user["email"],
                password=user["password"],
                credit=user["credit"],
                inventory=user["inventory"],
            ).save()
