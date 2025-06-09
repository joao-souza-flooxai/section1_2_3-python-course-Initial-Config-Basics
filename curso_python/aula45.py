
texto = iter('Luiz') # ____iter____()
print(next(texto)) 
print(next(texto)) 
print(next(texto)) 
print(next(texto)) 

texto = 'João'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break