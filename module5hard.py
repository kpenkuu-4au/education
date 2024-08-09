import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname

    def get_info(self):
        return self.nickname, self.password


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.videos = []

    def log_in(self, nickname, password):
        for i in self.users:
            if (nickname, hash(password)) == i.get_info():
                self.current_user = i
                return self.current_user
            else:
                print('Неверное имя пользователя или пароль')

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user)
            self.current_user = user


    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for i in other:
            if i.title in self.videos and isinstance(i, Video):
                continue
            else:
                self.videos.append(i)

    def get_videos(self, find):
        findlist = []
        for i in self.videos:
            if find.lower() in str(i).lower():
                findlist.append(str(i))
                continue
        return findlist

    def watch_video(self, name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for play in self.videos:
            if name == play.title:
                if play.adult_mode is True and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    while play.time_now <= play.duration:
                        print(play.time_now)
                        time.sleep(1)
                        play.time_now += 1
                        continue
                    print("Конец видео")
                    play.time_now = 0
                    return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')
