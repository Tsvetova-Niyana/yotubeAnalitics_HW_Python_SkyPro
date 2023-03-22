from channel import Channel

if __name__ == '__main__':
    # Создание экземпляра класса
    channel1 = Channel("UCYfYQ1lmPwPdxjBpW_rMJ7w")  # Radio Tapok
    channel2 = Channel("UCHH3KHUqDJX_CoRbqLy1zNg")  # Александр Пушной
    channel3 = Channel('UCvqXOuAHAc76rtZVVE4qfJw') # Кирилл Антонов

    # Получение информации о канале
    channel1.print_info()

    # Получение информации о канале из класса(__repr__)
    print()
    print(channel1)

    # Получение названия канала
    print()
    print(channel1.title_channel)

    # Сохранение сведений о канале в файл json
    channel1.to_json(f'{channel1.title_channel}.json')

    # Получение объекта для работы с API вне класса
    print()
    print(Channel.get_service())

    # Проверка отсутствия возможности изменения id канала
    # print()
    # channel1.id = 'efgterhthe'
    # print(channel1.id)

    # Проверка выполнения метода __str__
    print()
    print(channel1)
    print(channel2)
    print()

    print(channel1, channel1.subscriber_count, " - ", channel2, channel2.subscriber_count)
    print(channel1 > channel2)
    print(channel2 > channel1)
    print(channel1.__gt__(channel2))
    print()

    print(channel1, channel1.subscriber_count, " - ", channel3, channel3.subscriber_count)
    print(channel1 > channel3)
    print(channel3 > channel1)
    print(channel1.__gt__(channel3))
    print()

    print(channel3, channel3.subscriber_count, " - ", channel2, channel2.subscriber_count)
    print(channel3 < channel2)

    print(channel2, channel2.subscriber_count, " - ", channel3, channel3.subscriber_count)

    print(channel3 + channel2)
    print(channel2.__add__(channel3))
    # print(channel3 + 2)
    print()

    #
    # print(channel2, channel2.subscriber_count, " - ", 10)
    # print(channel2 > 10)

    # channel3.print_info()
