
lista = [10, 20, 30, 40] 
lista.append('Luiz')
nome = lista.pop()
lista.append(1233) 
del lista[-1]
lista.insert(100, 5) #tenta inserir no indice 100 se nao tiver, no ultimo indice
print(lista)
lista.clear() 
print(lista)