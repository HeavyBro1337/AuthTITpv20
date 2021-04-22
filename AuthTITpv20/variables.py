class user: # Создаем класс для определения пользователя. Он будет содержать два поля (Имя и пароль) и один метод.
	def __init__(self, username, password):
		self.username = username
		self.password = password
	def print_user(self):
		print("========================")
		print(f"Name : {self.username}")
		print(f"Password : {self.password}")

users = [] # Экземпляры класса будем хранить в списке, чтобы легче было
logged = None
def throw_error(code): # Создаем функцию, которая на основе кода ошибки выводит подробное описание
	if code == 0:
		return "Log in failed. User not found"
	elif code == 1:
		return "Less reliable password"
	elif code == 2:
		return "Wrong password"
	elif code == 3:
		return "User with that name already exists"
