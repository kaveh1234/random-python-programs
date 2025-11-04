
noms_code = {

}

employes = open("employes.txt", "r")
employees = employes.read().splitlines()
employes.close()

for person in employees:
    items = person.split(", ")
    noms_code[items[0]] = " ".join(items[2:0:-1])

print(noms_code)

hours = open("heures.txt", "r")
hours_list = hours.read().splitlines()
hours.close()

# print(hours_list)


def parse_line(line):
    hours_list2 = line.split(", ")
    nom = hours_list2[0]
    pay = float(hours_list2[1]) * float(hours_list2[2])
    return (nom, pay)  # returns a tuple

pay_employee = {

}

for line in hours_list:
    name, pay = parse_line(line)
    pay_employee[name] = pay_employee.get(name, 0) + pay

for key in noms_code:
    name = noms_code[key]
    pay = pay_employee[key]
    print(f"{name}: {pay:.2f} $")
