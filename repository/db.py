from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://admin:admin@ollivanders.8xp7x.mongodb.net/ollivanders_shop?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('ollivanders_shop')
inventory = pymongo.collection.Collection(db, 'inventory')

class DB:

    products = [
        {
            "name": "+5 Dexterity Vest",
            "sell_in": 10,
            "quality": 20
        },
        {
            "name": "Aged Brie",
            "sell_in": 2,
            "quality": 0
        },
        {
            "name": "Elixir of the Mongoose",
            "sell_in": 5,
            "quality": 7
        },
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": 0,
            "quality": 80
        },
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": -1,
            "quality": 80
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 15,
            "quality": 20
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 10,
            "quality": 49
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 5,
            "quality": 49
        },
        {
            "name": "Conjured Mana Cake",
            "sell_in": 3,
            "quality": 6
        }
    ]

    @staticmethod
    def load_database():
        for product in DB.products:
            inventory.insert_one(product)

    @staticmethod
    def get_all_items():
        return DB.products

    @staticmethod
    def get_item(name):
        items = DB.products
        return [item for item in items if item["name"] == name]
