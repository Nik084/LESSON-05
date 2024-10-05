class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        # return self.__lt__(other) or self.__eq__(other)
    def __gt__(self, other):
        return not self.__lt__(other)
    def __ge__(self, other):
        return not self.__le__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
h1 = House('ЖК "Приморье"', 8)
h2 = House('Васильково', 18)
print(h1)
print(h2)
print('количество этажей в домах одинаковое -', h1 == h2)
print('в первом доме этажей <, чем во втором -', h1 < h2)
print('в первом доме этажей <=, чем во втором -', h1 <= h2)
print('в первом доме этажей >, чем во втором -', h1 > h2)
print('в первом доме этажей >=, чем во втором -', h1 >= h2)
print('количество этажей в домах различно -', h1 != h2)
print('количество этажей в домах одинаковое -', h1 == h2)
h1 = h1 + 10 # __add__
print(h1)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print('количество этажей в домах одинаковое -', h1 == h2)

