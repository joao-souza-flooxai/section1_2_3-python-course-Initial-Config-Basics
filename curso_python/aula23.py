# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
if senha != "123456":
    print('Senha incorreta.')
print(not True)
print(not False)