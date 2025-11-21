def affiche(positions):
    for position in positions:
        line = ['.' for _ in range(len(positions))]
        line[position] = '#'
        print(line)


def verifie(positions, col):
    if col in positions:
        return False
    
    n_line = len(positions)
    
    faux_pas = []
    for i in range(len(positions)):
        diff = n_line - i
        bad_1 = positions[i] + diff
        bad_2 = positions[i] - diff
        faux_pas.append(bad_1)
        faux_pas.append(bad_2)
    
    if col not in faux_pas:
        return True
    else:
        return False
        
count = 0
def placedame(positions):
    global count
    if len(positions) == 8:
        print(positions)
        print()
    else:
        for col in range(8):
            if verifie(positions, col):
                placedame(positions + [col])

def trouvesol():
    placedame([])
