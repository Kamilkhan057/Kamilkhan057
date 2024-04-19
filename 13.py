# A =5 & G = M
# A = 2 & G =f
A = int(input("Enter value :- "))
G = input("M/f :- ")
if((A==1 or A==2) and G =="M"):
    print("FEE is 100$")
elif((A==3 or A==4) or G=="F"):
    print("FEE is 200$")
elif(A==5 and G=="M"):
    print("FEE is 300$")
else:
    print("not valid kye of value")

