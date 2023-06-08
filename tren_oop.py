from tkinter import *
window = Tk()
window.geometry('800x600')
canvas = Canvas(window, width=800, height=600)
canvas.pack()


class Human:
    def __init__(self, colour_head, colour_torso, colour_hands, colour_outline, x, y):
        self.colour_head = colour_head
        self.colour_torso = colour_torso
        self.colour_hands = colour_hands
        self.colour_outline = colour_outline
        self.y = x
        self.x = y

    def human_drawing(self):
        # голова
        canvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100, fill=self.colour_head,
                                outline=self.colour_outline)
        # торс
        canvas.create_rectangle(self.x - 25, self.y + 100, self.x + 125, self.y + 300, fill=self.colour_torso,
                                outline=self.colour_outline)
        # первая рука
        canvas.create_polygon(self.x - 25, self.y + 100, self.x - 25, self.y + 175, self.x - 175, self.y + 100,
                              fill=self.colour_hands, outline=self.colour_outline)
        # вторая рука
        canvas.create_polygon(self.x + 125, self.y + 100, self.x + 125, self.y + 175, self.x + 275, self.y + 100,
                              fill=self.colour_hands, outline=self.colour_outline)
        # первая нога
        canvas.create_polygon(self.x - 25, self.y + 300, self.x + 50, self.y + 300, self.x - 25, self.y + 450,
                              fill=self.colour_hands, outline=self.colour_outline)
        # вторая нога
        canvas.create_polygon(self.x + 50, self.y + 300, self.x + 125, self.y + 300, self.x + 125, self.y + 450,
                              fill=self.colour_hands, outline=self.colour_outline)


human = Human('red', 'yellow', 'green', 'black', 100, 300)
human.human_drawing()


window.mainloop()