# import sys
# import os
# # # Операционная система
# # print(sys.platform)
# # # Версия операционной системы
# # print(sys.version)
# # folder = os.getcwd()
# # print(folder)
# # print(os.listdir(folder))
# # # Заходим в папку 'c:\\'
# # os.chdir('c:\\')
# # # Смотрим, где мы сейчас находимся
# # print(os.getcwd())
# # # Создаём папку '4video3 и заходим в неё'
# # os.mkdir('4video3')
# # os.chdir('4video3')
# # print(os.getcwd())
#
#
# # Рекурсивная функция
# # получает папку (директорию)
# def f1(dir):
#     # Просматриваем каждый объект папки
#     for name in os.listdir(dir):
#         # Создаёт правильный путь к папке (в join засовываем папку и имя файла, с которым работаем, path работает с путями)
#         # Проще говоря, формирует путь
#         path = os.path.join(dir, name)
#         # Если этот путь является файлом
#         if os.path.isfile(path):
#             # Выводим путь
#             print(path)
#         # Если папка
#         else:
#             f1(path)
#
# # Засовываем в функцию текущую папку
# f1(os.getcwd())
import hashlib
astr = input()
adict = {
    'md5': hashlib.md5(astr.encode()).hexdigest(),
    'sha1': hashlib.sha1(astr.encode()).hexdigest(),
    'sha224': hashlib.sha224(astr.encode()).hexdigest(),
    'sha256': hashlib.sha256(astr.encode()).hexdigest(),
    'sha384': hashlib.sha384(astr.encode()).hexdigest(),
    'sha512': hashlib.sha512(astr.encode()).hexdigest()
}
alist = [key for key in adict]
alist.sort()
for i in alist:
    print(i, adict[i])


