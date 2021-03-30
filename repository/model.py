from mongoengine import *


class Inventory(Document):
    _id = StringField(required=True)
    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()
