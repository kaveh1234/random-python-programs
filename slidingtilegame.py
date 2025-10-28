

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
    longueur = len(jeu)
    ligne_sep = '+' + ('------+' * longueur)

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
    retourne true si la position est valide, False sinon
    """
    # Vérifier que jeu a la bonne taille
    if len(jeu) != taille: # verifie rangee
        return False

    for rangee in jeu:
        if len(rangee) != taille: # verifie que chaque rangee a taille colonnes
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
    pos_vide = position(jeu, 0) # la position vide ou la tuile se deplacera
    rangee, colonne = pos_vide

    if coup == "W":
        nouvelle_rangee, nouvelle_colonne = rangee + 1, colonne # on cherche la tuile en bas de l'espace vide (qui va devenir la nouvelle coordonnee de l'espace vide)
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
    for _ in range(nbcoups): # effectue un coup valide aleatoire nbcoups fois
        coups = coups_valides(jeu) # liste de coups valides
        coup = random.choice(coups)
        deplace(jeu, coup)



# Tâche 10: Jouer une partie
def joue(jeu):
    """
    Permet à l'utilisateur de jouer une partie
    """
    nb_coups = 0 # nombre de coups

    while not est_gagnant(jeu):
        affiche_jeu(jeu)
        print(f"Coups effectués: {nb_coups}")
        print(f"Coups valides: {', '.join(coups_valides(jeu))}")

        coups = ", ".join(coups_valides(jeu))

        coup = input(f"Entrez votre coup {coups} ou Q pour quitter: ").upper() # demande coup

        if coup == 'Q':
            print("Partie abandonnée.")
            return None

        if coup in coups_valides(jeu): # effectue coup
            deplace(jeu, coup)
            nb_coups += 1
        else:
            print("Coup invalide! Essayez à nouveau.")

    affiche_jeu(jeu)
    print(f"Félicitations! Vous avez résolu le jeu en {nb_coups} coups!") # partie gagnee


# Tâche 11: Incrémenter les séquences
def incremente_seq(liste):
    """
    Génère toutes les séquences d'un coup de plus que celles dans la liste

    Retourne la liste de séquences d'un coup de plus
    """
    coups = ["W", "A", "S", "D"] # liste de coups
    nouvelles_seq = [] # nouvelle liste avec sequences d'un coup de plus (4* longueur liste)

    for seq in liste: # attache chaque coup a chaque coup de la liste
        for coup in coups:
            nouvelles_seq.append(seq + coup)
    return nouvelles_seq


# Tâche 12: Générer toutes les séquences d'une longueur
def toutes_seq(longueur):
    """
    Génère toutes les séquences de coups d'une longueur donnée
    Retourne la liste de toutes les sequences de cette longueur
    """
    sequences = [""] # commence avec la liste de la chaine vide et non la liste vide
    for _ in range(longueur): # incremente selon la longueur
        sequences = incremente_seq(sequences) # sequences reste la sequence de longueur longueur
    return sequences


# Tâche 13: Chercher une solution de longueur donnée
def cherche(jeu, longueur):
    """
    Cherche une solution au jeu parmi les séquences d'une longueur donnée
    retourne une séquence gagnante ou None
    """
    sequences = toutes_seq(longueur) # on genere toutes les sequences de longueur longueur
    for seq in sequences:
        jeu_temp = copy.deepcopy(jeu) # on genere une copie temporaire du jeu
        if deplace_seq(jeu_temp, seq) and est_gagnant(jeu_temp): # si toutes les sequences ont ete effectuees et la position est gagnante, on retourne la sequence
            return seq
    return None


# Tâche 14: Résoudre le jeu
def resout(jeu, longueur_max):
    """
    Cherche une solution au jeu en essayant des séquences de longueur croissante
    retourne une séquence gagnante ou None
    """
    for longueur in range(1, longueur_max + 1): # on essaie avec les sequences de longueur 1 a longueur_max
        print(f"Essai de séquences de longueur {longueur}...")
        solution = cherche(jeu, longueur)
        if solution: # si solution est une liste de sequences, on la retourne (premiere sequence gagnante retrouvee)
            return solution

    return None


# Programme principal de test (decomenter pour essayer)

# print("=== Jeu de Taquin ===\n")
#
# # Créer un jeu 3x3 et le mélanger
# taquin = init_jeu(4)
# melange(taquin, 100)
# joue(taquin)


# ============================================
# Tests rapides pour les fonctions optionnelles (decomenter pour essayer)
# ============================================


# print("=== Test des fonctions optionnelles ===")

print("on teste cherche et resout avec un puzzle facile")
puzzle_test = [[1, 3, 6], [4, 2, 8], [7, 5, 0]]
affiche_jeu(puzzle_test)
solution = resout(copy.deepcopy(puzzle_test), 8)
if solution:
    print(f"  Solution trouvée: {solution}, de longueur: {len(solution)}")
    test_copie = copy.deepcopy(puzzle_test)
    deplace_seq(test_copie, solution) # on resout test_copie avec la solution
    print(f"  Résolu correctement: {est_gagnant(test_copie)}")
else:
    print("  Aucune solution trouvée")

print("=== Fin du test ===")


