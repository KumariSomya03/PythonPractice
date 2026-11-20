#Rock/Paper/Scissors
'''
import random
list1=["rock","paper","scissors"]
computer=random.choice(list1)
you=input("Choose among rock/paper/scissors: ").lower().strip()
print("Computer chose:",computer)

if(computer==you):
    print("It's a tie!")
else:
    if(computer=='rock' and you=="paper"):
        print("You won!")
    elif(computer=='rock' and you=='scissors'):
        print("You lose!")
    elif(computer=='paper' and you=='scissors'):
        print("You won!")
    elif(computer=='paper' and you=='rock'):
        print("You lose!")
    elif(computer=='scissors' and you=='paper'):
        print("You lose!")
    elif(computer=='scissors' and you=="rock"):
        print("You won!")
    else:
        print("make a valid choice!")
'''
import random
options=["rock","paper","scissors"]
win_moves={
    'rock':'scissors',
    'paper':'rock',
    'scissors':'paper'
}
computer=random.choice(options)
you=input("Choose among rock/paper/scissors: ").lower().strip()
print("Computer chose:",computer)

if you not in options:
    print("Choose correctly!")
elif computer==you:
    print("It's a tie!")
elif win_moves[you]==computer:
    print("You won!")
else:
    print("you lost!")