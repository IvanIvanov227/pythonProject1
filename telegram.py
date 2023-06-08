
def my_decorator(func_to_decorate):
    def decorated_func():
        print('Я начиная работать')
        func_to_decorate()
        print('Я закончил работать')
    return decorated_func

@my_decorator

# это аргумент для декоратора
def func_to_decorate():
    print('Я работаю')


func_to_decorate()