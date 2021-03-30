from mongoengine import *


class Inventory(Document):
    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()
