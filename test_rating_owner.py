def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    assert 400 <= res.status_code < 500

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


def test_other_user_cannot_change_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 5}, headers=other_auth)
    assert 400 <= res.status_code < 500

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    assert 400 <= res.status_code < 500

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating
