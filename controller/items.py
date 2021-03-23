from flask_restful import Resource

from services.service import Service


class Items(Resource):

    def get(self, key, value):
        return Service.get_item(key, value)

    def delete(self, id):
        return Service.delete_item(id)

    def post(self):
        return Service.add_item()
