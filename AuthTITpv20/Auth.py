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

def register(autogenerate):
	username = input("Type user's name ")
	if does_user_exist(username):
		return
	password = ""
	if autogenerate:
		password = gen_password()
		new_user = var.user(username,password)
		var.users.append(new_user)
		print("Successfully registered new account")
		print()
		return new_user
	else:
		password = input("Type a password ")
		if check_password(password):
			new_user = var.user(username,password)
			var.users.append(new_user)
			print("Successfully registered new account")
			print()
			return new_user
def check_password(password: str):
	isdig = False
	isupper = False
	islower = False

	for c in password:
		if c.isdigit():
			isdig = True
			break
	for c in password:
		if c.isupper():
			isupper = True
			break
	for c in password:
		if c.islower():
			islower = True
			break

	result = isdig and isupper and islower
	if result:
		return True
	else:
		print(var.throw_error(1))
		return False


def does_user_exist(username):
	for u in var.users:
		if u.username == username:
			print(var.throw_error(3))
			return True
	return False


def change_name(u : var.user, new_name):
	index = var.users.index(u)
	if not does_user_exist(new_name):
		var.users[index].username = new_name
def delete_account(u : var.user):
	var.users.remove(u)
def change_pass(u : var.user):
	index = var.users.index(u)
	old_pass = input("Type the old password ")
	if old_pass == u.password:
		new_password = input("Type the new password ")
		if check_password(new_password):
			var.users[index].password = new_password
			print("Successfully changed the password!")