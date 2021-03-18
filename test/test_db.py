import pytest

from repository.db import DB


@pytest.mark.db_get_item
def test_get_item():
    assert DB.get_item("Aged Brie") == [{
            "name": "Aged Brie",
            "sell_in": 2,
            "quality": 0
        },
        {
            "name": "Aged Brie",
            "sell_in": 5,
            "quality": 2
        }]
