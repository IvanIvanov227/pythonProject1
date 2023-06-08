x = int(input())
y = int(input())
lis = [lambda a, b: a * b, lambda a, b: (a + b) * 2]
print('0' + ' ' + str(lis[0](x, y)))
print('1' + ' ' + str(lis[1](x, y)))
print([lis[0](x, y), lis[1](x, y)])
print(str(lis[0](x, y)) + ' ' + str(lis[1](x, y)))
