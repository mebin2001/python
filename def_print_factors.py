def factor(x):
    print("The factor of",x+1)
    for i in range(1,x+1):
        if x % i==0:
            print(i)
n=int(input("Enter a number:"))
factor(n)            