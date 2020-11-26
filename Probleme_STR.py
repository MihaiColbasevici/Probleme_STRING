prob = int(input("Dati numarul problemei: "))
if (prob == 1):
    cuv = str(input("Dati un cuvant: "))
    lit = str(input("Dati o litera: "))
    for i in cuv:
        var = cuv.replace(i, lit)
        print(var)
elif (prob == 2):
    nume, prenume = str(input("Cum va numiti? ")).split()
    if ((ord(nume[0]) >= 65) and (ord(nume[0]) <= 90)) and ((ord(prenume[0]) <= 65) and (ord(prenume[0]) >= 90)):
        print("Corect")
    else:
        print("Gresit")