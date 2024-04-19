#WAP in python to check the tax on sellery.
#50000 in grater to tax 20%
#less then 50000 in tax 10%
sal = float(input("amount : ")) 
tax = sal*(0.1,0.2)[sal>50000]
print(tax)