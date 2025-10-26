

import random
import copy


# Tâche 1: Initialiser le jeu
def init_jeu(taille):
    """
    cette fonction crée et retourne la position gagnante pour un jeu de taille (taille x taille)
    Retourne:
        Liste de listes représentant la position gagnante
    """
    jeu = []
    numero = 1
    for i in range(taille): # construire taille rangees
        rangee = []
        for j in range(taille): # dans la rangee, construire taille colonnes
            if i == taille - 1 and j == taille - 1: # si on est a la derniere rangee et la derniere colonne, on attache 0
                rangee.append(0)
            else:
                rangee.append(numero) # sinon, on attache le numero correspondant
                numero += 1
        jeu.append(rangee)
    return jeu


# Tâche 2: Afficher le jeu
def affiche_jeu(jeu):
    """
    Prend une position en argument et l'affiche avec des bordures
    """
    n = len(jeu)
    ligne_sep = '+' + ('------+' * n)

    for rangee in jeu:
        print(ligne_sep)
        ligne = '|'
        for valeur in rangee:
            if valeur == 0:
                ligne += '      |'
            # Formater le nombre avec espaces
            else:
                if valeur < 10:
                    ligne += "  " + str(valeur) + "   |"
                else:
                    ligne += " " + str(valeur) + "   |"
        print(ligne)
    print(ligne_sep)


# Tâche 3: Vérifier si une position est valide
def position_valide(jeu, taille):
    """
    Vérifie si le jeu est une position valide pour la taille donnée
    Retourne:
        True si la position est valide, False sinon
    """
    # Vérifier que jeu a la bonne taille
    if len(jeu) != taille:
        return False

    for rangee in jeu:
        if len(rangee) != taille:
            return False

    # Vérifie que tous les nombres de 0 à taille^2 - 1 sont présents une fois
    # créer une liste pour compter les occurrences, commence avec juste des 0
    compte = []
    for i in range(taille * taille):
        compte.append(0)

    # Compter chaque valeur, la liste retournee sera juste des 1 avec longueur taille*taille si la position est bonne
    for rangee in jeu:
        for valeur in rangee:
            if valeur < 0 or valeur >= taille * taille:
                return False
            compte[valeur] += 1

    # Vérifier que chaque nombre apparaît exactement une fois, si c!=1 il y a un chiffre qui apparait plus qu'une fois ou aucune fois
    for c in compte:
        if c != 1:
            return False

    return True


# Tâche 4: Trouver la position d'un nombre
def position(jeu, nombre):
    """
    Trouve la position (rangée, colonne) d'un nombre dans le jeu.
    Retourne:
        Tuple (rangée, colonne) ou None si le nombre n'est pas trouve
    """
    for i in range(len(jeu)): # parcourt rangee
        for j in range(len(jeu[i])): # parcourt colonne
            if jeu[i][j] == nombre:
                return (i, j)
    return None

# Tâche 5: Vérifier si le jeu est gagné
def est_gagnant(jeu):
    """
        Vérifie si le jeu est dans la position gagnante
        Retourne:
            True si le jeu est gagne, False sinon
        """
    longueur = len(jeu)
    numero = 1

    for i in range(longueur):
        for j in range(longueur):
            if i == longueur - 1 and j == longueur - 1:
                if jeu[i][j] != 0:
                    return False # si la derniere position n'est pas 0, retourne False
            else:
                if jeu[i][j] != numero: # si la (numero)ieme case != numero, retourne false
                    return False
                numero += 1
    return True

# Tâche 6: Trouver les coups valides
def coups_valides(jeu):
    """  retourne la liste des coups valides pour la position actuelle (liste de caractères parmi 'W', 'A', 'S', 'D') """
    pos_vide = position(jeu, 0)
    if not pos_vide: #si il n'y a pas de 0, pas de coup possible
        return []
    rangee, colonne = pos_vide
    longueur = len(jeu)
    coups = []

    if rangee < longueur - 1: # si rangee n'est pas la derniere rangee, W possible
        coups.append('W')
    if colonne < longueur - 1: # si colonne n'est pas la colonne a l'extremite droite, A possible
        coups.append('A')
    if rangee > 0: # si rangee nest pas la premiere rangee, S possible
        coups.append('S')
    if colonne > 0: # si colonne n'est pas a l'extremite gauche, D possible
        coups.append('D')

    return coups

# Tâche 7: Déplacer une tuile
def deplace(jeu, coup):
    """ effectue un coup dans le jeu si possible
        retourne:
            True si le coup a ete effectué, False sinon
    """
    coup = coup.upper() # majuscule
    if coup not in coups_valides(jeu): # coup doit etre dans coups valides
        return False
    pos_vide = position(jeu, 0)
    rangee, colonne = pos_vide

    if coup == "W":
        nouvelle_rangee, nouvelle_colonne = rangee + 1, colonne # on cherche la tuile en bas de l'espace vide
    elif coup =="A":
        nouvelle_rangee, nouvelle_colonne = rangee, colonne + 1 # on cherche la tuile a droite de l'espace vide
    elif coup == "S":
        nouvelle_rangee, nouvelle_colonne = rangee - 1, colonne # on cherche la tuile en haut de l'espace vide
    elif coup == "D":
        nouvelle_rangee, nouvelle_colonne =  rangee, colonne - 1 # on cherche la tuile a gauche de l'espace vide

    # on echange les valeurs
    jeu[rangee][colonne] = jeu[nouvelle_rangee][nouvelle_colonne] # on met la tuile qu'on a cherche dans l'espace vide (mutabilite!)
    jeu[nouvelle_rangee][nouvelle_colonne] = 0 # l'espace precedent de la tuile est maintenant l'espace vide

    return True


# Tâche 8: Déplacer selon une séquence
def deplace_seq(jeu, sequence):
    """
    effectue une sequence de coups dans le jeu si possible
    retourne:
        True si tous les coups ont ete effectues, False sinon
    """
    # Créer une copie (deepcopy) pour tester la séquence (on veut savoir si la sequence est valide avant de changer le jeu, car mutabilite)
    jeu_temp = copy.deepcopy(jeu)

    for coup in sequence:
        if not deplace(jeu_temp, coup): # si on a un coup qui ne fonctionne pas, retourne false
            return False
    # si tous les coups sont valides, on peut les appliquer a l'original
    for coup in sequence:
        deplace(jeu, coup)
    return True


# Tâche 9: Mélanger le jeu
def melange(jeu, nbcoups):
    """melange le jeu en effectuant un nombre donne de coups aleatoires
    """
    for _ in range(nbcoups): #nb de coups
        coups = coups_valides(jeu) # coups valides
        if coups:
            coup = random.choice(coups) # coup random parmi coups valides
            deplace(jeu, coup)


# Tâche 10: Jouer une partie
def joue(jeu):
    """
    Permet à l'utilisateur de jouer une partie
    """
    nb_coups = 0 # nombre de coups

    while not est_gagnant(jeu):
        affiche_jeu(jeu)
        print(f"\nCoups effectués: {nb_coups}")
        print(f"Coups valides: {', '.join(coups_valides(jeu))}")

        coup = input("Entrez votre coup (W/A/S/D) ou Q pour quitter: ").upper() # demande coup

        if coup == 'Q':
            print("Partie abandonnée.")
            return

        if coup in coups_valides(jeu): # effectue coup
            deplace(jeu, coup)
            nb_coups += 1
        else:
            print("Coup invalide! Essayez à nouveau.")

    affiche_jeu(jeu)
    print(f"\nFélicitations! Vous avez résolu le jeu en {nb_coups} coups!") # partie gagnee

# Programme principal de test
print("=== Jeu de Taquin ===\n")

# Créer un jeu 3x3 et le mélanger
taquin = init_jeu(3)
melange(taquin, 100)
joue(taquin)


