import json


def test_index(app, client):
    res = client.get('/api/v1/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))
