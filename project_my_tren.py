from tkinter import *
from random import *
from functools import partial

points = 0


def right_answer(number_right_answer, number_button, label_points):
    """Обрабатывает ответ пользователя"""
    global points
    for w in window.winfo_children():
        if w.winfo_class() == 'Button':
            w.destroy()
    if number_right_answer == number_button:
        points += 10
        check_points(points, label_points)
        answer_question()

    else:
        window['bg'] = 'blue'
        label_exit = Label(text='Вы ответили неправильно\nИгра окончена :(', font=('Arial', 40), bg='blue',
                               fg='yellow')
        label_exit.place(x=0, y=0, width=1200, height=210)

        photo_exit = PhotoImage(file='грустный смайл.png')
        label_image = Label(image=photo_exit, bg='blue')
        label_image.image = photo_exit
        label_image.place(width=454, height=420, x=380, y=180)

        loss_user()


def loss_user():
    """Выводит кнопку с выводом из приложения"""
    next_pdf = Button(text='ВЫЙТИ', font=('Times New Roman', 16), command=on_close, fg='red')
    next_pdf.place(x=1030, y=520, width=150, height=60)


def start():
    """Начинает игру после нажатия кнопки 'Play'"""
    button_start.place_forget()
    answer_question()


def check_points(point, label_points):
    """Считает очки"""
    label_points['text'] = f'Очки: {point}'


def answer_question():
    """Выводит на экран пример и кнопки с ответами"""
    global randint_1, randint_2
    if points < 100:
        label_points = Label(text=f'Очки: {points}', font=('Arial', 25), bg='blue', fg='white')
        label_points.place(x=990, y=110, width=200, height=70)

        operation = ['+', '-', '*', '/']
        random_operation = choice(operation)
        randint_1 = randint(0, 100)
        randint_2 = randint(0, 100)

        while random_operation == '/' and randint_2 > randint_1:
            randint_1 = randint(0, 100)
            randint_2 = randint(0, 100)

        while random_operation == '/' and randint_2 == 0:
            randint_1 = randint(0, 100)
            randint_2 = randint(0, 100)

        question = f'{randint_1} {random_operation} {randint_2}'
        label_text['text'] = f'{question} = ?'

        if len(question) > 5:
            question = round(eval(question), 3)
        else:
            question = eval(question)

        number_right_answer = randint(1, 4)

        answer_question_button(number_right_answer, question, label_points, random_operation)

    else:
        window['bg'] = 'green'
        label_win = Label(text='Да вы математик!!!\nПоздравляем!!!', font=('Arial', 35),
                          bg='green', fg='yellow')
        label_win.place(x=0, y=0, width=1200, height=300)

        photo_win = PhotoImage(file='смайл.png')
        label_image = Label(image=photo_win, bg='green')
        label_image.image = photo_win
        label_image.place(width=376, height=308, x=400, y=250)

        next_win()


def answer_question_button(number_right_answer, question, label_points, random_operation):
    """Выводит на экран кнопки"""
    y = 0
    x = 0
    if number_right_answer == 1:
        answer_user_1 = Button(text=question, font=('Times New Roman', 16), command=partial(right_answer,
                                                                                            number_right_answer, 1,
                                                                                            label_points))
        answer_user_1.place(x=100, y=150, width=100, height=70)
        t = 1
        for i in range(3):
            answer_user = Button(text=random_examples(random_operation, question), font=('Times New Roman', 16),
                                 command=partial(right_answer, number_right_answer, 1 + t, label_points))
            answer_user.place(x=200 + x, y=250 + y, width=100, height=70)
            t += 1
            x += 200
            y += 100

    elif number_right_answer == 2:

        answer_user_1 = Button(text=random_examples(random_operation, question), font=('Times New Roman', 16),
                               command=partial(right_answer, number_right_answer, 1, label_points))
        answer_user_1.place(x=100, y=150, width=100, height=70)
        answer_user_2 = Button(text=question,
                               font=('Times New Roman', 16), command=partial(right_answer, number_right_answer, 2,
                                                                             label_points))
        answer_user_2.place(x=300, y=250, width=100, height=70)
        answer_user_3 = Button(text=random_examples(random_operation, question),
                               font=('Times New Roman', 16), command=partial(right_answer, number_right_answer, 3,
                                                                             label_points))
        answer_user_3.place(x=500, y=350, width=100, height=70)
        answer_user_4 = Button(text=random_examples(random_operation, question),
                               font=('Times New Roman', 16), command=partial(right_answer, number_right_answer, 4,
                                                                             label_points))
        answer_user_4.place(x=700, y=450, width=100, height=70)

    elif number_right_answer == 3:
        answer_user_1 = Button(text=random_examples(random_operation, question),
                               font=('Times New Roman', 16), command=partial(right_answer, number_right_answer, 1,
                                                                             label_points))
        answer_user_1.place(x=100, y=150, width=100, height=70)
        answer_user_2 = Button(text=random_examples(random_operation, question),
                               font=('Times New Roman', 16), command=partial(right_answer, number_right_answer, 2,
                                                                             label_points))
        answer_user_2.place(x=300, y=250, width=100, height=70)
        answer_user_3 = Button(text=question,
                               font=('Times New Roman', 16), command=partial(right_answer, number_right_answer, 3,
                                                                             label_points))
        answer_user_3.place(x=500, y=350, width=100, height=70)
        answer_user_4 = Button(text=random_examples(random_operation, question),
                               font=('Times New Roman', 16), command=partial(right_answer, number_right_answer, 4,
                                                                             label_points))
        answer_user_4.place(x=700, y=450, width=100, height=70)

    else:
        t = 0
        for i in range(3):
            answer_user = Button(text=random_examples(random_operation, question), font=('Times New Roman', 16),
                                 command=partial(right_answer, number_right_answer, 1 + t, label_points))
            answer_user.place(x=100 + x, y=150 + y, width=100, height=70)
            t += 1
            x += 200
            y += 100
        answer_user_1 = Button(text=question, font=('Times New Roman', 16), command=partial(right_answer,
                                                                                            number_right_answer, 4,
                                                                                            label_points))
        answer_user_1.place(x=700, y=450, width=100, height=70)


def random_examples(random_operation, question):
    """Если нужно, то округляет число"""
    random_1 = randint(0, 100)
    random_2 = randint(0, 100)
    while random_operation == '/' and random_2 == 0:
        random_1 = randint(0, 100)
        random_2 = randint(0, 100)
    answer = eval(f'{random_1} {random_operation} {random_2}')

    if answer != question:
        if len(str(answer)) > 5:
            return round(answer, 3)
        else:
            return eval(f'{randint(0, 100)} {random_operation} {randint(0, 100)}')
    else:
        random_operation(random_operation, question)


def next_win():
    """Кнопка Спасибо после выигрыша"""
    next_pdf = Button(text='Спасибо!', font=('Times New Roman', 14), command=on_close, fg='blue')
    next_pdf.place(x=1030, y=520, width=150, height=60)


def on_close():
    """Программа закрывается"""
    window.destroy()


window = Tk()
window.title('Счёт в столбик')
window.geometry('1200x600')
window.config(bg='white')

label_text = Label(text='ПОПРОБУЙ СОСЧИТАТЬ!', font=('Arial', 30), bg='green', fg='yellow')
label_text.place(x=0, y=0, width=1200, height=100)

button_start = Button(text='PLAY', font=('Times New Roman', 35), bg='white', fg='green', command=start)
button_start.place(x=500, y=300, width=200, height=100)

window.mainloop()