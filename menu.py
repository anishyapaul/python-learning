menus={'Breakfast':['Egg','Sandwich','Coffee'],
       'Lunch':['Biriyani','Rice','Porotta'],
       'Dinner':['Salad','Soup']}

print('Breakfast Menu:',menus['Breakfast'])

for i in menus:
    print(i)

for i,j in menus.items():
    print(i,':',j)