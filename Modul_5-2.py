class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
h1 = House('ЖК "Приморье"', 11)
h2 = House('Васильково', 7)
# название и кол-во этажей (str)
print(h1)
print(h2)
# кол-во этажей (int)
print(len(h1))
print(len(h2))