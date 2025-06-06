'''
while (condição):
    enquanto essa condição for verdadeira

'''

condicao = True

while condicao:
    digito = input('Se quiser sair, digite "sair"')
    if(digito=='sair'):
        break
    print(f"Voce digitou: {digito}")




#Loop infinito porque a condição nunca é mudada(sempre True)
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Você está em um loop infinito! Mas aqui está o seu nome: {nome}')

