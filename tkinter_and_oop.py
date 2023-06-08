from tkinter import *
window = Tk()
window.geometry('800x600')

# создал холст
canvas = Canvas(window, width=800, height=600, bg='white')

# прикрепил холст
canvas.pack()

# # рисую квадрат (fill - заливка, outline - цвет рамки)
# canvas.create_rectangle(10, 10, 30, 30, fill='yellow', outline='black')
# canvas.create_rectangle(10, 50, 50, 90, fill='yellow', outline='black')
# canvas.create_rectangle(10, 110, 70, 170, fill='yellow', outline='black')
#
# # рисую треугольник
# canvas.create_polygon(100, 100, 120, 80, 140, 140, fill='yellow', outline='black')

canvas.create_polygon(350, 100, 450, 100, 400, 50, fill='green', outline='black')
canvas.create_rectangle(350, 100, 450, 200, fill='yellow', outline='black')
canvas.create_rectangle(375, 125, 425, 175, fill='white', outline='black')

# создаём решётку
canvas.create_rectangle(399, 125, 400, 175, fill='black', outline='black')
canvas.create_rectangle(375, 150, 425, 151, fill='black', outline='black')

# наклонная линия
# x1 = 0
# y1 = 0
# x2 = 0
# y2 = 0
# for i in range(200):
#     canvas.create_rectangle(10 + x1, 150 + y1, 11 + x2, 151 + y2, fill='black', outline='black')
#     x1 += 1
#     y1 += 1
#     x2 += 1
#     y2 += 1


window.mainloop()