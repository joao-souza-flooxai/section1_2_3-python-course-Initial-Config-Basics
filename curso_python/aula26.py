'''
Formato básico de strings:
    s - string
    d - int
    f - float

    .<número de dígitos>f
    %X - Hexadecimal
    (Caractere)(><^)(quantidade)
    > - Esquerda

    < - Direita

    ^ - Centro

    Sinal: - + ou -

    Ex.: 0 > -100, .1f

    Conversion flags - !r ou !s
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}') #preenche com 10 caracteres para a direita
print(f'{variavel:<8}.') #preenche com 10 caracteres para a esquerda
print(f'{variavel:0^10}') #preenche com 10 caracteres(0) para ao redor
