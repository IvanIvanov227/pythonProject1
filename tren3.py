from tkinter import *

def check():
    global score, cur_q
    answer = var.get()
    if bool(answer) == facts[cur_q]['right']:
        score += 1
    if cur_q < len(facts) - 1:
        cur_q += 1
        fact['text'] = facts[cur_q]['text']
    else:
        points_label = Label(text=f'Количество набранных очков {score}', font=('Times New Roman', 24), fg='red')
        points_label.place(x=0, y=0, width=700, height=250)

window = Tk() # Создали окно
window.title('Самый сложный тест') # Называем окно
window.geometry('700x500') # Размеры окна

title_label = Label(text='Тестирование по вселенной Marvel', font=('Times New Roman', 24), bg='green', fg='white') # Параметры виджета
title_label.place(width=700, height=50, x=0, y=0) # координаты виджета на экране

facts = [
    {'text': 'Человеческое имя Халка - Брюс Беннер', 'right': 1},
    {'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
    {'text': 'До появления костюма супергероя, человек муравей занимался воровством', 'right': 1},
    {'text': 'Выдуманный город Дженоша является родиной Черной Пантеры', 'right': 0}
]

score = 0
cur_q = 0

fact = Message(text=facts[cur_q]['text'], font=('Times New Roman', 14), width=680, borderwidth=0) # Много строк текста
fact.configure(justify=CENTER)
fact.place(x=10, y=70) # Координаты

var = IntVar() # Кнопка
true = Radiobutton(text='Правда', variable=var, value=1, font=('Times New Roman', 12))
true.place(x=10, y=120)
false = Radiobutton(text='Ложь', variable=var, value=0, font=('Times New Roman', 12))
false.place(x=10, y=150)

b = Button(text='Ответить', command=check, font=('Arial', 13))
b.place(x=200, y=130)
window.mainloop() # Прорисовка окна (бесконечный цикл)