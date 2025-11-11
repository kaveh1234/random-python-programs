# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:06:46 2025

@author: User
"""

with open('input01.txt', 'r', encoding='utf8') as file:
    lines = file.read().splitlines()
    elves = []
    
    elf = []
    for line in lines:
        if line != '':
            elf.append(int(line))
        else:
            elves.append(elf)
            elf = []



sums = []
for elf in elves:
    somme = sum(elf)
    sums.append(somme)

print(sums)


largest = sorted(sums)
three_biggest = []
for i in range(3):
    print(largest[-1-i])   
    three_biggest.append(largest[-1-i])

print(sum(three_biggest))
    

            
            
