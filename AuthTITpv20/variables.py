import datetime
import random

class user: # Создаем класс для определения пользователя. Он будет содержать два поля (Имя и пароль) и один метод.
	def __init__(self, username, password): # Конструктор с параметрами
		self.username = username
		self.password = password
		self.date = datetime.datetime.now()
		self.balance = random.choice([0,200,500])
	def print_user(self): # Вывести на экран информацию о пользователе
		print("========================")
		print(f"Name : {self.username}")
		print(f"Password : {self.password}")
		print(f"Created in {self.date}")
		print(f"Balance : {self.balance}€")
	def __str__(self): # Оверрайд метода, который возвращает строку при принте. Схожий с ToString(); в C#
		return f"{self.username}\t{self.password}\t{self.date}\t{self.balance}€"
	def __lt__(self, value): # Добавляет возможность сравнить два класса со знаком <
		return ord(self.username[0]) < ord(value.username[0])

users = [] # Экземпляры класса будем хранить в списке, чтобы легче было
logged = None
def throw_error(code): # Создаем функцию, которая на основе кода ошибки выводит подробное описание
	if code == 0:
		return "Log in failed. User not found" # Авторизация провалилась - Пользователь не найден
	elif code == 1:
		return "Less reliable password. Requires at least 1 uppercase and 1 digit symbol" # Менее надежный пароль 
	elif code == 2:
		return "Wrong password" # Неверный пароль
	elif code == 3:
		return "User with that name already exists" # Пользователь с таким именем уже существует
