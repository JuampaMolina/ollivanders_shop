from flask import jsonify
from flask_restful import abort

from repository.db import DB


class Service:
    """resource_fields = {
        'name': fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer
    }"""

    @staticmethod
    def get_item(name):

        if not name:
            abort(400, message="You must introduce the name")

        items = DB.get_item(name)

        if items.data == b"[]":
            return abort(404, message="There is no item with the name {}".format(name))

        return items

    @staticmethod
    def get_all_items():
        items = DB.get_all_items()

        if not items:
            abort(404, message="The inventory is empty")

        return items

    @staticmethod
    def load_database():
        try:
            DB.load_database()
            return jsonify({"message": "Database loaded succesfully"})
        except:
            return jsonify({"message": "It wasn't possible to load the database"})

    @staticmethod
    def delete_item(id):
        if not id:
            abort(400, message="You must introduce the item id")
        try:
            response = DB.delete_item(id)
            return response
        except:
            return jsonify(
                {"message": "It wasn't possible delete the item with id: " + id}
            )

    @staticmethod
    def add_item():
        try:
            return DB.add_item()
        except:
            return jsonify(
                {"message": "It wasn't possible to load the item on the database"}
            )
