from tkinter import *
from random import *


window = Tk()
w = 600
h = 600
window.geometry(str(w) + 'x' + str(h))

canvas = Canvas(window, width=w, height=h)
canvas.pack()

bg_photo = PhotoImage(file='bg_2.png')


class Knight:
    def __init__(self):
        self.x = 70
        self.y = h//2
        self.photo = PhotoImage(file='knight.png')
        self.v = 0
        self.v_2 = 0

    def up(self, event):
        if self.y > 0:
            self.v = -3
        else:
            self.v = 0

    def down(self, event):
        if self.y < h:
            self.v = 3
        else:
            self.v = 0

    def left(self, event):
        if self.x > 0:
            self.v_2 = -3
        else:
            self.v_2 = 0

    def right(self, event):
        if self.x < w:
            self.v_2 = 3
        else:
            self.v_2 = 0

    def stop(self, event):
        self.v = 0


class Dragons:
    def __init__(self):
        self.x = 750
        self.y = randint(100, 500)
        self.v = randint(1, 3)
        self.photo = PhotoImage(file='dragon.png')


knight = Knight()
dragons = []
for i in range(1):
    dragons.append(Dragons())


def game():
    """Отрисовка кадров"""
    canvas.delete('all')
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v
    knight.x += knight.v_2

    current_dragon = 0
    dragon_to_kill = -1
    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

        if ((dragon.x - knight.x) ** 2) + ((dragon.y - knight.y) ** 2) <= 96 ** 2:
            dragon_to_kill = current_dragon
        current_dragon += 1
        if dragon.x <= 0:
            # # dragons.clear()
            # for t in range(5):
            #     dragons.append(Dragons())
            # break
            canvas.delete('all')
            canvas.create_text(w / 2, h / 2, text='You lose!', font='Verdana 42', fill='red')
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w/2, h/2, text='You win!', font='Verdana 42', fill='red')
    else:
        window.after(5, game)


game()
window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<Key-Left>', knight.left)
window.bind('<Key-Right>', knight.right)
window.bind('<KeyRelease>', knight.stop)
window.mainloop()