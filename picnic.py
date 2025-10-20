
aliments = []

while True:
    aliment = input("Quoi apporter? ")
    if aliment != "fini":
        if aliment not in aliments:
            aliments.append(aliment)
        else:
            print("On en a deja!")
    else:
        break

print("On apporte", end=" ")
for aliment in aliments[:-1]:
    print(aliment, end=", ")
print(f"{aliments[-1]}.")
