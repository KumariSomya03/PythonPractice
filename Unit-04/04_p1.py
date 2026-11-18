#WAP to find greatest of four numbers

a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
c=int(input("Enter number3: "))
d=int(input("Enter number4: "))

if(a>b and a>c and a>d):
    print("Greatest number = ",a)
elif(b>c and b>d):
    print("Greatest number = ",b)
elif(c>d):
    print("Greatest number = ",c)
else:
    print("Greatest number = ",d)
