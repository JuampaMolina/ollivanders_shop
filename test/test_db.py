import json
import pytest


@pytest.mark.db_get_item_by_name
def test_get_item_by_name(client):
    rv = client.get("/item/Aged Brie")
    assert json.loads(rv.data) == [{"name": "Aged Brie", "sell_in": 2, "quality": 0}]


@pytest.mark.db_get_inventory
def test_get_all_items(client):
    rv = client.get("/inventory")
    assert json.loads(rv.data) == [
        {"name": "Aged Brie", "sell_in": 2, "quality": 0},
        {"name": "+5 Dexterity Vest", "sell_in": 10, "quality": 20},
        {"name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7},
        {"name": "Sulfuras, Hand of Ragnaros", "sell_in": 0, "quality": 80},
        {"name": "Sulfuras, Hand of Ragnaros", "sell_in": -1, "quality": 80},
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 15,
            "quality": 20,
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 10,
            "quality": 49,
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 5,
            "quality": 49,
        },
        {"name": "Conjured Mana Cake", "sell_in": 3, "quality": 6},
    ]
