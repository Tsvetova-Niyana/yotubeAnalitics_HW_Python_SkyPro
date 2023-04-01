from playlist import Playlist


class TestPlaylist:
    def test_check_init_playlist(self):
        """Проверка инициализации экземпляра класса Playlist"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        assert playlist is not None

    def test_check_id_playlist(self):
        """Получение id плейлиста"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        assert playlist.id == 'PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5'

    def test_check_title_playlist(self):
        """Получение название (title) плейлиста"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        assert playlist.title == 'Пушной. ВСЕ каверы на 8-струнке. "А кому сейчас легко?"'

    def test_check_link_playlist(self):
        """Получение ссылки (url) плейлиста"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        assert playlist.url == 'https://www.youtube.com/playlist?list=PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5'

    def test_check_duration_playlist(self):
        """Получение длительности (duration) плейлиста"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        duration = playlist.total_duration
        assert str(duration) == '5:19:11'

    def test_check_type_duration_playlist(self):
        """Получение типа длительности (duration) плейлиста"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        duration = playlist.total_duration
        assert str(type(duration)) == "<class 'datetime.timedelta'>"

    def test_check_duration_in_second_playlist(self):
        """Получение длительности (duration) плейлиста в секундах"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        duration = playlist.total_duration
        assert str(duration.total_seconds()) == '19151.0'

    def test_check_url_best_video_playlist(self):
        """Получение ссылки на лучшее видео (show_best_video()) в плейлисте"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        assert str(playlist.show_best_video()) == 'https://www.youtube.com/watch?v=1bwXSOeP_Aw'

    def test_check_print_info_video_playlist(self):
        """Получение информации о видео (print_info_video_in_playlist()) в плейлисте"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        assert str(playlist.print_info_video_in_playlist) is not None

    def test_check_print_info_playlist(self):
        """Получение информации о (print_info_playlist()) плейлисте"""
        playlist = Playlist('PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5')
        assert str(playlist.print_info_playlist) is not None
