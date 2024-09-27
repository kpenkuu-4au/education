class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, self.number_of_floors + 1):
            if new_floor > self.number_of_floors:
                print("Такого этажа не существует")
                break
            elif new_floor < 1:
                print("Такого этажа не существует")
                break
            elif i > new_floor:
                break
            else:
                print(i)
                i += 1
                continue


h1 = House('ЖК Эльбрус', 30)
h2 = House('Дача', 1)
h3 = House('ЖК Новый', 13)
h1.go_to(5)
h2.go_to(3)
h3.go_to(0)
