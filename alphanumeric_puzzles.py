# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 08:15:50 2025

@author: User
"""
import itertools

def lettres_utilisees(liste_de_mots):
    lettres = []
    for chaine in liste_de_mots:
        for ch in chaine:
            if ch.upper() not in lettres:
                lettres.append(ch.upper())
    return lettres

def affiche_sol(nombres):
    somme = nombres[-1]
    empirical_somme = 0
    for nombre in nombres[:-1]:
        empirical_somme += nombre
    if empirical_somme != somme:
        return
    
    string_list = [str(nombre) for nombre in nombres]
    last = string_list[-1]
    addition = " + ".join(string_list[:-1])
    print(addition + " = " + last)
    
def valeur(mot, affectations):
    number = ''.join([str(affectations[ch]) for ch in mot])
    return int(number)
    
def trouve_sol(mots):
    mots_u = [mot.upper() for mot in mots]
    
    liste_lettres = lettres_utilisees(mots)
    nb_lettres = len(liste_lettres)
    if nb_lettres > 10:
        print('ya trop de lettres')
        return
    toutes_perms = itertools.permutations('0123456789', nb_lettres)
    
    for permutation in toutes_perms:
        affectations = dict(zip(liste_lettres, permutation))
        
        if any([affectations[mot[0]] == '0' for mot in mots_u]):
            continue
        
        nombres = [valeur(mot, affectations) for mot in mots_u]
        
        if sum(nombres[:-1]) == nombres[-1]:
            affiche_sol(nombres)
    
    

