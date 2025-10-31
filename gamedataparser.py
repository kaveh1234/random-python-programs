
games = open("nhl1966-67.txt", "r")
parties = games.readlines()

equipes = {
    "Montreal":0,
    "Boston":0,
    "Detroit":0,
    "NewYork":0,
    "Chicago":0,
    "Toronto":0
}

def gagnants(equipe1_tuple, equipe2_tuple):
    equipe1, but1 = equipe1_tuple
    equipe2, but2 = equipe2_tuple
    but1 = int(but1)
    but2 = int(but2)

    if but1 > but2:
        return equipe1
    elif but1 < but2:
        return equipe2
    else:
        return 1

def ajoute_points(ligne):
    ligne_split = ligne.split()

    equipe1_tuple = (ligne_split[1], ligne_split[2])
    equipe2_tuple = (ligne_split[3], ligne_split[4])

    gagnant = gagnants(equipe1_tuple, equipe2_tuple)

    if gagnant == 1:
        equipes[equipe1_tuple[0]] += 1
        equipes[equipe2_tuple[0]] += 1
    elif gagnant == equipe1_tuple[0]:
        equipes[equipe1_tuple[0]] += 2
    elif gagnant == equipe2_tuple[0]:
        equipes[equipe2_tuple[0]] += 2

def saison_points(saison):
    for match in saison:
        ajoute_points(match)

saison_points(parties)

print(equipes)
