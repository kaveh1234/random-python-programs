# Voici une utilisation légitime d'une variable globale:
# Les 8 sauts d'un cavalier
sauts = ((1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1))

def affiche_sol(echiquier):
    '''Affiche l'échiquier à l'écran'''
    for (r, c) in sorted(echiquier.keys()):
        if c==0 and r!=0:
            print()
            print()
        print(f"{echiquier[(r, c)]:4}", end="")
    print()
    print()
    print()

def possible(echiquier, r, c):
    '''Retourne True si (r, c) est une case vide de l'échiquier'''
    return (r, c) in echiquier.keys() and echiquier[(r, c)] == -1
    
def saute(echiquier, r, c, nb_cases):
    '''Fonction récursive qui explore le parcours du cavalier
    avec une méthode par retour arrière.
    On lui passe l'état actuel de l'échiquier, la position (r, c)
    du cavalier, et le nombre de cases visitées jusqu'à maintenant'''
    #
    # Écrivez cette fonction récursive.
    # 
    
    if nb_cases == len(echiquier):
        affiche_sol(echiquier)
        return 1
    
    else:
        total = 0
        for (dr, dc) in sauts:
            nr, nc = r + dr, c + dc
            if possible(echiquier, nr, nc):
                echiquier[(nr, nc)] = nb_cases
                total += saute(echiquier, nr, nc, nb_cases+1)
                echiquier[(nr, nc)] = -1
        return total
        
    

def parcours_cavalier(taille, r0, c0):
    '''Fonction principale. On lui donne la taille de l'échiquier et
    les coordonnées (r0, c0) initiales du cavalier. Par exemple, pour 
    trouver tous les parcours de cavalier d'un échiquier 5 x 5 qui 
    commencent au centre: parcours_cavalier(5, 2, 2)'''
    # Créer l'échiquier avec -1 dans chaque case
    echiquier = {(i, j): -1 for i in range(taille) for j in range(taille)}
    # Placer le cavalier en position initiale
    if (r0, c0) not in echiquier:
        raise ValueError("Case de départ invalide")
    echiquier[(r0, c0)] = 0
    # Appel de la fonction récursive qui compte les parcours
    total = saute(echiquier, r0, c0, 1)
    print(f"Il y a {total} solutions.")
    return total
