from flask import g, jsonify
from flask_restful import fields, marshal_with
from repository.db_engine import get_db


class DB:
    resource_fields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    @staticmethod
    @marshal_with(resource_fields)
    def get_inventory():
        db = get_db()
        inventory = []
        for object in g.Inventory.objects():
            inventory.append(object)
        return inventory

    @staticmethod
    @marshal_with(resource_fields)
    def get_item_by_name(name):
        db = get_db()
        items = []
        for object in g.Inventory.objects(name=name):
            items.append(object)
        return items

    @staticmethod
    @marshal_with(resource_fields)
    def get_item_by_quality(quality):
        db = get_db()
        items = []
        for object in g.Inventory.objects(quality=quality):
            items.append(object)
        return items

    @staticmethod
    @marshal_with(resource_fields)
    def get_item_by_sell_in(sell_in):
        db = get_db()
        items = []
        for object in g.Inventory.objects(sell_in__lte=sell_in):
            items.append(object)
        return items
