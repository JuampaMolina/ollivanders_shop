from flask import Flask
from flask_restful import Resource, Api
from controller.items import Items
from controller.inventory import Inventory
from controller.load_data import LoadData

app = Flask(__name__)
api = Api(app)


class WelcomeOllivanders(Resource):
    def get(self):
        return {'Welcome': 'Ollivanders'}


api.add_resource(WelcomeOllivanders, '/')
api.add_resource(Items, '/item/<name>')
api.add_resource(Inventory, '/inventory')
api.add_resource(LoadData, '/load')

if __name__ == '__main__':
    app.run(debug=True)
