# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season
#
#     def get_days(self):
#         return self.__days
#
#     def get_season(self):
#         return self.__season
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#
#     def set_season(self, season):
#         self.__season = season
#
#
# year = Year(365, 'Зима')
# print(year.get_days())
# print(year.set_days(300))


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self):
        return self.__age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError('Вы ещё не родились')
        self.__age = age


person = Person('Александр', 0)
person.age -= 1
print(person.age)


# class Alist:
#     def __init__(self, alist):
#         self.__reload = alist
#
#     def __iter__(self):
#         self.alist = self.__reload
#         return self.alist
#
#     def __next__(self):
#         if self.alist:
#             x = self.alist[0]
#             del self.alist[0]
#             return self.alist
#
#         else:
#             raise StopIteration
#
#     def delete_last_item(self):
#         del self.alist[-1]
#
#
#
# for i in Alist([1, 2, 3, 4, 5]):
#     print(i)


class MyClass(list):
    def delete_last_item(self):
        self.remove(self[-1])


a = MyClass([1, 2, 3, 4, 5])
print(a)
a.delete_last_item()
print(a)