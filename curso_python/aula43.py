'''
senha_salva = "123456"
senha_digitada = ""
repeticoes = 9

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes -= 1

print(repeticoes)

print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'

'''
texto =  'Python'

for letra in texto:
    print(letra)