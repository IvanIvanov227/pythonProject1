from tkinter import *

def on_close():
    if int(count_text['text']) > 0:
        count_text['text'] = int(count_text['text']) - 1
        count_text.place(x=250, y=25, width=400, height=100)
        window.after(1000, on_close) # Время в милисекундах, after позволяет отложить выполнение программы на столько то секунд
    else:
        photo = PhotoImage(file='skelet.gif')
        label_image = Label(image=photo, bg='black')
        label_image.image = photo
        height = window.winfo_height() # узнаёт габариты экрана пользователя
        width = window.winfo_width()
        window.state('zoomed') # Окно откроется во весь экран
        label_image.place(width=width, height=height, x=0, y=0)

window = Tk()
window.geometry('900x300')
window.title('Dangerous')
window.config(bg='black') # Задний фон окна
window.resizable(width=False, height=False) # Нельзя изменять размер окна

text = Label(text='Ваш компьютер заражён!!!!!', bg='black', font=('Arial', 34), fg='green')
text.place(x=100, y=100, width=700, height=100)

count_text = Label(text='6', fg='green', bg='black', font=('Arial', 40))

window.protocol('WM_DELETE_WINDOW', on_close) # Команда позволяет отловить какое-то событие
window.mainloop()