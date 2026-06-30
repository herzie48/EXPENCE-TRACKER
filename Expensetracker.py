expenses = []
while True :
	print("Menu")
	print("1.Add an expense")
	print("2.Remove an expense")
	print("3.View all expenses")
	print("4.Total expenses")
	print("5.Exit")
	print("Choose a number from 1-5 :")
	n = int(input("Enter your choice :"))
	if n == 1:
		expense = {
			"date":input("Date : "),
			"category":input("Category : "),
			"description":input("Description : "),
			"amount":int(input("Enter amount : "))
		}
		expenses.append(expense)
	elif n == 2:
		if len(expenses) == 0:
			print("No expenses to remove.")
		else:
			choice = int(input("Enter the no. of the expense to be removed:"))
			if 1<=choice<=len(expenses):
				expenses.pop(choice -1)
			else:
				print("Invalid choice ")
	elif n == 3:
		if len(expenses) == 0:
			print("No expenses to view.")
		else:
			for i,expense in enumerate (expenses,start =1):
				print(f"{i}. Date : { expense['date']}")
				print(f"      Category : { expense['category']}")
				print(f"      Description : {expense['description']}")
				print(f"      Amount : {expense['amount']}")
				print()
	elif n ==4:
		total = 0
		for expense in expenses:
			total += expense["amount"]
		print(f'Total Amount : {total}')
	elif n== 5:
		break
	else:
		print("Invalid Choice!")




































