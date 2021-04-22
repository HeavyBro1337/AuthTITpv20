import variables as var
import Auth as au


def transfer(u : var.user):
	name = None
	amount = None
	user = None
	while user == None:
		try:
			name = input("Send money to: ")
			amount = int(input("How much? "))
			user = au.does_user_exist(name)
			if amount == 0:
				return
			if u.balance < amount:
				print("You don't have that much. Try again, or type 0 in amount to cancel")
				continue
			break
		except:
			print("Error, please try again")
	if user != None:
		u.balance -= amount
		user.balance += amount
		print("Transaction successfull!")



def change_name(u : var.user, new_name): # Изменить имя аккаунта
	index = var.users.index(u)
	if not au.does_user_exist(new_name) != None:
		var.users[index].username = new_name



def delete_account(u : var.user): # Удалить аккаунт с базы данных
	var.users.remove(u)



def change_pass(u : var.user): # Изменить пароль аккаунта
	index = var.users.index(u)
	old_pass = input("Type the old password ")
	if old_pass == u.password:
		new_password = input("Type the new password ")
		if au.check_password(new_password):
			var.users[index].password = new_password
			print("Successfully changed the password!")

