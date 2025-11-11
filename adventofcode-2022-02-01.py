# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:23:49 2025

@author: User
"""

with open('input02.txt', 'r', encoding='utf8') as file:
    rounds = file.read().splitlines()
    
total_score = 0

weapon_score = {
    'X':1,
    'Y':2,
    'Z':3
    }

def winner(player1, player2):
    if player1 == 'X':
        if player2 =='A':
            return 3
        elif player2 == 'B':
            return 0
        elif player2 == 'C':
            return 6
    elif player1 == 'Y':
        if player2 =='A':
            return 6
        elif player2 == 'B':
            return 3
        else:
            return 0
    else:
        if player2 =='A':
            return 0
        elif player2 == 'B':
            return 6
        else:
            return 3
    
        



for round in rounds:
    round1 = round.split()
    score = 0
    score += weapon_score[round1[1]]
    score += winner(round1[1], round1[0])
    print(score)
    total_score += score

print(total_score)


    
