new_list=['Anju','Ethan','Sony','AA','PP']

new_list.append('SS')
new_list.remove('AA')
word='Anju'

if word in new_list:
    print("Item "+word+" present")
else:
    print("Item not present "+word)
print(new_list)

for i in new_list:
    print(i)