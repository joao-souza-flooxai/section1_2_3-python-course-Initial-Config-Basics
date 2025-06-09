
#Introdução ao desempacotamento + tuples (tuplas)

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes 
print(nome2)

produtos = ["bola", "caneta", "estojo"]
primeiro_produto, *resto = produtos

print(primeiro_produto, resto)