nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(media)
if media >=9:
    print("Passou com méritos")
elif media>=8:
    print("Passou como se esperava")
else:
    print("Reprovado. Estude mais")
    