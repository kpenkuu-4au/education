from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        prod = open(self.__file_name, 'r')
        readprod = str(prod.read())
        prod.close()
        return readprod

    def add(self, *products: Product):
        for product in range(len(products)):
            prod = open(self.__file_name, 'r')
            prod2 = open(self.__file_name, 'a')
            if products[product].name in prod.read():
                print(f'Продукт {products[product].name} уже есть в магазине')
                continue
            else:
                prod2.write(f'{str(products[product])}\n')
            prod.close()
            prod2.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
