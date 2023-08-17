# Entrada dos Dados
area=float(input("Informe quantos metros quadrado será pintado: "))

qtdLitro = float(area/6)
qtdLata = qtdLitro/18

if (qtdLitro%18 != 0):
    qtdLata=int(qtdLitro/18)+1
precoTLata= float(qtdLata*80)

galao = qtdLitro/3.6
if (qtdLitro%3.6 !=0):
    galao=int(qtdLitro/3.6)+1
precoTGalao = float (galao*25)

qtdLataMist = int(qtdLitro/18)
qtdGalaoMist = int((qtdLitro-(qtdLataMist*18))/3.6)

if qtdLitro-(qtdLata*18) %3.6 != 0:
    qtdGalaoMist+=1

# Imprimindo resultado

print ("Apenas Latas: Você precisará de {} lata(s) de 18 litros - Valor Total: R${}".format(qtdLata, precoTLata, 2))
print ("Apenas Galão: Você precisará de {} galão(ões) de 3.6 litros - Valor Total: R${}".format(galao, precoTGalao, 2))
print ("Mistura: {} Lata(s) e {} galão(ões)".format(qtdLataMist, qtdGalaoMist), " - Valor Total R${}".format((qtdLataMist*80)+(qtdGalaoMist*25)))  
