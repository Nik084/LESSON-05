class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor < self.number_of_floors:
            for i in range(new_floor):
                print (i+1)
        else:
                print ('Такого этажа не существует')
h1 = House('Nevskiy', 11)
h2 = House('Village', 3)
h1.go_to(7)
h2.go_to(7)
