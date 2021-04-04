from flask import jsonify, Response
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
    def add_item(args):
        DB.add_item(args)
        response = jsonify(
            {'message': 'Item added successfully'}
        )
        response.status_code = 201
        return response