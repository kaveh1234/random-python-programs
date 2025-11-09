
LARGEUR = 7
HAUTEUR = 7

damier = {}

def affiche_damier(damier):
    for r in range(HAUTEUR):
        for c in range(LARGEUR):
            print(damier.get((r,c), ".").center(3), end="")
        print()

def joue(damier, rangee, colonne, valeur):
    damier[(rangee, colonne)] = valeur

def retire(damier, rangee, colonne):
    damier.pop((rangee, colonne))

joueur = "X"
while True:
    affiche_damier(damier)
    commande = input(f"Joueur {joueur}, entrez rangee,colonne: ")
    if not commande:
        break
    (rang, col) = commande.split(",")
    rang = int(rang)
    col = int(col)
    joue(damier, rang, col, "X")
