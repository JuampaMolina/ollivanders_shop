from mongoengine import *


class Item(Document):
    _id = StringField(required=True)
    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()
