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
        items = DB.get_inventory()
        if not items:
            response = jsonify({"message": "The inventory is empty"})
            response.status_code = 404
            return response
        else:
            return items

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
    def add_item(args):
        DB.add_item(args)
        response = jsonify(
            {"message": "Item {} added successfully".format(args["name"])}
        )
        response.status_code = 201
        return response

    @staticmethod
    def delete_item(args):
        item = DB.delete_item(args)
        if item["name"] is None:
            response = jsonify({"message": "Item {} not found".format(args["name"])})
            response.status_code = 404
            return response

        response = jsonify(
            {"message": "Item {} deleted successfully".format(item["name"])}
        )
        response.status_code = 201
        return response

    @staticmethod
    def update_quality():
        return DB.update_quality()

    ## USERS

    @staticmethod
    def register_user(args):
        DB.register_user(args)
        response = jsonify(
            {"message": "User {} added successfully".format(args["user_name"])}
        )
        response.status_code = 201
        return response
