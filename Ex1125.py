n1 = float(input())
n2 = float(input())
media = (n1 + n2) / 2

if media >= 6:
    print("aprovado")
elif media < 6 and n1 >= 2:
    print("talvez com a sub")
else:
    print("reprovado")