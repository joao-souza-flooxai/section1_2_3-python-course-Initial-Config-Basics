primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

numero_primeiro = int(primeiro_valor)
numero_segundo = int(segundo_valor)

if(numero_primeiro > numero_segundo):
    print(f'O primeiro número "{numero_primeiro}" é maior do que o segundo número "{numero_segundo}"')
elif (numero_primeiro < numero_segundo):
      print(f'O segundo número "{numero_segundo}" é maior do que o primeiro número "{numero_primeiro}"')
else:
    print(f"Os números digitados são iguais: {numero_primeiro}, {numero_segundo} ")