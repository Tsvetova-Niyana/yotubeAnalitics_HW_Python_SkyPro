from channel import Channel

if __name__ == '__main__':
    # Создание экземпляра класса
    channel1 = Channel("UCYfYQ1lmPwPdxjBpW_rMJ7w")

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

    print()
    print(channel1)


