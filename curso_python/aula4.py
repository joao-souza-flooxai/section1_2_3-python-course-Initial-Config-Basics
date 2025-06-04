
# Tipos int e float

# int -> Numero inteiro
# 0 tipo int representa qualquer numero
# positivo ou negativo. int sem sinal é considerado
# positivo.

print(11)  # int
print(-11)  # int
print(1)  # int

# float -> Numero com ponto flutuante

# 0 tipo float representa qualquer numero
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.

print(1.1, 10.11, sep=', ')
print(0.0, -1.5, sep=', ', end='\n\n')

#Função type mostra o tipo que o Python inferiu do valor
print( type('Otávio') ) #String
print( type(123) ) #int
print( type(-1.24) ) #float