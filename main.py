from channel import Channel
from service import Service
from video import Video
from plvdeo import PLVideo

if __name__ == '__main__':
    # Создание экземпляра класса
    channel1 = Channel("UCYfYQ1lmPwPdxjBpW_rMJ7w")  # Radio Tapok
    channel2 = Channel("UCHH3KHUqDJX_CoRbqLy1zNg")  # Александр Пушной
    channel3 = Channel('UCvqXOuAHAc76rtZVVE4qfJw') # Кирилл Антонов


    video1 = Video('sZ71LP1EbgU')
    video2 = Video('jXjwWIMTugY') # PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8
    video3 = PLVideo('jXjwWIMTugY', 'PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8') # PLPOCJi2SznkrxxjSUC3Drb-cAL3wcUKD8

    print(video2.name_video)
    print(video2.view_count)
    print(video2.count_of_likes)

