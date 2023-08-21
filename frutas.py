# Criando uma lista de frutas
frutas =  ["laranja", "melancia", "banana", "limão", "tangerina"]
print ("Imprimindo a Lista:{}".format(frutas))

# invertendo a lista

def inverte_lista (lista):
    tamanho = len(lista)
    limite = tamanho//2
   
    for i in  range(limite):
        aux = lista[i]
        lista[i]=lista[tamanho-1]
        lista[tamanho-1]=aux


def imprime_lista(lista):
    tamanho = len(lista)
    
    for i in range(tamanho):
        print (lista[i])

    
#invertendo a lista
inverte_lista(frutas)

#imprimindo a lista inversa
print('Imprimindo Lista Invertida{}'.format(frutas));

imprime_lista(frutas)
#print ("Acrescentando um fruta depois na posição 3")
#frutas.slice(3,0, "uva")
#print('Imprimindo Lista com acrescimo{}'.format(frutas));

#frutas.reverse();

