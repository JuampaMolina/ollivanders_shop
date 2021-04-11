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
        "name": "Backstage Pass",
        "sell_in": 14,
        "quality": 21,
    },
    {
        "name": "Backstage Pass",
        "sell_in": 9,
        "quality": 50,
    },
    {
        "name": "Backstage Pass",
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


# USERS TESTS


@pytest.mark.db_get_users
def test_get_users(client):
    rv = client.get("/user")
    assert json.loads(rv.data) == expectedUsers


@pytest.mark.db_register_user
def test_register_user(client):
    rv1 = client.post(
        "/user?user_name=Test&email=test@gmail.com&password=test&credit=50"
    )
    assert json.loads(rv1.data) == {"message": "User Test added successfully"}
    rv2 = client.get("/user")
    expectedUsersAfterPost = expectedUsers.copy()
    expectedUsersAfterPost.append(
        {
            "user_name": "Test",
            "email": "test@gmail.com",
            "password": "test",
            "credit": 50,
            "inventory": [],
        }
    )
    assert json.loads(rv2.data) == expectedUsersAfterPost


@pytest.mark.db_buy_item
def test_buy_item(client):
    # Case can pay it and item exist
    rv1 = client.put("/buy?user_name=Juampa&name=Elixir of the Mongoose")
    assert json.loads(rv1.data) == {
        "message": "Congratulations Juampa item Elixir of the Mongoose buyed successfully"
    }
    rv2 = client.get("/user")
    expectedUsersBuyItem = expectedUsers.copy()
    expectedUsersBuyItem.remove(
        {
            "user_name": "Juampa",
            "email": "juampa@gmail.com",
            "password": "test",
            "credit": 50,
            "inventory": [],
        }
    )
    expectedUsersBuyItem.append(
        {
            "user_name": "Juampa",
            "email": "juampa@gmail.com",
            "password": "test",
            "credit": 43,
            "inventory": [
                {"name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7}
            ],
        }
    )
    assert json.loads(rv2.data) == expectedUsersBuyItem

    # Case can't pay it
    rv3 = client.put("/buy?user_name=Juampa&name=Sulfuras, Hand of Ragnaros")
    assert json.loads(rv3.data) == {"message": "You do not have enough credits"}
    rv4 = client.get("/user")
    assert json.loads(rv4.data) == expectedUsersBuyItem

    # Case item doesn't exist
    rv5 = client.put("/buy?user_name=Juampa&name=I don't exist")
    assert json.loads(rv5.data) == {"message": "No item found with that name"}
    rv6 = client.get("/user")
    assert json.loads(rv6.data) == expectedUsersBuyItem


@pytest.mark.db_get_personal_inventory
def test_get_personal_inventory(client):
    # Juampa buys item
    rv1 = client.put("/buy?user_name=Juampa&name=Elixir of the Mongoose")
    assert json.loads(rv1.data) == {"message": "Congratulations Juampa item Elixir of the Mongoose buyed successfully"}

    # User have items
    rv2 = client.put("/user/inventory?user_name=Juampa&password=test")
    assert json.loads(rv2.data) == [
        {
            "name": "Elixir of the Mongoose",
            "sell_in": 5,
            "quality": 7
        }
    ]

    # User doesn't have items
    rv3 = client.put("/user/inventory?user_name=Charlos&password=test")
    assert json.loads(rv3.data) == {"message": "The user Charlos doesn't have any items"}

    # Incorrect password
    rv4 = client.put("/user/inventory?user_name=Charlos&password=incorrect")
    assert json.loads(rv4.data) == {"message": "There is no user with this name and password"}
