
# Exercício
# Pede ao usuário para digitar seu nome
# Pede ao usuário para digitar sua idade

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Se nome e idade forem digitados:
if nome and idade:
    letras_validas = [
        "a","b","c","d","e","f","g","h",
        "i","j","k","l","m","n","o","p",
        "q","r","s","t","u","v","w","x",
        "y","z","ã","ç","ó","é","í","ú"
    ]
    nome_minusculo = nome.lower()
    letras_do_nome = [letra for letra in nome_minusculo if letra in letras_validas]
    qtd_letras = len(letras_do_nome)

    nome_invertido = nome[::-1]
    nome_sem_espaco = nome.strip()
    
    primeira_letra = letras_do_nome[0] if letras_do_nome else ''
    ultima_letra = letras_do_nome[-1] if letras_do_nome else ''


    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    print(f"Seu nome contém espaços: {'sim' if ' ' in nome else 'não'}")
    print(f"Seu nome tem {qtd_letras} letras")
    print(f"A primeira letra do seu nome é {primeira_letra}")
    print(f"A última letra do seu nome é {ultima_letra}")
else:
    print("Desculpe, você deixou campos vazios.")
