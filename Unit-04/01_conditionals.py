age=int(input("Enter age: "))
if(age>=18):
    print("Eligible for voting!")
elif(age<0):
    print("Don't enter invalid age!")
else:
    print("Not eligible!")