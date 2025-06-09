
#enumerate - enumera iteráveis (índices)
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
lista_enumerada = enumerate(lista) #transforma em tupla
print(next(lista_enumerada))#consumiu o primeiro indice do enumerate

for item in lista_enumerada:
    a,b = item #desempacotamento 
    print(a,b) #exibe o restante da lista que está no enumerate