#WAP to find greatest of 3 numbers
def greatestNumber(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
c=int(input("Enter number3: "))
print("Greatest number=",greatestNumber(a,b,c))