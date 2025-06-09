'''
    Listas em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis: append, insert, pop, del, clear, extend

'''

string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) # falsy
# print(lista, type(lista))

lista = [123, True, 'Luiz Otávio', 1.2, []] 
print(lista)
lista[2] = "João Victor"
print(lista)
del lista[4]
print(lista)
lista.append(50)
print(lista)
lista.pop()
print(lista)
lista.pop(1)
print(lista)