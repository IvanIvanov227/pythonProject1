# # Первый вариант записи
# def func1(a):
#     return a * a
#
# # Lambda - анонимна однострочная функция
# # Второй вариант записи
# func2 = lambda a: a * a
#
#
# print(func1(3))
# print(func2(3))
#
# # filter
# goods = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(filter(lambda i: i < 5, goods))
# # Равен
#
# def func(item):
#     if item < 5: return True
# print(filter(func, goods))


goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200,
    },
    {
        'name': 'Samsung Galaxy A53',
        'brand': 'Samsung',
        'price': 500,
    },
    {
        'name': 'REALME C25s',
        'brand': 'REALME',
        'price': 400,
    },
    {
        'name': 'OnePlus 9rt',
        'brand': 'OnePlus',
        'price': 550,
    }
]
# После массива обязательно должен быть именованный аргумент

from pprint import pprint # Для красивого вывода последовательности
pprint(sorted(goods, key=lambda item: item['price']))
pprint(list(filter(lambda item: item.get('brand') == 'Apple', goods)))
def f(item):
    item['price'] *= 0.85
    return item
pprint(list(map(f, goods)))

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
for i in zip(list_1, list_2, [True, False]):
    print(i)

# Точка входа
# Выполняется, если этот код должен выполняться первым
if __name__ == '__main__':
    print(__name__)
