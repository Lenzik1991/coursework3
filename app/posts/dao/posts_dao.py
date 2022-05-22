import json


class PostsDAO:
    """Класс, ответственный за работу со всеми постами"""

    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(f"{self.path}", "r", encoding="UTF-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        """возвращает все посты"""
        return self._load()

    def get_by_pk(self, pk):
        """возвращает пост по его идентификатору"""
        posts = self.get_all()

        for post in posts:
            if post["pk"] == pk:
                return post

    def get_by_user(self, user_name):
        """возвращает посты определенного пользователя"""
        posts = self.get_all()
        posts_by_user = []

        for post in posts:
            if post["posts_name"] == user_name:
                posts_by_user.append(post)
        return posts_by_user

    def search(self, query):
        """возвращает список словарей по вхождению query"""
        posts = self.get_all()
        matching_posts = []
        query_lower = query.lower()

        for post in posts:
            if query_lower in post["content"].lower():
                matching_posts.append(post)

        return matching_posts