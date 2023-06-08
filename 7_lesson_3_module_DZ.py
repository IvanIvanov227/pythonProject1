# Первое задание

# class Item:
#     """Товар"""
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     # Сложение
#     def __add__(self, other):
#         # Проверяет принадлежность объекта к классу
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int) or isinstance(other, str):
#             return self.price + other
#
#     # Вычитание
#     def __sub__(self, other):
#         if isinstance(other, Item):
#             return self.price - other.price
#         elif isinstance(other, int):
#             return self.price - other
#
#     # Умножение
#     def __mul__(self, other):
#         if isinstance(other, Item):
#             # Цена за вес
#             return self.price * self.weight + other.weight * other.price
#         elif isinstance(other, int):
#             return self.price * other
#
#     # Целочисленное деление
#     def __floordiv__(self, other):
#         if isinstance(other, Item):
#             return self.price // other.price
#         elif isinstance(other, int):
#             return self.price // other
#
#     # Остаток от деления
#     def __mod__(self, other):
#         if isinstance(other, Item):
#             return self.price % other.price
#         elif isinstance(other, int):
#             return self.price % other
#
#     # Обычное деление
#     def __truediv__(self, other):
#         if isinstance(other, Item):
#             return self.price / self.weight + other.price / other.weight
#         elif isinstance(other, int):
#             return self.price / other
#
#
# item1 = Item('Видеокарта', 15_000, 0.8)
# item2 = Item('Процессор', 12_000, 0.3)
# item3 = Item('Яблоко', 100, 1)
# item4 = Item('Лопата', 500, 5)
#
# price1 = item1 / item2
# price2 = item3 * item4
# price3 = (item3 + item1) / 1000
# price4 = item4 - item4 + 100
# print(price1)
# print(price2)
# print(price3)
# print(price4)



# Второе задание
from tkinter import *
import random
window = Tk()
window.geometry('600x600')


class Fire:
    """Огонь"""
    # Уменьшает изображение по x и y в четыре раза
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\free-icon-fire-9509865.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay

        elif isinstance(other, Water):
            return Steam
        elif isinstance(other, Wind):
            return Fire_Wind


class Water:
    """Вода"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\free-icon-water-drop-4246703.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam
        elif isinstance(other, Earth):
            return Wet_ground


class Wind:
    """Воздух"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust
        elif isinstance(other, Fire):
            return Fire_Wind


class Earth:
    """Земля"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

        elif isinstance(other, Wind):
            return Dust

        elif isinstance(other, Water):
            return Wet_ground


class Clay:
    """Горшок"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\free-icon-pottery-7942410.png').subsample(4, 4)

    def __add__(self, other):
        pass


class Dust:
    """Пыль"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\free-icon-dust-2396941.png').subsample(4, 4)

    def __add__(self, other):
        pass


class Steam:
    """Пар"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\aroma.png').subsample(4, 4)

    def __add__(self, other):
        pass


class Fire_Wind:
    """Огненный ветер"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\fire_wind.png').subsample(4, 4)

    def __add__(self, other):
        pass


class Wet_ground:
    """Мокрая земля"""
    image = PhotoImage(file=r'C:\Users\sivko\OneDrive\Рабочий стол\Урок\\wet_ground.png').subsample(4, 4)

    def __add__(self, other):
        pass


def move(event):
    """Вызывается при нажатии мышки"""
    # Метод, который возвращает id объектов в определённом периметре
    images_id = canvas.find_overlapping(event.x, event.y, event.x+3, event.y+3)
    if len(images_id) == 2:
        elem_id1, elem_id2 = images_id
        element_1 = elements[elem_id1 - 1]
        element_2 = elements[elem_id2 - 1]

        # Сложение классов
        new_element = element_1 + element_2
        # Если каждый из элементов не равен None (то-есть есть в списке)
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                images_id = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
                elements.append(new_element)
    # Меняем координаты рисунка
    canvas.coords(images_id, event.x, event.y)


canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Earth(), Fire(), Water(), Wind()]
y1 = 50
y2 = 100
x1 = 50
x2 = 500
for i in elements:
    canvas.create_image(random.randint(x1, x2), random.randint(y1, y2), image=i.image)
    y1 += 120
    y2 += 120

# Отслеживает нажатия мышкой
# обозначение мышки,
window.bind('<B1-Motion>', move)
window.mainloop()
