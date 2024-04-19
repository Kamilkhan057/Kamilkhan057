#WAP in python programming language in check the age  under avilabal for voting or not.
age = int(input("enter the age :-"))
if(age>=60):
    print("not this avilabal for voting")
elif (age>18):
    print("valid for voting")
elif(age<17):
    print("not valid for voting")
else:
    print("not valid")