import pytest

@pytest.mark.parametrize(
    "excluded",
    [
        [],
        ["Knife"],
        ["Scissors"],
        ["Knife", "Scissors"],
    ],
)
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


@pytest.mark.xfail(
    reason="Defect 1: excluding all three tools returns 500 instead of 400 with a JSON error message.",
    strict=True,
)
def test_excluding_all_tools_returns_client_error(api, auth):
    body = {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 400
    error = res.json()
    assert isinstance(error, dict)
    assert isinstance(error.get("error"), str)
    assert error["error"]