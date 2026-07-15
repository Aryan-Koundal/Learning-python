import random 
import os
number= random.randint(1,10)
guess = int (input("entre a number"))
if guess == number:
    print ("you won")
else :
    print ("you lost")