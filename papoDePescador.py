#Ler a entrada
pesoPeixes = float(input ("Insira o Peso Total de Peixe: "))

# Medições

if (pesoPeixes>50):
    excesso = float(pesoPeixes-50)
    multa = float(excesso*4)
    print ("Você excedeu o limite de 50 kg. O seu excesso foi de {}kg e sua multa é de R${}".format(excesso, multa,2))
else:
    print ("Você não excedeu o limite de 50kg de peixe")



