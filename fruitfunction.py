fruit={}
cart_list=[]

def main_menu():
	print("1.Add fruit")
	print("2.Delete fruit by name")
	print("3.Search fruit")
	print("4.Change fruit and rate")
	print("5.Display details")
	print("6.Add to cart")
	print("7.Display cart")
	print("8.Exit")

def add_fruit():
	fid = int(input("Enter the fruit id"))
	if fid not in fruit.keys():
		fname = input("Enter the name of the fruit")
		frate = int(input("Enter the fruit rate"))
		fimported = input("Imported from")
		fimportdate = input("Imported date")
		fbuyed=int(input("Enter the price of the fruit"))
		temp ={
			"fruit_name":fname,
			"fruit_rate":frate,
			"imported_from":fimported,
			"import_date":fimportdate,
			"fruit_buy":fbuyed
		}
		fruit[fid] = temp
		print(fruit)
	else:
		print("fruit id is already taken")

def delete_fruit():
	fid = int(input("Enter the fruit id"))
	name = input("Enter the name of the fruit")
	flag = False
	if fid in fruit.keys():
		for fdel in fruit.values():
			print(fdel['fruit_name'] == name)
			flag = True
	else:
		print("Invalid fruit id")
	if flag == True:
		del fruit[fid]
def search_fruit():
	print("1.search by name:")
	print("2.search by rate:")
	ch = int(input("Enter the choice"))
	if ch == 1:
		
		name = input("Enter the fruit name to be search")
		flag = False
		print("name",name)
		for i in fruit.values():
			if i["fruit_name"] == name:
				flag = True
				print("flag=>",flag)
			else:
				print("Invalid name")
		if flag == True:
			print(f"{i['fruit_name']} | {i['fruit_rate']} | {i['imported_from']} | {i['import_date']} | {i['fruit_buy']}")
	elif ch == 2:
		
		rate = int(input("Enter the fruit rate to be search"))
		flag = False
		for i in fruit.values():
			if i["fruit_rate"] == rate:
				flag = True
			else:
				print("\tInvalid raate")
		if flag == True:
			print(f"{i['fruit_name']} | {i['fruit_rate']} | {i['imported_from']} | {i['import_date']} | {i['fruit_buy']}")

def change_fruit():
	
	print("1 for Change by name")
	print("2 for Change by rate")
	ch1 = int(input("Enter the choice"))
	if ch1 == 1:
		
		fru_id = int(input("Enter the fruit id"))
		if fru_id not in fruit.keys():
			print("Invalid fruid id")
		else:
			new_name = input("Enter the new name")
			fruit[fru_id]['fruit_name'] = new_name
			print(fruit)
	if ch1 == 2:
		
		fru_id = int(input("Enter the fruit id"))
		if fru_id not in fruit.keys():
			print("Invalid id")
		else:
			new_rate = int(input("Enter new rate"))
			fruit[fru_id]['fruit_rate'] = new_rate
			print(fruit)

def display_fruit():
	
	for fid,fruits in fruit.items():
		print(f'{fid} | {fruits["fruit_name"]} | {fruits["fruit_rate"]} | {fruits["imported_from"]} | {fruits["import_date"]} | {fruits["fruit_buy"]}')

def add_to_cart():
	fid = int(input("Enter the fruit id"))
	if fid in fruit.keys():
		cart_list.append(fid)
		print(cart_list)

def display_cart():
	for i in cart_list:
		print(f"{i} | {fruit[i]}")


while True:
	main_menu()
	choice = int(input("Enter the choice"))
	if choice == 1:
		add_fruit()
	elif choice == 2:
		delete_fruit()	
	elif choice == 3:
		search_fruit()				
	elif choice == 4:
		change_fruit()
	elif choice == 5:
		display_fruit()

	elif choice == 6:
		add_to_cart()
	elif choice == 7:
		display_cart()
	elif choice == 8:
		break
	else:
		print("Invalid entry")
