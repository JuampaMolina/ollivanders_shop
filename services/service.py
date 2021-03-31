from flask import jsonify
from flask_restful import abort

from repository.db import DB


class Service:
    @staticmethod
    def check(items):
        if not items:
            abort(404, message="There are no items that meet the criterion")
        return items

    @staticmethod
    def get_inventory():
        return Service.check(DB.get_inventory())

    @staticmethod
    def get_item_by_name(name):
        return Service.check(DB.get_item_by_name(name))

    @staticmethod
    def get_item_by_quality(quality):
        return Service.check(DB.get_item_by_quality(quality))

    @staticmethod
    def get_item_by_sell_in(sell_in):
        return Service.check(DB.get_item_by_sell_in(sell_in))

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
