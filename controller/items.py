from flask_restful import Resource

from services.service import Service


class Items(Resource):
    def get(self, name):
        return Service.get_item_by_name(name)

    def delete(self, id):
        return Service.delete_item(id)

    def post(self):
        return Service.add_item()
