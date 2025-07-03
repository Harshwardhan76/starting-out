import os
import time
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
print("Welcome to the Guessing Game!\nI have selected a random number between 1 and 100. You have to guess it.\nYou have 100 guesses.\nYou will be given hints based on your guesses.\nIf your guess is within 10 of the number, you will be told 'warm'.\nIf it is more than 10 away, you will be told 'cold'.\nIf you guess correctly, you will be congratulated and the game will end.")
print('If you get closer to the number than your previous guess, you will be told "warmer", otherwise "colder".\nLet\'s start!')
import random
x = random.randint(1,100)
your_guess = []
dist = []
for i in range(1,101):
    y= int(input("Enter your guess: "))
    your_guess.append(y)
    dist.append(abs(x-y))
    if i == 1:
        if dist[-1] <= 10:
            print('warm')
        else:
            print('cold')
        continue
    elif y == x:
        print('You got it! the number is indeed', x)
        break
    elif y>100 or y<1:
        print('Out of range! Please guess a number between 1 and 100.')
        your_guess.pop()  
    elif dist[-1] > dist[-2]:
        print('colder')
    elif dist[-1] < dist[-2]:
        print('warmer') 
  
print('these are your valid guesses:', your_guess)     
time.sleep(10)
cls()