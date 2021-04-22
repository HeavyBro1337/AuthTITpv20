import variables as var
import random
def login(): # Функция для входа в систему
	username = input("Type user's name	")
	password = input("Type a password	")
	if len(var.users) == 0: # Проверяем список на пустоту, если она пустая значит нет смысла дальше выполнять код
		print(var.throw_error(0))
		print()
		return None
	for u in var.users: # Проверку на существование пользователя по имени
		if u.username == username: # Если имя совпадает, то идем проверять пароль
			if u.password == password: # Проверяем пароль
				return u # В случае верного пароля, мы возвращаем данного пользователя для логина
			else: # В случае неверного пароля, то возвращаем статус неавторизированного пользователя
				print(var.throw_error(2))
				return None
	print(var.throw_error(0)) # В этой ситуации мы не нашли пользователя по имени и показываем ошибку об этом
	print()
	return None
def gen_password(): # Функция для генерации пароля
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper()
	str4 = str0+str1+str2+str3
	ls = list(str4)
	random.shuffle(ls)
	# Извлекаем из списка 12 произвольных значений
	psword = ''.join([random.choice(ls) for x in range(12)])
	return psword

def register(autogenerate): # Регистрируем пользователя
	username = input("Type user's name ")
	if does_user_exist(username) != None: # Не запускаем дальше код, если есть уже пользователь с таким именем
		return
	password = "" # Создаем переменную и присваиваем значение на базе опции авто-генерации
	new_user = None
	register_usr = False
	if autogenerate:
		password = gen_password()
		register_usr = True
	else:
		password = input("Type a password ")
		if check_password(password):
			register_usr = True
	if register_usr:
		new_user = var.user(username,password)
		var.users.append(new_user)


		print("Successfully registered new account")
		print()
	return new_user
def check_password(password: str): # Проверка пароля на выполнение следующих условий
	isdig = False # Есть хотя бы одно число
	isupper = False # Имеется хотя бы буква в верхнем регистре
	islower = False # Так же и в нижнем регистре

	for c in password: # Создаем цикл, который будет проходить по password
		if c.isdigit():
			isdig = True
		elif c.isupper():
			isupper = True
		elif c.islower():
			islower = True
		if isdig and isupper and islower:
			return True

	print(var.throw_error(1))
	return False


def does_user_exist(username): # Проверка на существование пользователя по имени
	for u in var.users:
		if u.username == username:
			print(var.throw_error(3))
			return u
	return None