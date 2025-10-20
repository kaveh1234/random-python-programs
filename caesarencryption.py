
def cesar(texte, decalage=3):
    encrypted = ""
    for ch in texte.upper():
        if "A" <= ch <= "Z":
            position = ord(ch) - ord("A")
            position = (position + decalage) % 26
            encrypted += chr(position + ord("A"))
        else:
            encrypted += ch
    return encrypted

phrase = "CECI EST UN TEST: ABCDEFGHIJKLMNOPQRSTUVWXYZ 26 LETTRES!"

print(f"Texte clair:  {phrase}")
encodage = cesar(phrase)
print(f"Texte codÃ©:   {encodage}")
decodage = cesar(encodage, -3)
print(f"Texte dÃ©codÃ©: {decodage}")

if phrase == decodage:
    print("Test reussi")
else:
    print("Test echoue")
