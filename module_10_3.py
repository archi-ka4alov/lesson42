import threading
import random
import time

lock = threading.Lock()


class Bank:
    def __init__(self):
        self.balance = 0


    def deposit(self):
        lock.acquire()
        for i in range(100):
            dep_amount = random.randint(50, 500)
            self.balance += dep_amount
            print(f'Пополнение: {dep_amount}. Баланс: {self.balance}')

            if self.balance >= 500 and lock.locked():
                lock.release()

            time.sleep(0.001)


    def take(self):
        for y in range(100):
            take_amount = random.randint(50, 500)
            print(f'Запрос на {take_amount}')
            if take_amount <= self.balance:
                self.balance -= take_amount
                print(f'Снятие: {take_amount}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')