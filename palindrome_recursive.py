# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:33:50 2025

@author: 2532038
"""

def est_palindrome(chaine):
    if chaine == '':
        return True
    else:
        if chaine[0] == chaine[-1]:
            return est_palindrome(chaine[1:-1])
        else:
            return False