from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy_count = 100
        day_count = 0
        for enemy in range(enemy_count):
            if 0 < enemy_count:
                enemy_count = enemy_count - self.power
                day_count += 1
                print(f'{self.name} сражается {day_count} день, осталось {enemy_count} воинов.')
                sleep(1)
            elif enemy_count <= 0:
                print(f'{self.name} одержал победу спустя {day_count} дней!')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

knight_list = [first_knight, second_knight]
battle_list = []
for battle in knight_list:
    battle.start()
    battle_list.append(battle)
for stats in range(len(battle_list)):
    battle_list[stats].join()
    if stats == len(battle_list) - 1:
        print('Все битвы закончились!')


