#ts the game of life

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 09:03:47 2025

@author: User
"""

def affiche(population, xmin=0, xmax=40, ymin=0, ymax=40):
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            print("*" if (x,y) in population else ".", end="")
        print()
        
pop_test = {(20,20), (21,20), (22,20), (20,21), (23,21), (20,22), (24,22)}

def voisines(case):
    x, y = case
    voisins = set()
    for f in range(y-1, y+2):
        for d in range(x-1, x+2):
            voisins.add((d, f))
    voisins.discard(case)
    return voisins


def nb_voisines(case, pop):
    return  len({cell for cell in pop if cell in voisines(case)})

def futurs_deces(pop):
    return {cell for cell in pop if nb_voisines(cell, pop) not in [2,3]}

def futures_naissances(pop):
    neighbours = set()
    for cell in pop:
        neighbours.update(voisines(cell))
    neighbours = neighbours - pop
    newborns = set()
    for cell in neighbours:
        if nb_voisines(cell, pop) == 3:
            newborns.add(cell)
    return newborns

def generation_suivante(pop):
    newborns = futures_naissances(pop)
    survivors = pop - futurs_deces(pop)
    return(newborns | survivors)    
    

            
        
