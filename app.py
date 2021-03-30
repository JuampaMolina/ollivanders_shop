from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import json
from controller.inventory import Inventory
from controller.items import Items
from services.service import Service
from repository.db_engine import init_app

app = Flask(__name__)
CORS(app)
api = Api(app)
init_app(app)

class WelcomeOllivanders(Resource):
    def get(self):
        return {"Welcome": "Ollivanders"}


@app.route("/home")
def show_inventory():
    items = json.loads(Service.get_all_items().data)
    return render_template("inventory.html", inventory=items)


api.add_resource(WelcomeOllivanders, "/")
api.add_resource(Items, "/item/<name>", "/item/delete/<id>", "/item/add")
api.add_resource(Inventory, "/inventory")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
