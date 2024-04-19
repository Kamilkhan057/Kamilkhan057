#WAP in program to check the grades of student.
marks = int(input("Enter the marks :-  "))
if(marks>=90):
    print("A++")
elif(marks>=80 and marks<90):
    print("A+")
elif(marks>=70 and marks<80):
    print("B+")
elif(marks>=35 and marks<70):    
    print("B")
elif(marks>=23 and marks<35):
    print("c")
else:
    print("fail")

