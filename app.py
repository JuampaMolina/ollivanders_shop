from flask import Flask
from flask_restful import Resource, Api
from controller.items import Items

app = Flask(__name__)
api = Api(app)


class WelcomeOllivanders(Resource):
    def get(self):
        return {'Welcome': 'Ollivanders'}


api.add_resource(WelcomeOllivanders, '/')
api.add_resource(Items, '/item/<name>')

if __name__ == '__main__':
    app.run(debug=True)
