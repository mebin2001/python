a=int(input("enter the first value"))
b=int(input("enter the second value"))
print("the first value=",a)
print("the second value=",b)
while True: 
    print("menu")
    print("1. addition")
    print("2  subtraction")
    print("3.  multiplication")
    print("4.  division")
    print("5 exit")
    choice=int(input("enter a choice:"))
    if choice==1:
        c=a+b
        print("sum is" ,c)
    elif choice==2:
        c=a-b
        print("subtraction is",c)
    elif choice==3:
        c=a*b
        print("multiplication is",c)
    elif choice==4:
        c=a/b
        print("division is",c) 
    elif choice==5:
        break
    else: 
        print("wrong choice")         