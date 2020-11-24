a, b, c, d = input("Dati 4 siruri (separate prin spatiu): ").split()
cov = ""
if (len(a) >= 3) and (len(b) >= 3) and (len(c) >= 3) and (len(d) >= 3):
    cuv = a[0 : 2] + b[0] + c[0 : 3] + d[0 : (len(d) // 2)]
    print(cuv)
else:
    print("Scrieti alte siruri.")