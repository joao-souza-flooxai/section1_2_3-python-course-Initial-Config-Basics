'''
Fatiamento de strings

     Índices
     012345678
     Olá mundo
     -987654321

     Fatiamento [i:f:p] [::]

     Obs.: a função len retorna a qtd de caracteres da str

'''

variavel = 'Ola mundo'
print(variavel[1:8])
print(variavel[-8:-1])
print(len(variavel))
print(variavel[0:9:2]) #passo
print(variavel[::2])
print(variavel[::-1])