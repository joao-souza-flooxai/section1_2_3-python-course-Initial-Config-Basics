'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se 
este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''

numero = input("Digite um número inteiro: ")

try:
    numero_inteiro = int(numero)
    isPar = numero_inteiro % 2 == 0
    print(f"O numero {numero_inteiro} é: {'par' if isPar else 'ímpar'} ")
except:
    print("Você não digitou um numero inteiro!")


'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, 
exiba a saudação apropriada. 
Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

numero = input("Digite a hora(0 <= HH <=23): ")

try:
    hora = int(numero)
    if(hora>=0 and hora<=11):
        print("Bom dia!")
    elif(hora>=12 and hora<=17):
            print("Boa tarde!")
    elif(hora>=18 and hora<=23):
            print("Boa noite!")
    else:
         print("Formato inválido.")
except:
    print("Você não digitou uma hora válida!")


'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''

'''
Aqui eu considerei  "letras" no enunciado como qualquer 
caractere para não ter que repetir a lista que fiz no aula28.py.
Mas seria a mesma ideia de chave-valor aqui.
'''

nome = input("Digite o seu nome:  ")

nome_sem_espaco = nome.strip()

if(len(nome_sem_espaco) <=4):
    print("Seu nome é curto")
elif(len(nome_sem_espaco)<=6):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")


   

