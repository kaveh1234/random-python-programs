# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:44:26 2025

@author: User
"""

def lire_mots(nom):
    with open(nom, 'r', encoding='utf8') as file:
        return file.read().splitlines()

mots = lire_mots('mots.txt')

def sont_anagrammes(mot1, mot2):
    
    list_mot1 = list(mot1)
    list_mot2 = list(mot2)
    
    mot1_set = set(list_mot1)
    mot2_set = set(list_mot2)
    
    if mot1_set == mot2_set and len(list_mot1) == len(list_mot2):
        return True
    else:
        return False

def sont_anagrammes2(liste):
    anagrammes = {}
    
    for mot in liste:
        anagramme_list = tuple(sorted(list(mot)))
        
        if anagrammes.get(anagramme_list) == None:
            anagrammes[anagramme_list] = [mot]
        else:
            anagrammes[anagramme_list].append(mot)
    return anagrammes

stuff = sont_anagrammes2(mots)


max = 0
max_key = ()
for key in stuff:
    if stuff[key] is None:
        continue
    if len(stuff[key]) > max:
        max = len(stuff[key])
        max_key = key

    
print(max)
print(stuff[max_key])

        
    


        
        
 
    
        
