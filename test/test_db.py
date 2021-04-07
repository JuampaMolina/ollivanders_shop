import json
from test.conftest import SetupTestDB
import pytest

expectedInventory = SetupTestDB.default_inventory


@pytest.mark.db_get_item_by_name
def test_get_item_by_name(client):
    rv = client.get("/item/name/Aged Brie")
    assert json.loads(rv.data) == [{"name": "Aged Brie", "sell_in": 2, "quality": 0}]


@pytest.mark.db_get_inventory
def test_get_all_items(client):
    rv = client.get("/inventory")
    assert json.loads(rv.data) == expectedInventory
