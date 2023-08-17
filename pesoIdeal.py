# ler a altura

altura = float(input("Informe com sua altura: "))
sexo = input ("Informe o seu sexo (M/F): ")

#Calculando o Peso ideal 

if (sexo == "F"):
    
    pesoIdeal = float(62.1 * altura)-44.7

else:
    
     pesoIdeal = float(72.7 * altura)-58


# impimindo o resultado
print ("O seu peso ideal é: {}".format(pesoIdeal, 2) )
