from time import sleep
from random import randint
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for operation in range(100):
            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()
                money = randint(50, 500)
                self.balance += money
                sleep(0.001)
                print(f'Пополнение: {money}. Баланс: {self.balance}')
            elif self.balance >= 500 and self.lock.locked() is False:
                money = randint(50, 500)
                self.balance += money
                sleep(0.001)
                print(f'Пополнение: {money}. Баланс: {self.balance}')
            elif self.balance < 500 and self.lock.locked() is True:
                self.lock.release()
                money = randint(50, 500)
                self.balance += money
                sleep(0.001)
                print(f'Пополнение: {money}. Баланс: {self.balance}')
            elif self.balance < 500 and self.lock.locked() is False:
                money = randint(50, 500)
                self.balance += money
                sleep(0.001)
                print(f'Пополнение: {money}. Баланс: {self.balance}')

    def take(self):
        for operation in range(100):
            money = randint(50, 500)
            print(f'Запрос на {money}')
            if self.balance >= money and self.lock.locked() is True:
                self.lock.release()
                self.balance -= money
                sleep(0.001)
                print(f'Снятие: {money}. Баланс: {self.balance}')
            elif self.balance >= money and self.lock.locked() is False:
                self.balance -= money
                sleep(0.001)
                print(f'Снятие: {money}. Баланс: {self.balance}')
            elif self.balance < money and self.lock.locked() is False:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            elif self.balance < money and self.lock.locked() is True:
                print('Запрос отклонён, недостаточно средств')


bk = Bank()
print(f'Начальный баланс: {bk.balance}')
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
