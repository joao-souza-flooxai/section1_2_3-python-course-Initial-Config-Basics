'''
    Cuidados com dados mutáveis
    =copiado o valor (imutáveis)
    = aponta para o mesmo valor na memória (mutável)
   
'''
#imutáveis
nome = "João Victor"
nome_copia = nome
nome = "Alberto"

print(nome_copia)

#mutáveis
lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
print(lista_b)

lista_a = ['João', 'Maria']
lista_b = lista_a.copy()
lista_a =  ['Maria']
print(lista_b)