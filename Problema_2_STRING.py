sir = str(input("Dati sirul de caractere: "))
cr_maj = 0
cr_cif = 0
cr_sp = 0
for i in sir:
    if (ord(i) >= 65) and (ord(i) <= 90):
        cr_maj += 1
    elif (ord(i) >= 48) and (ord(i) <= 57):
        cr_cif += 1
    elif (ord(i) >= 40 and ord(i) <= 43) or (ord(i) >= 45 and ord(i) <= 47) or (ord(i) == 91) or (ord(i) == 93) or (ord(i) == 123) or (ord(i) == 125):
        cr_sp += 1
print(cr_maj, "caractere majuscule")
print(cr_cif, "cifre")
print(cr_sp, "caractere speciale")
