nome = 'Luiz Otavio'
altura = 1.80
peso = 95

imc = peso / altura ** 2

#Formatação de string, permite escrever com variáveis e formatar as casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura' 

print(linha_1, f'pesa {peso} quilos e seu imc é {imc:.4}')