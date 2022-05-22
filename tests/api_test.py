from run import app


class TestApi:

    def test_app_all_posts_code(self):
        """Проверяем, получили ли адекватный список"""
        response = app.test_client().get("/api/posts", follow_redirects=True)

#        print(response.status_code)
#        print(response.minetype)

        assert response.status_code == 200, "Статус код запросов всех постов неверный"
        assert response.minetype == "application/json", "Получен на JSON"

    def test_app_one_posts_code(self):
        """Проверяем, получили ли вообще адекватный список"""
        response = app.test_client().get("/api/posts/1", follow_redirects=True)

#        print(response.status_code)
#        print(response.minetype)

        assert response.status_code == 200, "Статус код запросов всех постов неверный"
        assert response.minetype == "application/json", "Получен на JSON"