# class LocalStorage:
#     pass

#name = 'Ivan'
#age = '12'

# def get_name():
#     pass

class Fruit:
    name: str = ''
    country: str = ''
    color: str = None
    # pass

    def get_info(self):
        print(self.name, self.color, self.country)
        # print("Hello")


fruit_1 = Fruit()
Fruit_2 = Fruit()
fruit_1.name = 'Apple' # экземпяры объекта
fruit_1.color = 'Green'
fruit_1.country = 'Russia'
Fruit_2.name = 'Banana'
Fruit_2.color = 'Yellow'
Fruit_2.country = 'Russia'

# print(id(fruit_1), fruit_1.name, fruit_1.color, fruit_1.country)
# print(id(Fruit_2), Fruit_2.name, Fruit_2.color, Fruit_2.country)
fruit_1.get_info()
Fruit_2.get_info()

# print(fruit_1)
# print(Fruit_2) # справа адрес памяти
# print(fruit_1 == Fruit_2) # они не равны
