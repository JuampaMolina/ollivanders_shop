from flask_restful import Resource
from services.service import Service


class Items(Resource):

    def get(self, name):
        return Service.get_item(name)
