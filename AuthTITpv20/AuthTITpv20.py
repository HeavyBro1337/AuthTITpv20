import Auth as au
import variables as var
import pickle
import account_management as accs
def print_help():
	print()
	print(f"Logged as {var.logged.username}" if var.logged != None else "Currently not logged in")
	print("/login - Log in using username and password" if var.logged == None else "/logout - Log out from the current account")
	if var.logged == None:
		print("/register - Register with all manually")
		print("/aregister - Register with auto-generated password")
	print("/printusers - Print all users")
	print("/printc - Print all users COMPACT")
	print("/sort - Sort users by name alphabetically")
	if var.logged != None:
		print()
		print("======== Account Management ========")
		print("/delete - Delete current account for good")
		print("/changename - Set new username")
		print("/changepassword - Change the password")
		print("/transfer - Transfer money to user")
		print()
		print(f"Balance: {var.logged.balance}€")
	print()

comm = ""
while True: # предлагаем пользователю загрузить базу данных о других пользователей
	try:
		open("users.pickle")
		ans = input("Hello, do you want to load users into the program? y/n ")
		if ans == "y":
			var.users = pickle.load(open("users.pickle", "rb", -1))
			break
		elif ans == "n":
			break
		else:
			print("Sorry?")
	except:
		break
while comm != "/exit": # Цикл работает до тех пор, пока пользователь не пропишет комманду /exit
	print_help()
	comm = input("Insert a command here =>	")
	if comm == "/login": # Цепочка "если" по всем командам
		if var.logged == None:
			var.logged = au.login()
	elif comm == "/register":
		if var.logged == None:
			var.logged = au.register(False)
	elif comm == "/aregister":
		if var.logged == None:
			var.logged = au.register(True)
	elif comm == "/printusers":
		if len(var.users) > 0:
			for u in var.users:
				u.print_user()
			print("========================")
			print()
			print("Amount of users: ", len(var.users))
		else:
			print()
			print("Currently, there are no users")
	elif comm == "/printc":
		if len(var.users) > 0:
			print("=================================")
			for u in var.users:
				print(u)
			print("=================================")
			print()
			print("Amount of users: ", len(var.users))
		else:
			print()
			print("Currently, there are no users")
	elif comm == "/logout":
		if var.logged != None:
			var.logged = None
	elif comm == "/delete":
		if var.logged != None:
			accs.delete_account(var.logged)
			var.logged = None
			print("Successfully removed account")
	elif comm == "/changename":
		if var.logged != None:
			accs.change_name(var.logged, input("Write new name "))
	elif comm == "/changepassword":
		if var.logged != None:
			accs.change_pass(var.logged)
	elif comm == "/exit":
		continue
	elif comm == "/transfer":
		if var.logged != None:
			accs.transfer(var.logged)
	elif comm == "/sort":
		var.users.sort()
		print()
		for u in var.users:
			print(u)
		print()
	else:
		print("Sorry?")
print("The programm has ended")
while True: # Запрашиваем у пользователя разрешение, чтобы сохранить файл на компьютер
	ans = input("Would you save users locally? y/n ")
	if ans == "y":
		with open("users.pickle", "wb") as file_:
			pickle.dump(var.users, file_, -1)
			break
	elif ans == "n":
		break
	else:
		print("Sorry?")


		