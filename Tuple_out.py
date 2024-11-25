# Tuple Out
# To win Score the most points
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dice = [1,2,3,4,5,6]
dice_tuple= tuple(dice)

dice_tuple[1:4]

# random.sample[(1,2,3), 1]
def __init__(self):
    high_score = 0

def (roll_dice):
return[random.randint(dice), range (3)]

def player_turn:
    dice =
    

# code for fixed dice 

fixed_dice=[]
next_roll=[]

for roll in range(3):
    if dice.count(dice[roll])==2:
        fixed.dice.append(dice[roll])
    else:
        next_roll.append(roll)


# code to tuple out
while True:
    if dice[0]==dice[1]==dice[2]:
        print(f"You Tupled Out! Game over\n","Your score was:"{final_score})

#Roll Three dice
#If the three dice are the same number you "tupled Out"

#If two dice are the same number they are "fixed" and cant be re-rolled
#One Player Game, user must seek their high score untill they tuple out
# Game must record High Score. 
if current_score > high_score:
    high_score = current_score
    print(f"Congratulations! This is a new high score:[high_score]")
else:
    print(f"Your score was:[current_score].\n Your high score is [high_score]")
    if input ("Try Again? (y/n):").lower()!='y':
        print("Thank's for playing!") 