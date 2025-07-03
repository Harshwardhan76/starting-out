import time
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()    
from random import shuffle
balls = [' ','O',' ']
def shuffled_balls(mylist):
    shuffle(mylist)
    return mylist
for i in range(1,100):

    y = shuffled_balls(balls)
    x = input('enter an index location. 0, 1 or 2 ')
    index = int(y.index('O'))
    k = int(x)
    if k==index:
        print('you got that right')
    else:
        print('the ball was placed at ', index, "\nbetter luck next time") 
    break  
time.sleep(10)        
cls()