import Auth as au
import variables as var

def print_help():
	print()
	print(f"Logged as {var.logged.username}" if var.logged != None else "Currently not logged in")
	print("/login - Log in using username and password" if var.logged == None else "/logout - Log out from the current account")
	print("/register - Register with all manually")
	print("/aregister - Register with auto-generated password")
	print("/printusers - Print all users")
	if var.logged != None:
		print("======== Account Management ========")
		print("/delete - Delete current account for good")
		print("/changename - Set new username")
		print("/changepassword - Change the password")
	print()

while True:
	print_help()
	comm = input("Insert a command here =>	")
	if comm == "/login":
		if var.logged == None:
			var.logged = au.login()
	elif comm == "/register":
		if var.logged == None:
			var.logged = au.register(False)
	elif comm == "/aregister":
		if var.logged == None:
			var.logged = au.register(True)
	elif comm == "/printusers":
		for u in var.users:
			u.print_user()
		print("========================")
		print()
		print("Amount of users: ", len(var.users))
	elif comm == "/logout":
		if var.logged != None:
			var.logged = None
	elif comm == "/delete":
		if var.logged != None:
			au.delete_account(var.logged)
			var.logged = None
			print("Successfully removed account")
	elif comm == "/changename":
		if var.logged != None:
			au.change_name(var.logged, input("Write new name "))
	elif comm == "/changepassword":
		if var.logged != None:
			au.change_pass(var.logged)
	else:
		print("Sorry?")
		