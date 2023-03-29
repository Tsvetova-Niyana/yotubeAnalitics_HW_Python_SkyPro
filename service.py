import os

from googleapiclient.discovery import build


class Service:

    @classmethod
    def get_service(cls):
        """Реализуйте метод класса, который возвращает объект для работы с API ютуба.
        Используйте этот метод в классе, чтобы избежать дублирования кода."""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
