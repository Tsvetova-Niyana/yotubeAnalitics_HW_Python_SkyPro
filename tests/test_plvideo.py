import pytest
from plvdeo import PLVideo


class TestPLVideo:
    def test_check_get_id_playlist(self):
        """Проверка получения id плейлиста (id_playlist) видео с помощью геттера"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert video_1.id_playlist == 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8'

    def test_check_get_id_video_in_playlist(self):
        """Проверка получения id видео (id_video) в плейлисте"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert video_1.id_video == 'jXjwWIMTugY'

    def test_check_playlist_name(self):
        """Проверка получения названия плейлиста (playlist_name)"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert video_1.playlist_name == 'РОК ЖИВ'

    def test_check_name_video(self):
        """Проверка получения названия видео (name_video)"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert video_1.name_video == 'Rammstein | РОК ЖИВ'

    def test_check_view_count(self):
        """Проверка получения количества просмотра видео (view_count)"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert video_1.view_count is not None

    def test_check_count_of_likes(self):
        """Проверка получения количества лайков видео (count_of_likes)"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert video_1.count_of_likes is not None

    def test_check_playlist(self):
        """Проверка получения ошибки при запросе параметра playlist (приватный)"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        with pytest.raises(AttributeError):
            str(video_1.__playlist)

    def test_check_repr(self):
        """Проверка корректности работы метода __repr__ для класса PLVideo"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert repr(video_1) == f'id_video: {video_1.id_video}\n' \
                                f'playlist: {video_1.id_playlist}\n' \
                                f'name_video: {video_1.name_video}\n' \
                                f'view_count_video: {video_1.view_count}\n' \
                                f'count_of_likes_video: {video_1.count_of_likes}\n' \
                                f'playlist_name: {video_1.playlist_name}'

    def test_check_str(self):
        """Проверка корректности работы метода __str__ для класса PLVideo"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert str(video_1) == f'{video_1.name_video} ({video_1.playlist_name})'

    def test_check_print_info(self):
        """Проверка работы метода print_info (функция для получения информации о плейлисте) для класса PLVideo"""
        video_1 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')
        assert str(video_1.print_info) is not None
