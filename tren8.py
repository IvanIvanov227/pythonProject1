from tkinter import *
import time

def on_close():
    button.place_forget()
    text.destroy()
    text_2 = Label(text='АХАХАХ\nЭто\nобман!!!', bg='red', font=('Arial', 40), fg='yellow')
    text_2.place(x=50, y=0, width=250, height=700)
    time.sleep(5)
    skam()

def skam():

    window.config(bg='red')
    text_3 = Label(text='Переводите\nденьги!!!\n Или мы\nвзломаем\nваш\nкомпьютер', font=('Arial', 35), fg='yellow', bg='red')
    text_3.place(x=1050, y=0, width=280, height=900)
    photo = PhotoImage(file='злой.png')
    label_image = Label(image=photo)
    label_image.image = photo
    label_image.place(width=700, height=700, x=325, y=180)
    hacking()

def hacking():
    if int(count_text['text']) > 0:
        count_text['text'] = int(count_text['text']) - 1
        count_text.place(x=550, y=25, width=400, height=100)
        window.after(1000, hacking)
    else:
        window.config(bg='black')
        photo = PhotoImage(file='скример (1).png')
        label_image = Label(image=photo, bg='black')
        label_image.image = photo
        height = window.winfo_height()
        width = window.winfo_width()
        window.state('zoomed')
        label_image.place(width=width, height=height, x=0, y=0)

def off_close():
    pass

window = Tk()
window.geometry('1400x900')
window.title('Инвестиции - это просто!')
window.config(bg='white')
window.resizable(width=False, height=False)

text = Label(text='Мы знаем как из 100 рублей\nсделать 1 млн. рублей!!!', bg='green', font=('Arial', 30), fg='yellow')
text.place(x=0, y=0, width=1400, height=200)

button = Button(text='УЗНАТЬ СЕКРЕТ', font=('Times New Roman', 50), fg='blue', command=on_close)
button.place(width=700, height=300, x=380, y=400)

count_text = Label(text='16', fg='blue', bg='red', font=('Arial', 50))

window.protocol('WM_DELETE_WINDOW', off_close)

window.mainloop()