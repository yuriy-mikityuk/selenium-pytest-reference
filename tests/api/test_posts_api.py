import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5


def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    payload = response.json()
    assert payload["id"] == 1
    assert payload["userId"] == 1
    assert "title" in payload
    assert "body" in payload


def test_get_missing_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/99999", timeout=TIMEOUT)

    assert response.status_code == 404
    assert "application/json" in response.headers["Content-Type"]
    assert response.json() == {}


def test_filter_posts_by_user_id():
    response = requests.get(f"{BASE_URL}/posts", params={"userId": 1}, timeout=TIMEOUT)

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, list)
    assert payload
    assert all(post["userId"] == 1 for post in payload)


def test_create_post():
    request_body = {
        "userId": 1,
        "title": "Test title",
        "body": "Test body",
    }

    response = requests.post(f"{BASE_URL}/posts", json=request_body, timeout=TIMEOUT)

    assert response.status_code == 201

    payload = response.json()
    assert payload["userId"] == 1
    assert payload["title"] == "Test title"
    assert payload["body"] == "Test body"
    assert "id" in payload


def test_update_post_title():
    response = requests.patch(f"{BASE_URL}/posts/1", json={"title": "Updated title"}, timeout=TIMEOUT)

    assert response.status_code == 200

    payload = response.json()
    assert payload["id"] == 1
    assert payload["title"] == "Updated title"
