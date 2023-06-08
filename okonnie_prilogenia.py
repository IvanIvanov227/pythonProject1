from tkinter import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup

root = Tk()
root.resizable(width=False, height=False)
root.title('Курс валют')
root.geometry('400x350+600+200')
root['bg'] = 'white'

image_1 = PhotoImage(file='bank.png')
label_image = Label(root, image=image_1)
label_image.image = image_1
label_image.place(x=0, y=0)

image_2 = PhotoImage(file='money.png')
label_image = Label(root, image=image_2)
label_image.image = image_2
label_image.place(x=230, y=210)

today = datetime.today().strftime('%d.%m.%Y')
url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
date = {'date_req': today}
response = requests.get(url, params=date).content
xml = BeautifulSoup(response, 'lxml')

id_EUR = 'R01239'
id_USD = 'R01235'
id_CNY = 'R01375'


def get_valute(id):
    return round(float(xml.find('valute', {'id': id}).value.text.replace(",", ".")), 2)


label_title_1 = Label(root, text='Курс валют', font=('Times New Roman', 16), bg='white', fg='red')
label_title_1.place(x=220, y=10)

label_title_2 = Label(root, text='Банк: Упитанный кот', font=('Times New Roman', 16), bg='white', fg='green')
label_title_2.place(x=170, y=70)

label_course = Label(root, text=f'Курс на: {today}', font=('Times New Roman', 16), bg='white', fg='black')
label_course.place(x=50, y=130)

label_course_USD = Label(root, text=f'$ {get_valute(id_USD)}', fg='blue', font=('Arial', 12))
label_course_USD.place(x=100, y=180)

label_course_EUR = Label(root, text=f'€ {get_valute(id_EUR)}', fg='blue', font=('Arial', 12))
label_course_EUR.place(x=100, y=230)

label_course_CNY = Label(root, text=f'元 {get_valute(id_CNY)}', fg='blue', font=('Arial', 12))
label_course_CNY.place(x=100, y=280)


root.mainloop()