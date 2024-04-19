#WAP in program to check the grades of student.
marks =int(input("enter marks :-"))
if(marks==100):
    print("A++")
elif(marks>=95):
    print("A+")
elif(marks>=90):
    print("A")
elif(marks>=70):
    print("B++")
elif(marks>=50):
    print("B+")
elif(marks>=35):
    print("B")
elif(marks>=23):
    print("c")
else:
    print("fail")
