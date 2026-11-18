# nested if-->if inside another if
age=int(input("Enter age: "))
citizen=True
if(age>=18):
    if(citizen):
        print("Eligible to vote!")

else:
    print("Not Eligible")