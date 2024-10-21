import inspect


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 30)


def introspection_info(obj):
    type_ = str(type(obj)).split("'")[1]
    method_ = [method for method in dir(obj) if callable(getattr(obj, method))]
    if isinstance(obj, (int, float, str, list, tuple, dict)):
        module_ = str(inspect.getmodule(type(obj))).split("'")[1]
        return {'type': type_, 'attributes': dir(obj), 'methods': method_, 'module': module_}
    else:
        module_ = str(inspect.getmodule(obj)).split("'")[1]
        return {'type': type_, 'attributes': dir(obj), 'methods': method_, 'module': module_}


number_info = introspection_info(h1)
print(number_info)
