#WAP in python to  cheke courses fees in college 
A = int(input("Enter value :- "))
G = input("courses :- ")
if((A==1 or A==2) and G =="b.tech"):
    print("FEE is 60000$")
elif((A==3 or A==4) or G=="diploma"):
    print("FEE is 30000$")
elif(A==5 and G=="BCA"):
    print("FEE is 20000$")
else:
    print("not valid kye of value")