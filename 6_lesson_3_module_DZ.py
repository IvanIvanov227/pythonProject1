# ПЕРВОЕ ЗАДАНИЕ
# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#
#     @property
#     def season(self):
#         return self.__season
#
#     @season.setter
#     def season(self, season):
#         self.__season = season
#
#
# year = Year(200, 'summer')
# year.days = 366
# print(year.days)



# # ВТОРОЕ ЗАДАНИЕ
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        print('Теперь вы без имени')
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError('Вы ещё не родились')
        self.__age = age

    @age.deleter
    def age(self):
        print('Обнуляем ваш возраст!!!')
        self.__age = 0


person = Person('Александр', 0)
person.age = 5
person.name = 'Иван'
del person.age
del person.name
print(f'Текущий возраст: {person.age}')
print(f'Текущее имя: {person.name}')

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return f"{self.first}.{self.last}@beget.com"
#
#     @property
#     def fullname(self):
#         return f"{self.first} {self.last}"
#
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print("Delete Name!")
#         self.first = None
#         self.last = None
#
# emp_1 = Employee("Ivan", "Petrov")
#
# # Change the attribute
#
# emp_1.fullname = "Andrei Olegovich"
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
#
# del emp_1.fullname
#
# print(emp_1.fullname)