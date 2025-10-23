
file = open("particules.txt", "r", encoding="utf-8")
lines = file.read().splitlines()
file.close()

listed = [lines[i].split() for i in range(len(lines))]


values_list = []



for sublist in listed:
    new_sublist = []
    for i in range(len(sublist)):
        if i == 1:
            new_sublist.append(sublist[i].strip("()"))


        elif i == 3:
            new_sublist.append(float(sublist[i]))
    values_list.append(new_sublist)

tuples = []
for sublist in values_list:
    pos = sublist[0].split(",")
    triplets = [float(pos[0]), float(pos[1]), sublist[1]]
    tuples.append(triplets)
print(tuples)

def calcule_e(particules):

    sum_charge = 0

    for i in range(len(particules)):
        for j in range(i+1, len(particules)):
            nom = particules[i][2] * particules[j][2] * 9
            dist = ((particules[i][0] - particules[j][0])**2 + (particules[i][1] - particules[j][1])**2)**0.5
            sum_charge += nom/dist
    return sum_charge


print(f"{calcule_e(tuples):.3f}")

