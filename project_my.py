from tkinter import *
from fpdf import FPDF
from datetime import datetime


exit_list = 0
points = 0
math_examples = [
    {'examples': '23 + 48',
     'answer': ['70', '51', '71', '25']
     },
    {'examples': '5 * 13',
     'answer': ['17', '75', '65', '55']
     },
    {'examples': '2**10',
     'answer': ['1024', '512', '2048', '20']
     },
    {'examples': '123 - 48',
     'answer': ['62', '75', '65', '54']
     },
    {'examples': '3 - 3 * 3',
     'answer': ['-6', '0', '6', '9']
     },
    {'examples': '84 / 7 - 5',
     'answer': ['17', '7', '42', '12']
     },
    {'examples': '2 + 2',
     'answer': ['1', '2', '3', '4']
     },
    {'examples': '15**2',
     'answer': ['5', '225', '30', '125']
     },
    {'examples': '16 * 4 / 8',
     'answer': ['8', '0.5', '16', '320']
     },
    {'examples': '0 ** 0',
     'answer': ['1', '0', '2', '10']
     }
]


class Game:
    """Поведение игры"""

    def __init__(self, answer, question, label_points):
        self.answer = answer
        self.question = question
        self.label_points = label_points

    def right_answer(self):
        """Обрабатывает ответ пользователя"""
        global points
        for w in window.winfo_children():
            if w.winfo_class() == 'Button':
                w.destroy()
        if int(self.answer) == eval(self.question['examples']):
            points += 10
            check_points(points, self.label_points)
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
    y = 0
    x = 0
    if points < 100:
        label_points = Label(text=f'Очки: {points}', font=('Arial', 25), bg='blue', fg='white')
        label_points.place(x=990, y=110, width=200, height=70)

        for question in math_examples:
            label_text['text'] = f'{question["examples"]} = ?'
            for answer in question['answer']:
                plays = Game(answer, question, label_points)
                answer_user = Button(text=answer, font=('Times New Roman', 16), command=plays.right_answer)
                answer_user.place(x=100 + x, y=150 + y, width=100, height=70)
                x += 200
                y += 100

            break
        del math_examples[exit_list]

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


def next_win():
    """Кнопка ПРОДОЛЖИТЬ после выигрыша"""
    next_pdf = Button(text='Продолжить', font=('Times New Roman', 14), command=question_of_pdf, fg='blue')
    next_pdf.place(x=1030, y=520, width=150, height=60)


def question_of_pdf():
    """Спрашивает, нужно ли делать поздравительную открытку?"""
    # Удаляет все виджеты на экране
    for w in window.winfo_children():
        w.destroy()

    label_pdf = Label(text='Вы хотите получить грамоту \nоб успешном окончании нашего теста?', font=('Arial', 30), bg='green', fg='yellow')
    label_pdf.place(x=0, y=0, width=1200, height=300)

    user_button_1 = Button(text='ДА', font=('Times New Roman', 25), command=pdf_win, fg='blue')
    user_button_1.place(x=300, y=300, width=150, height=80)

    user_button_2 = Button(text='НЕТ', font=('Times New Roman', 25), command=on_close, fg='red')
    user_button_2.place(x=700, y=300, width=150, height=80)


def pdf_win():
    """Создаёт поздравительную открытку для победителя"""
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_page()

    pdf.image('фон.png', h=210, w=297, x=0, y=0)

    pdf.add_font('Times New Roman', '', 'C:\WINDOWS\FONTS\COUR.ttf', uni=True)
    pdf.set_font('Times New Roman', size=40)
    pdf.set_text_color(150, 30, 200)
    pdf.set_left_margin(80)
    pdf.set_top_margin(30)
    pdf.cell(150, 60, txt='Грамота вручается', align='C', border=0, fill=False, ln=1)

    pdf.set_text_color(124, 89, 147)
    pdf.cell(150, 40, txt='Талантливому Математику', align='C', border=0, fill=False, ln=1)

    pdf.set_text_color(59, 50, 200)
    pdf.cell(150, 30, txt='ПОЗДРАВЛЯЕМ!!!', align='C', border=0, fill=False, ln=1)

    date = datetime.today().strftime('%d.%m.%Y')
    pdf.set_text_color(51, 255, 51)
    pdf.set_font('Times New Roman', size=20)
    pdf.set_right_margin(60)

    pdf.cell(0, 20, txt=f'{date}, Министерство Просвещения РФ', align='C', ln=1)
    pdf.output('win.pdf')
    on_close()


def on_close():
    """Программа закрывается"""
    window.destroy()


window = Tk()
window.title('Устный счёт')
window.geometry('1200x600')
window.config(bg='white')

label_text = Label(text='ПОПРОБУЙ СОСЧИТАТЬ В УМЕ!', font=('Arial', 30), bg='green', fg='yellow')
label_text.place(x=0, y=0, width=1200, height=100)

button_start = Button(text='PLAY', font=('Times New Roman', 35), bg='white', fg='green', command=start)
button_start.place(x=500, y=300, width=200, height=100)

window.mainloop()
