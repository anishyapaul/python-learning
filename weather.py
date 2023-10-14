temperature=75
forecast='rainy'
if temperature >75:
    print("its hot")
    print('stay inside')
elif temperature < 60:
    print("its Cold")
elif temperature >=75 and forecast=='rainy':
    print('stay inside')
else:
    print('Njoy Outdoors')