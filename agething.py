ages = {
    'Paul':53, 'Ingrid':17, 'Livia':19, 'Marc':17
}

def inverse_dict(dictionnaire):
    tuple_list = []
    for key, value in dictionnaire.items():
        tuple_list.append((key, value))
    nouv_dict = {}
    for tuple in tuple_list:
        n, a = tuple
        if a in nouv_dict:
            nouv_dict[a].append(n)
        else:
            nouv_dict[a] = [n]
    return nouv_dict

print(inverse_dict(ages))
