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
