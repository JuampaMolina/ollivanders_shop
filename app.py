from flask import Flask
from flask_restful import Resource, Api
from controller.items import Items
from controller.inventory import Inventory
from repository.db import DB

app = Flask(__name__)
api = Api(app)


class WelcomeOllivanders(Resource):
    def get(self):
        return {'Welcome': 'Ollivanders'}


api.add_resource(WelcomeOllivanders, '/')
api.add_resource(Items, '/item/<name>')
api.add_resource(Inventory, '/inventory')

DB.load_database();

if __name__ == '__main__':
    app.run(debug=True)
