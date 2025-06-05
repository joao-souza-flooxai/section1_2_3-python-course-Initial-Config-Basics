nome = input('Qual o seu nome? ') #por padrão o python  recebe uma string
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

#Aqui será exibido uma concatenção, pois numero_1 e numero_2 são strings
print(f'A soma dos números é: {numero_1 + numero_2}')

#Aqui será exibido uma a soma, pois numero_1 e numero_2 são agora convertidos para int
print(f'A soma dos números é: {int(numero_1) + int(numero_2)}')