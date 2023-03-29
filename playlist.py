import json
import os

import isodate
from googleapiclient.discovery import build
import datetime
from service import Service


class Playlist:
    def __init__(self, id):
        """Реализуйте класс `PlayList`, который инициализируется id плейлиста и имеет следующие публичные атрибуты:
        - название плейлиста
        - ссылку на плейлист"""

        self.id = id

        self.youtube = Service().get_service()
        self.playlist_info = self.youtube.playlists().list(
            part='snippet',
            id=self.id
        ).execute()
        self.title = self.playlist_info["items"][0]["snippet"]["localized"]["title"]
        self.link_playlist = f'https://www.youtube.com/playlist?list={self.id}'

    @property
    def sum_duration(self):
        # print(json.dumps(self.playlist_info, indent=2, ensure_ascii=False))
        # получить все id видеороликов из плейлиста
        self.pl_video = self.youtube.playlistItems().list(playlistId=self.id,
                                                          part='contentDetails',
                                                          maxResults=50,
                                                          ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.pl_video['items']]

        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()

        total_duration = datetime.timedelta()
        for video in video_response['items']:
            # Длительности YouTube-видео представлены в ISO 8601 формате
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration
