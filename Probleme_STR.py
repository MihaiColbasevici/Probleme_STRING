prob = int(input("Dati numarul problemei: "))
if (prob == 1):
    cuv = str(input("Dati un cuvant: "))
    lit = str(input("Dati o litera: "))
    for i in range(0, len(cuv)):
        print(f'{cuv[:i]}{lit}{cuv[i + 1:]}')
elif (prob == 2):
    nume, prenume = str(input("Cum va numiti? ")).split()
    if (ord(nume[0])>=65 and ord(nume[0])<=95) and (ord(prenume[0])>=65 and ord(prenume[0])<=95):
        print("Corect")
    else:
        print("Gresit")
elif (prob == 3):
    num = str(input("Dati un numar: "))
    s = " "
    if (len(num) <= 50):
        print(num)
        for i in range(1, (len(num) // 2) + 1):
            print(s + num[i : -i]) 
            s += " "
