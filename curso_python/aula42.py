frase = 'O Python é uma linguagem de programacao ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum. '

print(frase.count("python")) 
print(frase.count("Python"))
print(frase.lower().count("PYTHON"))
print(frase.upper().count("python"))
print(frase.count("a")) 


#Letra que mais apareceu
i = 0
qtd_letra_que_apareceu_mais = 0
letra_que_apareceu_mais = ''
frase_sem_espaco = frase.replace(" ", '').lower()
print(frase_sem_espaco)
while i<len(frase_sem_espaco):
    letra_atual = frase_sem_espaco[i]
    qtd_letra_atual = frase_sem_espaco.count(letra_atual)

    if(qtd_letra_atual > qtd_letra_que_apareceu_mais):
        qtd_letra_que_apareceu_mais =  qtd_letra_atual
        letra_que_apareceu_mais = letra_atual
    i+=1

print(f'A letra que mais apareceu foi "{letra_que_apareceu_mais}", {qtd_letra_que_apareceu_mais} vezes.')

