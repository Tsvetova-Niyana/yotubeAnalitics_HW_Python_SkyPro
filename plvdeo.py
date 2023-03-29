"""
Создайте второй класс для видео PLVideo, который инициализируется айдишников видео и
айдишником плейлиста, в котором он находится.
Сделайте так, чтобы **дополнительно** инициализировались такие атрибуты экземпляра `PLVideo` как

- название видео
- количество просмотров
- количество лайков
- название плейлиста
"""
import json

from video import Video
from service import Service


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.__id_playlist = id_playlist

        playlist = Service()
        self.__playlist = playlist.get_service().playlists().list(
            part='snippet',
            id=id_playlist
        ).execute()

        self.playlist_name = self.__playlist["items"][0]["snippet"]["title"]

    @property
    def id_playlist(self):
        return self.__id_playlist

    def __repr__(self):
        return f'id_video: {self.id_video}\n' \
               f'playlist: {self.id_playlist}\n' \
               f'name_video: {self.name_video}\n' \
               f'view_count_video: {self.view_count}\n' \
               f'count_of_likes_video: {self.count_of_likes}\n' \
               f'playlist_name: {self.playlist_name}'

    def __str__(self):
        return f'{self.name_video} ({self.playlist_name})'

    def print_info(self):
        """Переопределение метода print_info для получения информации о плейлисте"""
        print(json.dumps(self.__playlist, indent=2, ensure_ascii=False))
