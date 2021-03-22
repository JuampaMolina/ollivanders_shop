from flask_restful import Resource
from services.service import Service


class LoadData(Resource):

    def get(self):
        return Service.load_database()