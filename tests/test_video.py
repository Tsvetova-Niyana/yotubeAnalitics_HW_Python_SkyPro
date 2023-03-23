import pytest
from video import Video


class TestVideo:
    def test_check_get_video_id(self):
        """Проверка получения id видео (id) с помощью геттера при инициализации"""
        video_1 = Video('jXjwWIMTugY')
        assert video_1.id == 'jXjwWIMTugY'

    def test_check_name_video(self):
        """Проверка получения названия видео (name_video) с помощью геттера при инициализации"""
        video_1 = Video('jXjwWIMTugY')
        assert video_1.name_video == 'Rammstein | РОК ЖИВ'

    def test_check_view_count_video(self):
        """Проверка получения количества просмотров видео (view_count) с помощью геттера при инициализации/
        Значение динамически меняется"""
        video_1 = Video('jXjwWIMTugY')
        assert video_1.view_count is not None

    def test_check_count_of_likes_video(self):
        """Проверка получения количества лайков видео (count_of_likes) с помощью геттера при инициализации.
        Значение динамически меняется"""
        video_1 = Video('jXjwWIMTugY')
        assert video_1.count_of_likes is not None

    def test_check_repr_video(self):
        """Проверка корректности работы метода repr для класса Video"""
        video_1 = Video('jXjwWIMTugY')
        assert repr(video_1) == f'id_video: {video_1.id}\n' \
                                f'name_video: {video_1.name_video}\n' \
                                f'view_count_video: {video_1.view_count}\n' \
                                f'count_of_likes_video: {video_1.count_of_likes}'

    def test_check_str_video(self):
        """Проверка корректности работы метода str для класса Video"""
        video_1 = Video('jXjwWIMTugY')
        assert str(video_1) == 'Rammstein | РОК ЖИВ'

    def test_check_print_info_video(self):
        """Проверка корректности работы метода str для класса Video"""
        video_1 = Video('jXjwWIMTugY')
        assert str(video_1.print_info) is not None
