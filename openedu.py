# Обработка запросов HTTP сервера
from http.server import BaseHTTPRequestHandler
# HTTP запросы
from http.server import HTTPServer


# # Выводит текст на экран на веб-сайте
# class ServerWorking(BaseHTTPRequestHandler):
#     def do_it(self):
#         self.send_response(200)
#         # Заголовок: Первый параметр - текст HTML
#         self.send_header('Content-type', 'text/html')
#         # Закрываем заголовок
#         self.end_headers()
#         # Пишем в текст в определённом заголовке и кодировке
#         self.wfile.write(bytes('<html><head><title>Обработка</title></head>', 'utf-8'))
#         self.wfile.write((bytes('<body><h1>Питон работает</h1>', 'utf-8')))
#         # Указываем путь, из которого работаем
#         self.wfile.write(bytes('<p> %s</p>' % self.path, 'utf-8'))
#         self.wfile.write(bytes('<body></html>', 'utf-8'))
#
#
# # 1-ый параметр - серверный адрес, 2-ой - порт
# serv_address = ('', 8080)
# # Запуск HTTP сервера 2-ой параметр - с помощью чего обрабатываем запросы
# serv = HTTPServer(serv_address, BaseHTTPRequestHandler)
# # Постоянная работа сервера
# serv.serve_forever()

# CGI запросы
# from http.server import CGIHTTPRequestHandler
#
# # Создание CGI сервера
# server_address = ('localhost', 8080)
# http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
# http_server.serve_forever()


# from urllib.parse import urlparse
# import requests
# from bs4 import BeautifulSoup
# astr = input()
# url_file = requests.get('http://en.ifmo.ru/en/contacts/Contacts.htm').text
# html_file = BeautifulSoup(url_file, 'xml')
# url_res = urlparse(astr)
# print(tuple(url_res))
# print(html_file.find('h1').text)

from urllib.parse import urlparse
import urllib.request
import re
astr = input()
url_file = urllib.request.urlopen('http://en.ifmo.ru/en/contacts/Contacts.htm').read().decode('utf-8')
html_file = re.findall(r'<h1>(.*?)</h1>', url_file)
url_res = urlparse(astr)
print(tuple(url_res))
print(*html_file)

