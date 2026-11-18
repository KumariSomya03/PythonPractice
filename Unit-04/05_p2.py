#Student's marks and result
marks1=int(input("Enter marks1: "))
marks2=int(input("Enter marks2: "))
marks3=int(input("Enter marks3: "))

total_percentage=((marks1+marks2+marks3)/300)*100

if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("Pass")
else:
    print("Fail")