# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:11:40 2025

@author: 2532038
"""

def len_iter(liste):
    count = 0
    for element in liste:
        count += 1
    return count

def len_rec(liste):
    if liste == []:
        return 0
    else:
        return 1 + len_rec(liste[1:])
    
def len_rec_2(liste, n):
    if liste[0] == liste[n]:
        return -n
    else:
        return len_rec_2()