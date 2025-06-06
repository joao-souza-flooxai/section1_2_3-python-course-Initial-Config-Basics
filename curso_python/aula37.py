
#Escopo e ordem de execução de repetições
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Nao vou mostrar o 6.')
        continue

    print(contador)

    if contador == 40:
        break