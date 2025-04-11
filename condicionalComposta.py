# Conceito de IF ELIF ELSE:
# if = SE
# elif = SE NÃO
# else = OU

idade = 20

if idade < 18:
    print("você é menor de idade")
elif idade >= 18 and idade < 65:
    print("você é adulto")
else:
    print("você é idoso")

nota = float(input("Qual a sua nota?"))
if nota <= 0 or nota>=10:
    print("Erro:Nota inválida. Digite um valor entre 0 e 10.")
elif nota >=9:
    print("Aprovado")
elif nota >=7:
    print("Recuperação")
else:
    print("Reprovado")
    