from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe(Table):

    def __init__(self, *tables: Table, number=None):
        super().__init__(number)
        self.tables = tables
        self.next = Queue()

    def guest_arrival(self, *guests: Guest):
        for guest_ in range(len(guests)):
            for table in range(len(self.tables)):
                if guest_ == self.tables[table].number - 1 and self.tables[table].guest is None:
                    self.tables[table].guest = guests[guest_]
                    guests[guest_].start()
                    print(f'Гость {guests[guest_].name} сел за стол №{self.tables[table].number}')
                    break
                elif guest_ > table and len(self.tables) == table + 1:
                    self.next.put(guests[guest_])
                    print(f'Гость {guests[guest_].name} в очереди')
                    break
                else:
                    continue

    def discuss_guests(self):
        while self.next.empty() is False:
            for table in range(len(self.tables)):
                if self.tables[table].guest is not None:
                    self.tables[table].guest.join()
                    print(f'Гость {self.tables[table].guest.name} закончил прием пищи и ушел')
                    self.tables[table].guest = None
                    print(f'Стол №{self.tables[table].number} освободился')
                    if self.next.empty() is False:
                        self.tables[table].guest = self.next.get()
                        self.tables[table].guest.start()
                        print(f'Гость {self.tables[table].guest.name} вышел '
                              f'из очереди и сел за стол №{self.tables[table].number}')
                    else:
                        continue
                elif self.tables[table].guest is None:
                    continue
        for table in range(len(self.tables)):
            if self.tables[table].guest is not None:
                self.tables[table].guest.join()
                print(f'Гость {self.tables[table].guest.name} закончил прием пищи и ушел')
                self.tables[table].guest = None
                print(f'Стол №{self.tables[table].number} освободился')


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
