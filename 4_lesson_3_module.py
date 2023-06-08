import time


# def lazy_func():
#     for i in range(10):
#         yield i
#
#
# start = time.time()
# for x in lazy_func():
#     print(x)
# stop = time.time()
# print(stop - start)
# start = time.time()
# a = (time.sleep(1) for x in 'ab')
# stop = time.time()
# print(stop - start)
# for i in a:
#     i
import contextlib


# @contextlib.contextmanager
# def reverse_str(str):
#     print('Входим в контекстный менеджер')
#     yield str[::-1]
#     print('Выходим из контекстного менеджера')
#
#
# with reverse_str('Hello, world!') as new_str:
#     print(f'Выполняется код основного блока {new_str}')

@contextlib.contextmanager
def exc_handler(exc):
    try:
        print('до yield')
        yield True
        print('после yield')
    except exc:
        print('Ошибка')


with exc_handler(IndexError):
    print('Начало программы')
    print('Создаём список')
    my = [1, 2]
    print('Обращаемся к элементу')
    print(my[1])
    print('Всё хорошо')
#
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs.get('text', 'Такого ключа нет'))
# func(1, 2, 3, a=4, b=5, c=6)