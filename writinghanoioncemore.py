# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 15:06:18 2025

@author: User
"""

count = 0
def hanoi(n, start, end):
    global count
    if n == 1:
        count += 1
        print(f'{count}: move disc {n} from {start} to {end}')
    else:
        aux = 6 - (start + end)
        hanoi(n-1, start, aux)
        count += 1
        print(f'{count}: move disc {n} from {start} to {end}')
        hanoi(n-1, aux, end)
        
        
    
