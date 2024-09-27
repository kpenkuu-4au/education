class Vehicle:
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.model = str(__model)
        self.engine_power = int(__engine_power)
        self.color = str(__color)
        self.__COLOR_VARIANTS = ['red', 'white', 'black']

    def get_owner(self):
        print(f'Владелец: {self.owner}')

    def get_model(self):
        print(f"Модель {self.model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.engine_power}")

    def get_color(self):
        print(f"Цвет: {self.color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        self.get_owner()

    def set_color(self, new_color):
        i = 0
        while i < len(self.__COLOR_VARIANTS):
            if new_color.lower() != self.__COLOR_VARIANTS[i].lower():
                i += 1
                if i == len(self.__COLOR_VARIANTS):
                    print(f"Нельзя сменить цвет на {new_color}")
            else:
                self.color = new_color
                break


class Sedan(Vehicle):
    def __new__(cls, *args, **kwargs):
        __PASSENGERS_LIMIT = 5
        return super().__new__(cls)


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
