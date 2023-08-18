# Guessing game

n = ''
guess = int(input('Enter any number'))
while n != guess:
    if(guess <= 5):
        print("Try Again!!!")
        guess = int(input('Enter any number'))
    elif(guess >= 7):
        print("Try again")
        guess = int(input("Enter any number"))
    else:
        print("you've won")
    break