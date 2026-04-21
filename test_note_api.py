import requests
import allure

@allure.epic("Note API")
@allure.feature("CRUD операции")
class TestNoteAPI:

    @allure.title("Создание заметки")
    @allure.description("POST /posts — создание новой записи")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_note(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        payload = {"title": "Моя заметка", "body": "Текст", "userId": 1}
        with allure.step("Отправка POST запроса"):
            response = requests.post(url, json=payload)
        with allure.step("Проверка статуса 201"):
            assert response.status_code == 201

    @allure.title("Получение всех заметок")
    @allure.description("GET /posts — получение списка")
    def test_get_all_notes(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        with allure.step("Отправка GET запроса"):
            response = requests.get(url)
        with allure.step("Проверка статуса 200"):
            assert response.status_code == 200

    @allure.title("Получение заметки по ID")
    @allure.description("GET /posts/1 — получение записи")
    def test_get_note_by_id(self):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        with allure.step("Отправка GET запроса"):
            response = requests.get(url)
        with allure.step("Проверка статуса 200"):
            assert response.status_code == 200

    @allure.title("Обновление заметки")
    @allure.description("PUT /posts/1 — обновление записи")
    def test_update_note(self):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        payload = {"id": 1, "title": "Новый заголовок", "body": "Новый текст", "userId": 1}
        with allure.step("Отправка PUT запроса"):
            response = requests.put(url, json=payload)
        with allure.step("Проверка статуса 200"):
            assert response.status_code == 200

    @allure.title("Удаление заметки")
    @allure.description("DELETE /posts/1 — удаление записи")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_note(self):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        with allure.step("Отправка DELETE запроса"):
            response = requests.delete(url)
        with allure.step("Проверка статуса 200"):
            assert response.status_code == 200
