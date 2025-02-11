import pytest
from screenpy import Actor
from boldback.requests.get_users_request import get_users


@pytest.mark.parametrize("page,expected_status_code,expected_empty", [
    (1, 200, False),
    (2, 200, False),
    (98767, 200, True),
    (0, 200, False)
])
def test_get_users(page, expected_status_code, expected_empty):
    actor = Actor.named("Test User")

    response = get_users(page)

    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, but got {response.status_code}"

    response_json = response.json()

    assert "page" in response_json, "Response does not contain 'page'"
    assert "per_page" in response_json, "Response does not contain 'per_page'"
    assert "total" in response_json, "Response does not contain 'total'"
    assert "total_pages" in response_json, "Response does not contain 'total_pages'"
    assert "data" in response_json, "Response does not contain 'data'"
    assert "support" in response_json, "Response does not contain 'support'"
    assert "url" in response_json["support"], "Support section does not contain 'url'"
    assert "text" in response_json["support"], "Support section does not contain 'text'"

    if expected_empty:
        assert len(response_json["data"]) == 0, f"Expected empty 'data' array, but got {len(response_json['data'])} items"
    else:
        assert len(response_json["data"]) > 0, f"Expected non-empty 'data' array, but got empty"

        for user in response_json["data"]:
            assert "id" in user, "User data does not contain 'id'"
            assert isinstance(user["id"], int), "'id' should be an integer"

            assert "email" in user, "User data does not contain 'email'"
            assert isinstance(user["email"], str) and "@" in user["email"], "Invalid email format"

            assert "first_name" in user, "User data does not contain 'first_name'"
            assert isinstance(user["first_name"], str) and len(user["first_name"]) > 0, "Invalid first_name"

            assert "last_name" in user, "User data does not contain 'last_name'"
            assert isinstance(user["last_name"], str) and len(user["last_name"]) > 0, "Invalid last_name"

            assert "avatar" in user, "User data does not contain 'avatar'"
            assert isinstance(user["avatar"], str) and user["avatar"].startswith("https://"), "Invalid avatar URL"

    assert 'Content-Type' in response.headers, "Response does not contain 'Content-Type' header"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Content-Type is not as expected"
