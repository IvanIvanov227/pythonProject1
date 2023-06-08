# Первое задание
# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         """Магический метод класса, который возвращает определённое значение при отображении экземпляра класса"""
#         return self.brand
#
#
# item_list = [
#     Item(1000, 'Apple'),
#     Item(1200, 'Apple'),
#     Item(900, 'Samsung'),
#     Item(700, 'Samsung'),
#     Item(660, 'Xioami')
# ]
# print([i for i in item_list if i.brand == 'Apple'])


# Второе задание
names_list = ['данил', 'артём', 'никита', 'влад']
print(list(map(lambda i: i.capitalize(), names_list)))