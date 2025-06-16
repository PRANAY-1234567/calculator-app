a=float(input("Enter the first number"))
b=input("Enter the Operator")
c=float(input("Enter the second number"))
if b=="+":
    print(a+c)
elif b=="*":
    print (a*c)
elif b=="/":
    if c!=0:
        print(a/c)
    else:
        print("cannot divide by zero")
elif b=="-":
    print(a-c)
else:
    print("Fail")