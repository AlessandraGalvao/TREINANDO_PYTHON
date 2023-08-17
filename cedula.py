# ler o valor
valor = int(input())

# imprimir o valor de entrada
print (valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    qtdnotas = int(valor/nota)
    print ("{} nota(s) de R${}".format(qtdnotas, nota))
    valor = valor%nota

    