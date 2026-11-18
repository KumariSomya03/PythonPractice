#username length <=10

username=input("Enter your username: ")
if(len(username)<10):
    print("Username must contain more than 10 characters!")
else:
    print("Username valid!")