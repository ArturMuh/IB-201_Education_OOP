# SOLID - это аббреавиатура 5 символов принцип

# принцип единственной ответственности
class TelephoneDirectory:
    def __init__(self):
        self.telephone_directory = dict()

    def add_entry(self, name, number):
        self.telephone_directory[name] = number

    def delete_entry(self, name):
        del self.telephone_directory[name]

    def update_entry(self, name, number):
        self.telephone_directory[name] = number

    def lookup_number(self, name):
        return self.telephone_directory.get(name)

    def __str__(self):
        ret_dct = ''
        for key, value in self.telephone_directory.items():
            ret_dct += f'{key} : {value}\n'
        return ret_dct

phone_book = TelephoneDirectory()
phone_book.add_entry('Ravi', 123456)
phone_book.add_entry('Vikas', 67890)
print(phone_book)

phone_book.delete_entry('Ravi')
phone_book.add_entry('Ravi', 123456)
phone_book.update_entry('Vikas', 776589)
print(phone_book.lookup_number('Vikas'))
print(phone_book)

# библиотеки абстрактный метод
# Принцип открытости/закрытости

from abc import ABCMeta, abstractmethod

class DiscountCalculator():

    @abstractmethod
    def get_discounted_price(self):
        pass

class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.10)

class DiscountCalculatorTshirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.15)

class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.25)


dc_shirt = DiscountCalculatorShirt(100)
print(dc_shirt.get_discounted_price())

dc_tshirt = DiscountCalculatorTshirt(100)
print(dc_tshirt.get_discounted_price())

dc_pant = DiscountCalculatorPant(100)
print(dc_pant.get_discounted_price())

# Принцип подстановки Барбары Лисков

# Сложный принцип это

# class Car():
#     def __init__(self, type):
#         self.type = type
#
# class PetrolCar(Car):
#     def __init__(self, type):
#         self.type = type
#
#
# car = Car("SUV")
# car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}
#
# petrol_car = PetrolCar("Sedan")
# petrol_car.properties = ("Blue", "Manual", 4)
#
# cars = [car, petrol_car]
#
# def find_red_cars(cars):
# red_cars = 0
# for car in cars:
#     if car.properties['Color'] == "Red":
#         red_cars += 1
# print(f'Number of Red Cars = {red_cars}')

find_red_cars(cars)

# Принцип разделения интерфейсов

# Принцип инверсии зависимостей

from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
    BLUE_TEAM = 1
    RED_TEAM = 2
    GREEN_TEAM = 3


class TeamMembershipLookup():
    @abstractmethod
    def find_all_students_of_team(self, team):
        pass

class Student:
    def __init__(self, name):
        self.name = name

class TeamMemberships(TeamMembershipLookup):
    def __init__(self):
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students_of_team(self, team):
        for members in self.team_memberships:
            if members[1] == team:
                yield members[0].name

class Analysis():
    def __init__(self, team_membership_lookup):
        for student in team_membership_lookup.find_all_students_of_team(Teams.RED_TEAM):
            print(f'{student} is in RED team.')


student1 = Student('Ravi')
student2 = Student('Archie')
student3 = Student('James')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)