weight=int(input("enter your weight:\n"))
unit=input("weight in Kg or Lb?\n")
if unit.upper()=='LB':
    lb_kg = weight/2.204623
    print("Lb to Kg is",str(lb_kg))
elif unit.upper()=='KG':
    lb_kg = weight * 2.204623
    print("Kg to Lb is",str(lb_kg))