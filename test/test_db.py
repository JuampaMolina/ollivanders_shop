import json
from test.conftest import SetupTestDB
from repository.db_engine import default_inventory, default_users
import pytest

expectedInventoryDay0 = default_inventory
expectedInventoryDay1 = [
    {
        "name": "Aged Brie",
        "sell_in": 1,
        "quality": 1,
    },
    {
        "name": "+5 Dexterity Vest",
        "sell_in": 9,
        "quality": 18,
    },
    {
        "name": "Elixir of the Mongoose",
        "sell_in": 4,
        "quality": 6,
    },
    {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": 0,
        "quality": 80,
    },
    {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": -1,
        "quality": 80,
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 14,
        "quality": 21,
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 9,
        "quality": 50,
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 4,
        "quality": 50,
    },
    {
        "name": "Conjured Mana Cake",
        "sell_in": 2,
        "quality": 4,
    },
]

expectedUsers = default_users


@pytest.mark.db_get_inventory
def test_get_inventory(client):
    rv = client.get("/inventory")
    assert json.loads(rv.data) == expectedInventoryDay0


@pytest.mark.db_get_item_by_name
def test_get_item_by_name(client):
    rv = client.get("/item/name/Aged Brie")
    assert json.loads(rv.data) == [{"name": "Aged Brie", "sell_in": 2, "quality": 0}]


@pytest.mark.db_get_item_by_quality
def test_get_item_by_quality(client):
    rv = client.get("/item/quality/80")
    assert json.loads(rv.data) == [
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": 0,
            "quality": 80,
        },
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": -1,
            "quality": 80,
        },
    ]


@pytest.mark.db_get_item_by_sell_in
def test_get_item_by_sell_in(client):
    rv = client.get("/item/sell_in/2")
    assert json.loads(rv.data) == [
        {"name": "Aged Brie", "sell_in": 2, "quality": 0},
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": 0,
            "quality": 80,
        },
        {
            "name": "Sulfuras, Hand of Ragnaros",
            "sell_in": -1,
            "quality": 80,
        },
    ]


@pytest.mark.db_delete_item
def test_delete_item(client):
    rv1 = client.delete("/item?name=Aged Brie&sell_in=2&quality=0")
    assert json.loads(rv1.data) == {"message": "Item Aged Brie deleted successfully"}
    rv2 = client.get("/inventory")
    expectedInventoryAfterDelete = expectedInventoryDay0.copy()
    expectedInventoryAfterDelete.remove(
        {"name": "Aged Brie", "sell_in": 2, "quality": 0}
    )
    assert json.loads(rv2.data) == expectedInventoryAfterDelete


@pytest.mark.db_add_item
def test_add_item(client):
    rv1 = client.post("/item?name=Test&sell_in=4&quality=10")
    assert json.loads(rv1.data) == {"message": "Item Test added successfully"}
    rv2 = client.get("/inventory")
    expectedInventoryAfterPost = expectedInventoryDay0.copy()
    expectedInventoryAfterPost.append({"name": "Test", "sell_in": 4, "quality": 10})
    assert json.loads(rv2.data) == expectedInventoryAfterPost


@pytest.mark.db_update_quality
def test_update_quality(client):
    rv = client.get("/update_quality")
    assert json.loads(rv.data) == expectedInventoryDay1


# USERS

@pytest.mark.db_get_users
def test_get_users(client):
    rv = client.get("/user")
    assert json.loads(rv.data) == expectedUsers


@pytest.mark.db_register_user
def test_register_user(client):
    rv1 = client.post("/user?user_name=Test&email=test@gmail.com&password=test&credit=50")
    assert json.loads(rv1.data) == {"message": "User Test added successfully"}
    rv2 = client.get("/user")
    expectedUsersAfterPost = expectedUsers.copy()
    expectedUsersAfterPost.append({
        "user_name": "Test",
        "email": "test@gmail.com",
        "password": "test",
        "credit": 50,
        "inventory": []
    })
    assert json.loads(rv2.data) == expectedUsersAfterPost
