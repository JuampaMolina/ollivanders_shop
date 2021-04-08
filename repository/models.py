from mongoengine import *


class Inventory(Document):
    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()


class Users(Document):
    user_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    inventory = ListField(ReferenceField(Inventory))
