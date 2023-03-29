from channel import Channel
from service import Service
from video import Video
from plvdeo import PLVideo
from playlist import Playlist

if __name__ == '__main__':
    # Создание экземпляра класса
    channel1 = Channel("UCYfYQ1lmPwPdxjBpW_rMJ7w")  # Radio Tapok
    channel2 = Channel("UCHH3KHUqDJX_CoRbqLy1zNg")  # Александр Пушной
    channel3 = Channel('UCvqXOuAHAc76rtZVVE4qfJw')  # Кирилл Антонов

    video1 = Video('sZ71LP1EbgU')
    video2 = Video('jXjwWIMTugY')  # PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8
    video3 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')  # PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8

    playlist = Playlist('PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8')

    print(playlist.title)
    print(playlist.link_playlist)
    # playlist.print_info()
    print(playlist.sum_duration)

    # # Получение информации о канале из класса(__repr__)
    # print("Получение информации о канале из класса(__repr__):")
    # print()
    # print(channel1)
    #
    # # Получение названия канала
    # print()
    # print("Получение названия канала:")
    # print()
    # print(channel1.title_channel)
    #
    # # Сохранение сведений о канале в файл json
    # channel1.to_json(f'{channel1.title_channel}.json')
    #
    # # Получение объекта для работы с API вне класса
    # print()
    # print("Получение объекта для работы с API вне класса:")
    # print()
    # print(Service.get_service())
    #
    # # Проверка отсутствия возможности изменения id канала
    # print()
    # # channel1.id = 'efgterhthe'
    # # print(channel1.id)
    #
    # # Проверка выполнения метода __str__
    # print()
    # print("Проверка выполнения метода __str__:")
    # print()
    # print(channel1)
    # print(channel2)
    # print()
    #
    # # Проверка выполнения метода __gt__
    # print("Проверка выполнения метода __gt__:")
    # print()
    # print(channel1, channel1.subscriber_count, " - ", channel2, channel2.subscriber_count)
    # print(channel1 > channel2)
    # print(channel2 > channel1)
    # print(channel1.__gt__(channel2))
    # print()
    #
    # print(channel1, channel1.subscriber_count, " - ", channel3, channel3.subscriber_count)
    # print(channel1 > channel3)
    # print(channel3 > channel1)
    # print(channel1.__gt__(channel3))
    # print()
    #
    # # Проверка выполнения метода __lt__
    # print("Проверка выполнения метода __lt__:")
    # print()
    # print(channel3, channel3.subscriber_count, " - ", channel2, channel2.subscriber_count)
    # print(channel3 < channel2)
    #
    # # Проверка выполнения метода __add__
    # print()
    # print("Проверка выполнения метода __add__:")
    # print()
    # print(channel2, channel2.subscriber_count, " - ", channel3, channel3.subscriber_count)
    #
    # print(channel3 + channel2)
    # print(channel2.__add__(channel3))
    # # print(channel3 + 2)
    # print()
    #
    # # print(channel2, channel2.subscriber_count, " - ", 10)
    # # print(channel2 > 10)
    #
    # # Проверка выполнения метода print_info()
    # print()
    # print("Проверка выполнения метода print_info():")
    # print()
    # channel3.print_info()
    #
    # # Проверка выполнения метода print_info_video_by_channel()
    # print()
    # print("Проверка выполнения метода print_info_video_by_channel():")
    # print()
    # channel1.print_info_video_by_channel()
    #
    # # Проверка корректности инициализации экземпляров класса Video
    # print()
    # print("Проверка корректности инициализации экземпляров класса Video:")
    # print()
    # video1.print_info()
    # print(video1.name_video)
    # print(video1.id_video)
    # print(video1.view_count)
    # print(video1.count_of_likes)
    #
    # # Проверка выполнения метода print_info() для видео
    # print()
    # print("Проверка выполнения метода print_info() для видео:")
    # print()
    # video2.print_info()
    #
    # # Проверка корректности инициализации экземпляров класса PLVideo
    # print()
    # print("Проверка корректности инициализации экземпляров класса PLVideo:")
    # print()
    # print(video3.id_video)
    # print(video3.name_video)
    # print(video3.view_count)
    # print(video3.count_of_likes)
    # print(video3.playlist_name)
    #
    # # Проверка выполнения метода print_info() для плейлиста
    # print()
    # print("Проверка выполнения метода print_info() для плейлиста:")
    # print()
    # video3.print_info()
    #
    # # Проверка выполнения метода __str__ для видео
    # print()
    # print("Проверка выполнения метода __str__ для видео:")
    # print()
    # print(video1)
    #
    # # Проверка выполнения метода __str__ для плейлиста
    # print()
    # print("Проверка выполнения метода __str__ для плейлиста:")
    # print()
    # print(video3)
    #
    # # Проверка выполнения метода __repr__ для плейлиста
    # print()
    # print("Проверка выполнения метода __repr__ для плейлиста:")
    # print()
    # print(repr(video3))
    #
    # # Проверка инициализации экземпляра класса Service
    # print()
    # print("Проверка инициализации экземпляра класса Service")
    # service = Service()
    # print(service)
    #
    # # Проверка работы метода get_service() класса Service
    # print()
    # print(service.get_service())
