
class person():

    def __init__(self, name):
        self.name = name


class Bus():

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passenger_list = []


    def add_passenger(self, person):
        if len(self.passenger_list) <= self.max_passengers-1:
            self.passenger_list.append(person)
            print(f"{person.name} got on the bus")
        else:
            print(f" The bus is full. {person.name} couldn't get on !")

    def remove_passenger(self, person):
        if person in self.passenger_list:
            self.passenger_list.remove(person)
            print(f"{person.name} got off the Bus!")
        else:
            print(f"-> {person.name} is not on the Bus!")


person1 = person("Andrea")
person2 = person("Carlos")
person3 = person("Diego")
person4 = person("Ana")

my_bus = Bus(3)

my_bus.add_passenger(person1)
my_bus.add_passenger(person2)
my_bus.add_passenger(person3)
my_bus.add_passenger(person4)

my_bus.remove_passenger(person3)

my_bus.add_passenger(person4)



