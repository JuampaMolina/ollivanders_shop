import pytest

from repository.db import DB


@pytest.mark.db_get_item
def test_get_item():
    assert DB.get_item("Aged Brie") == [["Aged Brie", 2, 0]]
