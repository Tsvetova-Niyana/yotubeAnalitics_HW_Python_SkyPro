"""
Создайте класс Video. Для инициализации экземпляра Video используется id.
Сделайте так, чтобы дополнительно инициализировались такие атрибуты как

- название видео
- количество просмотров
- количество лайков
"""
import json
from service import Service


class Video:
    def __init__(self, id):
        self.__id_video = id

        video = Service()
        self.__video = video.get_service().videos().list(part='snippet,statistics', id=self.id).execute()

        self.name_video = self.__video["items"][0]["snippet"]["title"]
        self.view_count = self.__video["items"][0]["statistics"]["viewCount"]
        self.count_of_likes = self.__video["items"][0]["statistics"]["likeCount"]

    @property
    def id(self):
        return self.__id_video

    def __repr__(self):
        return f'id_video: {self.id}\n' \
               f'name_video: {self.name_video}\n' \
               f'view_count_video: {self.view_count}\n' \
               f'count_of_likes_video: {self.count_of_likes}'

    def __str__(self):
        return f'{self.name_video}'

    def print_info(self):
        """Функция вывода информации о видео"""
        print(json.dumps(self.__video, indent=2, ensure_ascii=False))
