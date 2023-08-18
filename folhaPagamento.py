# Programa que faça cálculo de uma folha de pagamento

#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%

#FGTS corresponde a 11% do Salário Bruto, mas não é descontado(a empresa paga)

#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O usuário entrará com o valor e quantidade e horas trabalhadas


# Inputs do Sistema

print ("****** Folha de Pagamento ********")
valorHora = float(input("Qual o valor da Hora: R$"))
qtdHora = float(input("Quantas Horas por mês:"))

salarioBruto = float(valorHora*qtdHora)
inss = float(salarioBruto*0.1)
fgts = float(salarioBruto*0.11)

if salarioBruto <=900:
    ir = 0
    desc = 0
elif salarioBruto >900 and salarioBruto<= 1500:
    ir = salarioBruto*0.05
    desc = 5
elif salarioBruto >1500 and salarioBruto<=2500:
    ir = salarioBruto*0.10
    desc = 10
else:
    ir = salarioBruto*0.20
    desc = 20

print ("Salário Bruto               : R$ {}".format(salarioBruto,2))
print ("(-) IR ({}%)".format(desc),"                : R$ {}".format(ir,2))
print ("(-) INSS (10%)              : R$ {}".format(inss, 2))
print ("FGTS (11%)                  : R$ {}".format(fgts, 2))
print ("Total de descontos          : R$ {}".format(ir+inss, 2))
print ("Total de Líquido            : R$ {}".format(salarioBruto-(ir+inss), 2))
