import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __hash__(self):
        return self.password

class Video:
    def __init__(self, title, duration, time_now, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = hash(password)

        for i in self.users:
            if i[0] == self.nickname and i[1] == self.password:
                self.current_user = self.nickname
                self.veryfy_user = 1
            elif i[0] == self.nickname and i[1] != self.password:
                self.veryfy_user = 2
        return self.veryfy_user


    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.veryfy_user = 0
        for i in self.users:
            if i[0] == self.nickname:
                self.log_in(self.nickname, self.password)
        if self.veryfy_user == 0:
            self.users.append(self.users)
            self.log_in(self.nickname, self.password)
        elif self.veryfy_user == 2:
            print(f'Пользователь {nickname} уже существует')


    def lof_out(self,nickname, password, age, current_user):
        self.current_user = None
        self.nickname = ''
        self.password = hash('')
        self.age = 0
        return

    def __add__(self, *args):
        for video in args:
            if video.title not in self.videos:
                self.videos.append(video.title)

    def get_videos(self, search_video):
        self.search_videos = search_video.lower()
        self.my_search_list = []
        for i in self.videos:
            my_str = i [0]
            self.my_str = my_str.lower()
            if self.my_str.find(self.search_video) != -1:
                self.my_search_list.append(i[0])
        return self.my_search_list

    def watch_video(self, get_video):
        self.get_video = get_video
        if self.current_user != None:
            for i in self.videos:
                if i[0] == self.get_video and i[3] == True:
                    self.current_duration = i[1]
                    self.current_time_now = i[2]

                    if self.age > 18:
                        print(f'\033[34m Воспроизводится: {self.get_video}\033[0m')
                        for j in range(self.current_duration):
                            self.current_time_now = j
                            print('\033[35m * \033[0m', end='')
                            print(self.current_time_now, sep='', end='')
                            time.sleep(2)
                    else:
                        print('\033[31m Вам нет 18, пожалуйста покиньте страницу \033[0m')
                        self.lof_out()
            else:
                print('\033[31m Войдите в аккаунт что бы смотреть видео \033[0m')


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