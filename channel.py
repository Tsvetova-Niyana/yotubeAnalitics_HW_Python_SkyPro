import os
from googleapiclient.discovery import build
import json


class Channel:
    def __init__(self, channel_id):
        self.id = channel_id


    def print_info(self):
        api_key: str = os.getenv('API_KEY')

        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))
