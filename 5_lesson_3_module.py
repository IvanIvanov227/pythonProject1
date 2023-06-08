import time


class RunningCode:
    def __init__(self):
        self.start = None

    def __enter__(self):
        """Создание контекста"""
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Остановка и очищение контекста"""
        res = time.time() - self.start
        print(f'Время выполнения кода: {res} секунд.')
        if exc_type == TypeError:
            return True

    def hi(self):
        print('Привет')


with RunningCode() as rc:
    rc.hi()
    my_list = [x for x in range(10000)]
    print(rc)

# my_list = [1, 2, 3, 4, 5]
# iter_list = iter(my_list)
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))



import random


class RandomIter:
    def __init__(self, limit):
        self.__reload = limit

    def __iter__(self):
        self.limit = self.__reload
        return self

    def __next__(self):
        if self.limit:
            self.limit -= 1
            return random.randint(1, 1000)
        else:
            raise StopIteration


# rand = RandomIter(10)
# for i in rand:
#     print(i)
# rand.__iter__()
# print()
# for i in rand:
#     print(i)

# class FibClass:
#
#     def __init__(self, number):
#         self.__reload = number
#
#     def __iter__(self):
#         self.number = self.__reload
#         self.cur_val = 0
#         self.next_val = 1
#         return self
#
#     def __next__(self):
#         if self.number:
#             t = self.next_val
#             self.next_val += self.cur_val
#             self.cur_val = t
#             self.number -= 1
#             return self.cur_val
#         else:
#             raise StopIteration
#
#
# a = FibClass(20)
# for i in a:
#     print(i)