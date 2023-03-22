import os

from googleapiclient.discovery import build
import json


class Channel:
    def __init__(self, channel_id):
        """Модифицируйте метод `__init__`, чтобы при создании экземпляра класса происходила инициализация следующих
        атрибутов класса:

        - id канала
        - название канала
        - описание канала
        - ссылка на канал
        - количество подписчиков
        - количество видео
        - общее количество просмотров

        Сделайте так, чтобы можно было получить id канала, но нельзя было его изменять/удалять."""
        self.__id = channel_id

        self.channel = self.get_service().channels().list(id=self.id, part='snippet,statistics').execute()

        self.title_channel = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url_channel = "https://www.youtube.com/" + self.channel['items'][0]['snippet']['customUrl']
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def __repr__(self) -> str:
        return f"id канала: {self.id}\n" \
               f"Название канала: {self.title_channel}\n\n" \
               f"Описание канала: \n{self.description}\n\n" \
               f"Ссылка на канал: {self.url_channel}\n" \
               f"Количество подписчиков: {self.subscriber_count}\n" \
               f"Количество видео: {self.video_count}\n" \
               f"Общее количество просмотров: {self.view_count}"

    def __str__(self):
        return f"Youtube-канал: {self.title_channel}"

    @property
    def id(self):
        """Геттер для id канала"""
        return self.__id

    @classmethod
    def get_service(cls):
        """Реализуйте метод класса, который возвращает объект для работы с API ютуба.
        Используйте этот метод в классе, чтобы избежать дублирования кода."""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, name_file):
        """Реализуйте метод, который сохраняет информацию по каналу, хранящуюся в атрибутах экземпляра класса Channel,
        в json-файл. Продумайте самостоятельно формат записи в файл."""
        data = {
            "id": self.id,
            "title_channel": self.title_channel,
            "description": self.description,
            "url_channel": self.url_channel,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(name_file, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def print_info(self):
        """Функция вывода информации о канале"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
