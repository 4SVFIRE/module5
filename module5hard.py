from typing import List, Optional
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __str__(self):
        return self.nickname


class Video:
    # конструктор - вызывается, когда создается объект
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
class UrTube:
    def __init__(self):
        self.users:List[User] = []
        self.videos:List[Video] = []
        self.current_user:Optional[User] = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print('Успешный вход!')
                return None
        print('Пользователь не найден')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print('Такой пользователь существует!')
                return None
        new_user = User(nickname, password, age )
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован')

    def log_out(self):
        self.current_user = None
        print('Вы вышли')

    def add(self, *videos:Video):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f'Видео с название {video.title} добавлено ')

    def watch_video(self, title_video:str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return None
        found_videos = []
        # !!!!!!!!!!!!!!!!!!!!!!!!
        for video in self.videos:
            if video.title == title_video:
                found_videos.append(video)
        if not found_videos:
            print('Ничего не найдено')
            return
        for video in found_videos:
            if video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
        while video.time_now < video.duration:
            video.time_now += 1
            print(video.time_now)
            time.sleep(1)
        print('Конец видео')
        video.time_now = 0

    def get_videos(self, search_word:str):
        search_word = search_word.lower()
        found_videos = []
        for video in self.videos:
            if search_word in video.title.lower():
                found_videos.append(video.title)
        return found_videos




# ur = UrTube()
# ur.register('fire', 1234, 20)
# ur.log_in('fire', 1234)
# print(f'Active is user on the net is {ur.current_user}')
# v1 = Video('Лучший язык программирования 2024 года', 20)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# ur.add(v1, v2, v1)
# print(ur.videos)
# ur.watch_video(v1.title)
# ur.watch_video(v1.title)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')