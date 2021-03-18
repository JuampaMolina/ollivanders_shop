import pytest

from repository import db


@pytest.mark.db_get_item
def test_get_item():
    assert db.get_item("Aged Brie") == ["Aged Brie", 2, 0]
