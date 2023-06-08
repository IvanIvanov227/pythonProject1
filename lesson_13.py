from fpdf import FPDF
from datetime import datetime

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

pdf.image('bg.jpg', h=297, w=210, x=0, y=0)

pdf.add_font('Times New Roman', '', 'C:\WINDOWS\FONTS\COUR.ttf', uni=True)
pdf.set_font('Times New Roman', size=37)
pdf.set_text_color(0, 0, 0)
name = input('Введите имя друга:\n')
pdf.cell(0, 95, ln=1)
pdf.cell(0, 20, txt=f'Дорогой, {name}!', align='C', border=0, fill=False, ln=1)

pdf.set_font('Times New Roman', size=18)
pdf.set_draw_color(0, 0, 0)
message = input('Введите текст поздравления\n')
pdf.set_left_margin(50) # отступ слева
pdf.set_right_margin(50) # отступ справа
pdf.multi_cell(0, 10, txt=message, align='C')
# multi_cell может принимать несколько строк текста, вторая цифра может отвечать за интервал между строками
# ln=1 - под каждой ячейкой будут располагаться

date = datetime.today().strftime('%d.%m.%Y')
# из всей строки оставляем день, месяц и год в нужном нам порядке
# (день.месяц.год)
pdf.set_text_color(124, 89, 147)
pdf.cell(0, 20, txt=date, align='R', ln=1)

author = input('Введите ваше имя\n')
pdf.cell(0, 10, txt=author, align='R', ln=1)

pdf.output('card.pdf')