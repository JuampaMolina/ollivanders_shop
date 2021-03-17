import pytest


@pytest.mark.welcome
def test_welcome(client):
    rv = client.get('/')
    assert b'{"Welcome": "Ollivanders"}' in rv.data
