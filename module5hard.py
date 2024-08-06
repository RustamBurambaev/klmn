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
        self.duration = []
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
        self.videos = []




