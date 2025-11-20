# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:03:02 2025

@author: User
"""



count = 0
def deplace(n, origine, destination):
    global count
    
    aux = ({"A", "B", "C"} - {origine, destination}).pop()
    
    if n == 1:
        count += 1
        print(f"{count}: deplacer un disque de {origine} a {destination}")
        return
    
    deplace(n-1, origine, aux)
    count += 1
    print(f"{count}: deplacer disque {n} de {origine} a {destination}")
    deplace(n-1, aux, destination)


deplace(8, 'A', 'C')
