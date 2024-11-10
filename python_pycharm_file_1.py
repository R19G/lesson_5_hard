import time

class User:

    def __init__(self, nickname, password, age):
        # Осуществляется проверка на то, чтобы в nickname была передана строка
        if isinstance(nickname, str):
            self.nickname = nickname
        else:
            print('Попробуйте снова.')
        # Осуществляется проверка на то, чтобы в password была передана строка
        if isinstance(password, str):
            self.password = hash(password)
        else:
            print('Попробуйте снова.')
        # Осуществлется проверка на то, чтобы в age было передано число
        if isinstance(age, int):
            self.age = age
        else:
            print('Попробуйте снова.')


class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        # Осуществляется проверка на то, чтобы в title была передана строка
        if isinstance(title, str):
            self.title = title
        else:
            print('Попробуйте снова.')
        # Осуществляется проверка на то, чтобы в duration было передано число
        if isinstance(duration, int):
            self.duration = duration
        else:
            print('Попробуйте снова.')
        # Осуществляется проверка на то, чтобы в time_now было передано число
        if isinstance(time_now, int):
            self.time_now = time_now
        else:
            print('Попробуйте снова.')
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        # Создаем базу данных для пользователей, видео и создаем текущего пользователя
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        self.password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        return self.current_user

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = hash(password)
        for user in self.users:
            if user.nickname == self.nickname and user.password == self.password:
                self.current_user = user

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
        return self.videos

    def get_videos(self, expression):
        list_of_movies = []
        if isinstance(expression, str):
            self.expression = expression
        for movie in self.videos:
            if expression.upper() in movie.title.upper():
                list_of_movies.append(movie.title)
        return list_of_movies

    def watch_video(self, name_of_movie):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео.')

        for i in self.videos:
            if i.title == name_of_movie:
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')

                for j in range(1, i.duration + 1):
                    print(j, end=' ')
                    i.time_now += 1
                i.time_now = 0
                print('Конец видео')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    # ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')