import json
from service import Service


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

        self.__channels = Service()
        self.channel = self.__channels.get_service().channels().list(id=self.id, part='snippet,statistics').execute()

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
        """Реализуйте для класса Канал магический метод для вывода через print() информации о канале:
        Youtube-канал: <название_канала>"""
        return f"Youtube-канал: {self.title_channel}"

    def __gt__(self, other):
        """Реализуйте возможность сравнивать два канала на больше между собой.
        Сравнение идет по количеству подписчиков."""
        if isinstance(other, Channel):
            return int(self.subscriber_count) > int(other.subscriber_count)
        else:
            raise TypeError("Сравниваются количества подписчиков каналов!")

    def __lt__(self, other):
        """Реализуйте возможность сравнивать два канала на меньше между собой.
            Сравнение идет по количеству подписчиков."""
        if isinstance(other, Channel):
            return int(self.subscriber_count) < int(other.subscriber_count)
        else:
            raise TypeError("Сравниваются количества подписчиков каналов!")

    def __add__(self, other):
        """Реализуйте возможность складывать два канала между собой.
        Сложение идет по количеству подписчиков."""
        if isinstance(other, Channel):
            return int(self.subscriber_count) + int(other.subscriber_count)
        else:
            raise TypeError("Складываются количества подписчики каналов!")

    @property
    def id(self):
        """Геттер для id канала"""
        return self.__id

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

    def print_info_video_by_channel(self):
        """Функция вывода информации о всех видео канала (можно дернуть id)"""
        video_info = self.__channels.get_service().search().list(channelId=self.id,
                                                                 part="snippet",
                                                                 type='video',
                                                                 order='rating',
                                                                 maxResults="15", ).execute()
        print(json.dumps(video_info, indent=2, ensure_ascii=False))

