import pytest

from channel import Channel


class TestChannel:
    def test_method_str_as_magical_method(self):
        """Проверка корректности работы магического метода __str__"""

        channel = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel.__str__() == 'Youtube-канал: Александр Пушной'

    def test_method_str_as_user_func(self):
        """Проверка корректности работы магического метода __str__ в виде пользовательской функции str"""

        channel = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert str(channel) == 'Youtube-канал: Александр Пушной'

    def test_method_gt_as_magical_method_true(self):
        """Проверка корректности работы магического метода __gt__ (сравнение на больше).
        Проверка на значение True"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')

        assert channel_1.__gt__(channel_2) is True

    def test_method_gt_as_user_func_true(self):
        """Проверка корректности работы магического метода __gt__ (сравнение на больше).
        в виде пользовательской функции '>'
        Проверка на значение True"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')
        assert (channel_1 > channel_2) is True

    def test_method_gt_as_magical_method_false(self):
        """Проверка корректности работы магического метода __gt__ (сравнение на больше).
        Проверка на значение False"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')

        assert channel_2.__gt__(channel_1) is False

    def test_method_gt_as_user_func_false(self):
        """Проверка корректности работы магического метода __gt__ (сравнение на больше)
        в виде пользовательской функции '>'.
        Проверка на значение False"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')
        assert (channel_2 > channel_1) is False

    def test_method_gt_as_magical_method_exeption(self):
        """Проверка корректности работы магического метода __gt__ (сравнение на больше).
        Проверка вывода исключения в случае, если один из переданных объектов не является экземпляром класса Channel"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')

        with pytest.raises(TypeError):
            channel_1.__gt__('Test')

    def test_method_gt_as_user_func_exeption(self):
        """Проверка корректности работы магического метода __gt__ (сравнение на больше)
        в виде пользовательской функции '>'.
        Проверка вывода исключения в случае, если один из переданных объектов не является экземпляром класса Channel"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        with pytest.raises(TypeError):
            (channel_1 > 'Test')

    def test_method_lt_as_magical_method_true(self):
        """Проверка корректности работы магического метода __lt__ (сравнение на меньше).
        Проверка на значение True"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')

        assert channel_2.__lt__(channel_1) is True

    def test_method_lt_as_user_func_true(self):
        """Проверка корректности работы магического метода __lt__ (сравнение на меньше)
        в виде пользовательской функции '>'.
        Проверка на значение True"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')
        assert (channel_2 < channel_1) is True

    def test_method_lt_as_magical_method_false(self):
        """Проверка корректности работы магического метода __lt__ (сравнение на меньше).
        Проверка на значение False"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')

        assert channel_1.__lt__(channel_2) is False

    def test_method_lt_as_user_func_false(self):
        """Проверка корректности работы магического метода __lt__ (сравнение на меньше)
        в виде пользовательской функции '>'.
        Проверка на значение False"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')
        assert (channel_1 < channel_2) is False

    def test_method_lt_as_magical_method_exeption(self):
        """Проверка корректности работы магического метода __lt__ (сравнение на меньше).
        Проверка вывода исключения в случае, если один из переданных объектов не является экземпляром класса Channel"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')

        with pytest.raises(TypeError):
            channel_1.__lt__('Test')

    def test_method_lt_as_user_func_exeption(self):
        """Проверка корректности работы магического метода __lt__ (сравнение на меньше)
        в виде пользовательской функции '>'.
        Проверка вывода исключения в случае, если один из переданных объектов не является экземпляром класса Channel"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        with pytest.raises(TypeError):
            (channel_1 < 'Test')

    def test_method_add_as_magical_method_false(self):
        """Проверка корректности работы магического метода __add__ (сложение)"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')

        assert channel_1.__add__(channel_2) == 1409920

    def test_method_add_as_user_func_false(self):
        """Проверка корректности работы магического метода __add__ (сложение)
        в виде пользовательской функции '+'"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        channel_2 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')
        assert (channel_1 + channel_2) == 1409920

    def test_method_add_as_magical_method_exeption(self):
        """Проверка корректности работы магического метода __add__ (сложение).
        Проверка вывода исключения в случае, если один из переданных объектов не является экземпляром класса Channel"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')

        with pytest.raises(TypeError):
            channel_1.__add__(10)

    def test_method_add_as_user_func_exeption(self):
        """Проверка корректности работы магического метода __add__ (сложение) в виде пользовательской функции '+'.
        Проверка вывода исключения в случае, если один из переданных объектов не является экземпляром класса Channel"""

        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        with pytest.raises(TypeError):
            (channel_1 + 10)

    def test_check_get_channel_id(self):
        """Проверка получения id канала (id) канала с помощью геттера"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel_1.id == 'UCHH3KHUqDJX_CoRbqLy1zNg'

    def test_check_title_channel(self):
        """Проверка получения название канала (title_channel) канала при инициализации"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel_1.title_channel == 'Александр Пушной'

    def test_check_description_channel(self):
        """Проверка получения описание канала (description) канала при инициализации"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel_1.description is not None

    def test_check_url_channel(self):
        """Проверка получения ссылка на канал (url_channel) канала при инициализации"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel_1.url_channel == 'https://www.youtube.com/@pushnoyru'

    def test_check_subscriber_count_channel(self):
        """Проверка получения количество подписчиков (subscriber_count) канала при инициализации"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel_1.subscriber_count == '1400000'

    def test_check_video_count_channel(self):
        """Проверка получения количество видео (video_count) канала при инициализации"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel_1.video_count == '249'

    def test_check_view_count_channel(self):
        """Проверка получения общее количество просмотров (view_count) канала при инициализации.
        Показатель динамически изменяется"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert channel_1.view_count is not None

    def test_check_repr_channel(self):
        """Проверка корректности работы метода __repr__ для класса Channel"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert repr(channel_1) == f"id канала: {channel_1.id}\n" \
                                  f"Название канала: {channel_1.title_channel}\n\n" \
                                  f"Описание канала: \n{channel_1.description}\n\n" \
                                  f"Ссылка на канал: {channel_1.url_channel}\n" \
                                  f"Количество подписчиков: {channel_1.subscriber_count}\n" \
                                  f"Количество видео: {channel_1.video_count}\n" \
                                  f"Общее количество просмотров: {channel_1.view_count}"

    def test_check_print_info_channel(self):
        """Проверка получения данных о канале функицией print_info"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert str(channel_1.print_info) is not None

    def test_check_print_info_video_by_channel(self):
        """Проверка получения данных о видео на канале функицией print_info_video_by_channel"""
        channel_1 = Channel('UCHH3KHUqDJX_CoRbqLy1zNg')
        assert str(channel_1.print_info_video_by_channel) is not None
