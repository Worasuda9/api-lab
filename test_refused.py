import uuid


def new_user():
    name = "lab-" + uuid.uuid4().hex[:12]
    return {"username": name, "password": "Pizza-2026"}


# A second user with an existing name is refused with 400 and an error message.
def test_duplicate_user_is_refused(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# Logging in with a wrong password is refused with 401 and an error message.
def test_wrong_password_is_refused(api):
    user = new_user()
    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    wrong_password = {"username": user["username"], "password": "wrong-password"}
    res = api.post("/api/users/token/login", json=wrong_password)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# An empty username is refused with 400 and an error message.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}
