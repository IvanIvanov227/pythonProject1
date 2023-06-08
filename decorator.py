def header(func):

    def inner(n, m, v):
        print('<h1>')
        func(n, m, v)
        print('</h1>')
    return inner


def table(func):

    def inner(n, m, v):
        print('<table>')
        func(n, m, v)
        print('</table>')
    return inner


@ header
def say(name, fullname, age):
    print('hello', name, fullname, age)


say('Vasya', 'Sivkov', 100)
