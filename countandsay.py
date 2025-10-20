
n_terms = int(input("Enter the number of terms: "))

ch = "1"
for j in range(n_terms):
    print(ch)
    suiv = ""
    i = 0
    while i < len(ch):
        chiffre = ch[i]
        repetitions = 0
        while i < len(ch) and chiffre == ch[i]:
            i += 1
            repetitions += 1
        suiv += str(repetitions)
        suiv += chiffre
    ch = suiv
