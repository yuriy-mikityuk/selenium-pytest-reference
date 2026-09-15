import requests
"""
Для тебя сейчас лучший вариант — JSONPlaceholder.
Это бесплатный API без регистрации. Он поддерживает GET, POST, PUT, PATCH, DELETE, фильтрацию и вложенные ресурсы. Сегодня эндпоинт отвечает нормально.
Первое упражнение:
GET https://jsonplaceholder.typicode.com/posts/1
Создай:
tests/api/test_posts_api.py
И самостоятельно проверь:
•
статус ответа — 200;
•
Content-Type содержит application/json;
•
тело преобразуется через response.json();
•
id == 1;
•
присутствуют поля userId, title и body.
Важное ограничение: JSONPlaceholder имитирует запись данных, но фактически не сохраняет результаты POST, PUT, PATCH и DELETE. Поэтому после POST нельзя проверять сохранение повторным GET — это прямо указано в официальном руководстве.
После него можно перейти к:
•
httpbin — параметры, заголовки, cookies, авторизация, редиректы и разные статус-коды;
•
Restful Booker — полноценный CRUD, токен авторизации и намеренно оставленные ошибки для поиска.
Но начинал бы именно с JSONPlaceholder и одного GET-теста. Готовый код пока писать не буду — лучше ты попробуешь сам.
"""
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_typicode_first():
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == 1
    assert payload["userId"] == 1
    assert "title" in payload
    assert "body" in payload

    content_type = response.headers["Content-Type"]
    assert "application/json" in content_type

def test_absence_of_post():
    url = f"{BASE_URL}/posts/99999"
    response = requests.get(url, timeout=5)
    assert response.status_code == 404
    content_type = response.headers["Content-Type"]
    assert "application/json" in content_type
    payload = response.json()
    assert payload == {}, "Ошибка при получении данных"

def test_filter_posts_by_user_id():
    url = f"{BASE_URL}/posts"
    response = requests.get(url, params={"userId": 1},timeout=5)
    payload = response.json()
    assert isinstance(payload, list)
    assert payload
    assert response.status_code == 200
    assert all(post["userId"] == 1 for post in payload)

def test_create_post():
    url = f"{BASE_URL}/posts"
    request_body = {
        "userId": 1,
        "title": "Test title",
        "body": "Test body",
    }

    response = requests.post(url, json=request_body)

    assert response.status_code == 201

    payload = response.json()
    assert payload["userId"] == 1
    assert payload["title"] == "Test title"
    assert payload["body"] == "Test body"
    assert "id" in payload

def test_update_post_title():
    url = f"{BASE_URL}/posts/1"
    update_data = {
        "title": "Updated title"
    }

    response = requests.patch(
        url=url,
        json=update_data
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["id"] == 1
    assert payload["title"] == "Updated title"
