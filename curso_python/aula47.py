import os

def ler_letra(mensagem):
    while True:
        letra = input(mensagem)
        if len(letra) != 1:
            print("Apenas 1 letra por vez.")
        else:
            return letra


def formar_palavra(palavra_secreta, letras_acertadas):
    palavra_formada =""
    for letra_na_palavra_secreta in palavra_secreta:
        if(letra_na_palavra_secreta in letras_acertadas):
            palavra_formada += letra_na_palavra_secreta
        else:
            palavra_formada += "*"
    return palavra_formada



palavra_secreta = "endocrino"
tentativas = 0
letras_acertadas = ""
while True:

    tentativas +=1
    letra = ler_letra("Digite uma letra: ")
    if(letra in palavra_secreta):
        letras_acertadas += letra

    palavra_formada = formar_palavra(palavra_secreta, letras_acertadas)
    print(palavra_formada)

    if("*" not in palavra_formada):
        os.system('cls')
        print(f"Você ganhou! Tentativas: {tentativas}. Palavra: {palavra_formada}")
        break
        
