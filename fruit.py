print("Fruit shop")

fruit=[]
while True:
	print("Enter 1 for add fruit ")
	print("Enter 2 for delete fruit")
	print("Enter 3 for search fruit by name and rate")
	print("Enter 4 for change fruit name and rate")
	print("Enter 5 for display")
	print("Enter 6 for exit")

	choice=int(input())

	if(choice == 1):
		print("enter fruit name")
		aname=input()
		print("enter fruit rate")
		arate=input()
		fruit.append([aname,arate])
		print(fruit)
	elif(choice == 2):
		print("enter fruit name to delete")
		dname=input()
		for i in fruit:
			if (fruit[fruit.index(i)][0] == dname):
				#print("found")
				fruit.pop(fruit.index(i))
				print(fruit)
			else:
				print("not found")
		#	print("found")
		#	fruit.remove(dname)
		#else:
		#	print("not found")

	elif(choice == 3):
		sname=input("enter fruit name to search")
		srate=input("enter fruit rate to search")
		for i in fruit:
			if (fruit[fruit.index(i)][0] == sname) and (fruit[fruit.index(i)][1] == srate):
				print("fruit found")
			else:
				print("not found")
#		srate=input(("enter fruit rate to search"))
#		for i in fruit:
#			if fruit[fruit.index(i)][1] == srate:
#				print("rate found")
#			else:
#				print("not found")
	elif(choice == 4):
		cname=input("enter fruit name")
		for i in fruit:
			if(fruit[fruit.index(i)][0] == cname):
				newname=input("New name")
				newrate=input("New rate")
				fruit[fruit.index(i)][0]=newname
				fruit[fruit.index(i)][1]=newrate
	elif(choice == 5):
		print(fruit)
	elif(choice == 6):
		break;
	else:
		print("invalid entry")

