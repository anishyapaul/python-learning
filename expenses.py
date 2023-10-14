#expenses=[11,34,56,23.10,3,5.7,89]
expenses=[]
total=0
num_of_expenses=0
'''for i in expenses:
  sum=sum+i
print('Total Expense is $',sum, sep='')'''
num_of_expenses=int(input('What total no of expenses?\n'))
for i in range(num_of_expenses):
    expenses.append(float(input("Enter an expense:")))
    print(expenses)
total=sum(expenses)
print("Total is $",total) 