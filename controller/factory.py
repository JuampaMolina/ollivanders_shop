from flask import Flask
from flask_restful import Resource, Api
from controller.items import Items
from controller.inventory import Inventory


def create_app():
    app = Flask(__name__)

    api = Api(app)

    class WelcomeOllivanders(Resource):
        def get(self):
            return {'Welcome': 'Ollivanders'}

    api.add_resource(WelcomeOllivanders, '/')
    api.add_resource(Items, '/item/<name>')
    api.add_resource(Inventory, '/inventory')

    return app
