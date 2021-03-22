import json
import pytest


@pytest.mark.db_get_item
def test_get_item(client):
    rv = client.get('/item/Aged Brie')
    # assert b'[{"_id": {"$oid": "605890fbdf7ed8ef465527ee"},"name": "Aged Brie","sell_in": 2,"quality": 0}]' in rv.data
    # assert DB.get_item("Aged Brie") == [{'_id': {'$oid': '605890fbdf7ed8ef465527ee'}, 'name': 'Aged Brie', 'quality': 0, 'sell_in': 2}]
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
