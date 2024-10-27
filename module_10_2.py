import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        number_of_enemies = 100
        number_of_day = 0
        print(f'{self.name}, на нас напали!')
        while number_of_enemies:
            time.sleep(1)
            number_of_enemies -= self.power
            number_of_day += 1
            print(f'{self.name} сражается {number_of_day} дней(дня), осталось {number_of_enemies} воинов')

        print(f'{self.name} одержал победу спустя {number_of_day} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()