# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 15:20:14 2025

@author: User
"""

def cherche(element, liste):
    '''
    Parameters
    ----------
    element : element we  tryna find
    liste : a given list where the element might be

    Returns
    -------
    true if its in there false if not

    '''
    for item in liste:
        if type(item) == list:
            if cherche(element, item):
                return True
        else:
            if item == element:
                return True
    return False


# def cherche2(element, objet):
#     if type(object) == list:
#         for item in object:
#             if cherche(element, item):
#                 return True   
#     else:
#         return element == object
