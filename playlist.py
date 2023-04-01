import json

import isodate

import datetime
from service import Service


class Playlist:
    def __init__(self, id):
        """Реализуйте класс `PlayList`, который инициализируется id плейлиста и имеет следующие публичные атрибуты:
        - название плейлиста
        - ссылку на плейлист"""

        self.id = id

        self.__youtube = Service().get_service()
        self.__playlist_info = self.__youtube.playlists().list(
            part='snippet',
            id=self.id
        ).execute()
        self.title = self.__playlist_info["items"][0]["snippet"]["localized"]["title"]
        self.url = f'https://www.youtube.com/playlist?list={self.id}'

        self.__pl_video = self.__youtube.playlistItems().list(playlistId=self.id,
                                                              part='contentDetails',
                                                              maxResults=50,
                                                              ).execute()
        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__pl_video['items']]

        self.__video_response = self.__youtube.videos().list(part='contentDetails,statistics',
                                                             id=','.join(video_ids)
                                                             ).execute()

    @property
    def total_duration(self):

        total_duration = datetime.timedelta()
        for video in self.__video_response['items']:
            # Длительности YouTube-видео представлены в ISO 8601 формате
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self):
        max_likes = 0
        for video in self.__video_response['items']:
            current_likes = video["statistics"]["likeCount"]
            if int(current_likes) > int(max_likes):
                max_likes = video["statistics"]["likeCount"]
                id_video = video["id"]

        link_best_video = f'https://www.youtube.com/watch?v={id_video}'
        return link_best_video

    def print_info_video_in_playlist(self):
        print(json.dumps(self.__video_response, indent=2, ensure_ascii=False))

    def print_info_playlist(self):
        print(json.dumps(self.__playlist_info, indent=2, ensure_ascii=False))
