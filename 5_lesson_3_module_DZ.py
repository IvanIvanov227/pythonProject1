# Первое задание

class MyFile:
    def __init__(self, name_file, reading_mode, encoding='utf-8'):
        self.name_file = name_file
        self.reading_mode = reading_mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.name_file, self.reading_mode, encoding=self.encoding)
        except FileNotFoundError:
            print('Данный файл не найден')
        except ValueError as e:
            print(f'ValueError: {e}')
        except AttributeError as y:
            print(f'AttributeError: {y}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_td):
        if self.file is not None:
            self.file.close()

with MyFile('<имя файла>', '<режим открытия>') as file:
    if file is not None:
        file.write(input())


# Второе задание

# class Infinitely:
#     def __init__(self, count):
#         self.count = count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.count
#
#
# infinitely = Infinitely('Привет')
# for i in infinitely:
#     print(i)
