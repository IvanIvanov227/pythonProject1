from fpdf import FPDF

pdf = FPDF('P', 'cm', (10, 15)) # Параметры странички
pdf.add_page() # Создаём страничку
pdf.add_font('courier', '', 'C:\WINDOWS\FONTS\COUR.ttf', uni=True) # '' - стиль шрифта
pdf.set_font('courier', size=16)
pdf.set_text_color(0, 255, 0) # Цвет заливки надписи, текста
pdf.set_fill_color(155, 50, 168) # Цвет заливки рамочки
pdf.set_draw_color(0, 0, 255) # Цвет рамочки
pdf.cell(8, 5, txt='Privet!', align='C', border=1, fill=True) # Параметры четырёхугольника

pdf.image('pic.jpg', h=0, w=10, x=0, y=5)

pdf.output('test_pdf.pdf')
