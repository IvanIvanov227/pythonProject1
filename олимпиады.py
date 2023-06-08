# sum = 0
# for i in range(10, 100):
#     if i / int(str(i)[:-1]) == 13.0:
#         sum += 1
#         print(i)
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return n * func(n - 1)
# print(func(25))
# # 155112100433309__5984000000
# # 15511210043330985984000000
a = []
i = 0
while len(a) < 10:
    s = 0
    for x in range(2, i):
        if i % x:
            s += 1
    if s == i - 2:
        a.append(i)
    i += 1
n = ''
for i in a:
    n += str(i)
n = int(n)
max = 0
import random
for i in range(10000):
    for i in range(16):
        del a[random.randint(0, 16)]
    f =
