import json
import pytest
from repository.db import DB


@pytest.mark.db_get_item
def test_get_item(client):
    rv = client.get('/item/Aged Brie')
    assert json.loads(rv.data) == [
        {
            "_id": {
                "$oid": "605890fbdf7ed8ef465527ee"
            },
            "name": "Aged Brie",
            "sell_in": 2,
            "quality": 0
        }
    ]

@pytest.mark.db_get_inventory
def test_get_all_items(client):
    DB.load_database()
    rv = client.get('/inventory')
    assert json.loads(rv.data) == [
    {
        "_id": {
            "$oid": "605890fbdf7ed8ef465527ee"
        },
        "name": "Aged Brie",
        "sell_in": 2,
        "quality": 0
    },
    {
        "_id": {
            "$oid": "6058c0385a343a36b273fd71"
        },
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20
    },
    {
        "_id": {
            "$oid": "6058c0395a343a36b273fd72"
        },
        "name": "Elixir of the Mongoose",
        "sell_in": 5,
        "quality": 7
    },
    {
        "_id": {
            "$oid": "6058c0395a343a36b273fd73"
        },
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": 0,
        "quality": 80
    },
    {
        "_id": {
            "$oid": "6058c0395a343a36b273fd74"
        },
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": -1,
        "quality": 80
    },
    {
        "_id": {
            "$oid": "6058c0395a343a36b273fd75"
        },
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 15,
        "quality": 20
    },
    {
        "_id": {
            "$oid": "6058c0395a343a36b273fd76"
        },
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 10,
        "quality": 49
    },
    {
        "_id": {
            "$oid": "6058c0395a343a36b273fd77"
        },
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 5,
        "quality": 49
    },
    {
        "_id": {
            "$oid": "6058c0395a343a36b273fd78"
        },
        "name": "Conjured Mana Cake",
        "sell_in": 3,
        "quality": 6
    }
]
