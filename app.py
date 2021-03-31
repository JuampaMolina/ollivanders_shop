from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import json
from controller.inventory import Inventory
from controller.items import Items
from controller.quality import Quality
from controller.sell_in import Sell_in
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
api.add_resource(Inventory, "/inventory")
api.add_resource(Items, "/item/<name>", "/item/delete/<id>", "/item/add")
api.add_resource(Quality, "/item/quality/<int:quality>")
api.add_resource(Sell_in, "/item/sell_in/<int:sell_in>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
