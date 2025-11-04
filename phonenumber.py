numeros = {
    "2":["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],

}

def telephone(mot):
    new_number = ""
    for char in mot:
        if char.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_number += char
        else:
            for key in numeros:
                if char.upper() in numeros[key]:
                    new_number += key
    return new_number
print(telephone("555-PYTHON7"))
