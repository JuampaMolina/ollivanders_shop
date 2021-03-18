from flask_restful import Resource, fields, abort
from repository.db import DB


class Service:
    '''resource_fields = {
        'name': fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer
    }'''

    @staticmethod
    def get_item(name):

        if not name:
            abort(400, message="You must introduce the item name")

        items = DB.get_item(name)

        if not items:
            abort(404, message="The item {} doesn't exist".format(name))

        return items
