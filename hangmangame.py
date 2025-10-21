
import random

# La fonction suivante est fournie. Vous ne devez pas la modifier.

def dessine_bonhomme(morceaux):
    """Dessine le bonhomme pendu. Si morceaux = 0, on dessine seulement
    la potence, sinon on dessine 1) la tete, puis 2) le corps, puis 3) le 
    bras gauche, puis 4) le bras droit, puis 5) la jambe gauche, puis 6) la 
    jambe droite. Le joueur a alors perdu."""
    dessins = ["   ____\n  |    |\n  |\n  |\n  |\n__|__\n",
               "   ____\n  |    |\n  |    O\n  |\n  |\n__|__\n",
               "   ____\n  |    |\n  |    O\n  |    |\n  |\n__|__\n",
               "   ____\n  |    |\n  |    O\n  |   /|\n  |\n__|__\n",
               "   ____\n  |    |\n  |    O\n  |   /|\\\n  |\n__|__\n",
               "   ____\n  |    |\n  |    O\n  |   /|\\\n  |   /\n__|__\n",
               "   ____\n  |    |\n  |    O\n  |   /|\\\n  |   / \\\n__|__\n"]
    if 0 <= morceaux <= 6:
        print(dessins[morceaux])
    else:
        print("ARGUMENT INVALIDE")


def positions(mot, lettre):
    """Retourne l'ensemble des positions du mot où on retrouve la lettre.
    Par exemple, positions("BONJOUR", "O") retourne {1, 4}. Si la lettre
    n'est dans le mot, retourne l'ensemble vide."""
    pos = []
    compte = -1
    for i in mot:
        compte += 1
        if i == lettre:
            pos.append(compte)
    return pos


def devoile_mot(mot, lettres_connues):
    """Retourne une chaîne représentant le mot, où les lettres connues sont
    écrites comme telles mais les autres sont représentées par des soulignés."""
    
    mot_final = ''
    for i in mot:
        if i in lettres_connues:
            mot_final += (i + ' ')
        else:
            mot_final += '_ '
    length = len(mot_final) - 1
    mot_final = mot_final[:length]
    return mot_final
            


def partie_gagnee(mot, lettres):
    """Retourne True si toutes les lettres du mot sont dans l'ensemble
    utilisees, False sinon"""
    for ch in mot:
        if ch not in lettres:
            return False
    return True


def choisir_mot(nom_fichier):
    """Retourne un mot choisi au hasard dans le fichier (le fichier contient un
    mot par ligne)"""
    fichier = open(nom_fichier, "r", encoding="utf8")
    lignes = fichier.read().splitlines()
    mot = random.choice(lignes)
    return mot


def demande_nouvelle_lettre(deja_essayees):
    """Demande à l'usager d'entrer une lettre. Répète la question
    tant que l'usager n'a pas donné une lettre qui n'est pas dans
    l'ensemble déjà_essayees. Retourne la lettre majuscule."""
    while True:
        lettre = input('Entrez une lettre de A à Z: ')
        lettre = lettre.upper()
        if lettre not in deja_essayees and lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            break
        if lettre not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Not a valid lettre")
        elif lettre in deja_essayees:
            print("Letter must not be in list")
    return lettre


def joue():
    """Fonction principale qui joue une partie de bonhomme pendu"""

    print("Bienvenue au jeu du bonhomme pendu. Vous devez deviner")
    print("le mot secret en proposant des lettres. Si la lettre")
    print("n'est pas dans le mot, on ajoute un morceau au pendu.")
    print("Au sixième morceau, vous avez perdu. Bonne chance!")

    #
    # Écrivez le reste de la fonction
    #

    mot = choisir_mot("mots-pendu.txt")
    lettres_connues = []
    deja_essayees = []
    erreurs = 0

    while True:
        print("\nMot :", devoile_mot(mot, lettres_connues))
        if deja_essayees:
            print("Lettres essayées :", " ".join(sorted(deja_essayees)))
        else:
            print("Aucune lettre essayee pour l'instant")

        lettre = demande_nouvelle_lettre(deja_essayees)
        deja_essayees.append(lettre)

        idx = positions(mot, lettre)
        if idx:
            if lettre not in lettres_connues:
                lettres_connues.append(lettre)
            print(f"La lettre {lettre} apparaît {len(idx)} fois dans le mot.\n")
        else:
            erreurs += 1
            print(f"Il n'y a pas de {lettre} dans le mot.\n")

        dessine_bonhomme(erreurs)
        if partie_gagnee(mot, lettres_connues):
            print("Felicitations, vous avez trouve le mot!")
            return
        if erreurs >= 6:
            print(f"Vous avez perdu, le mot etait {mot}.")
            return

        
joue()
