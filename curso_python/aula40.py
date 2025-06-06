## Calculadora com While modular(não estava na aula, mas decidi fazer).

def ler_numero(mensagem):
    while True:
        valor = input(mensagem)
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número válido.")

def ler_operador():
    operadores_permitidos = '+-/*'
    while True:
        operador = input('Digite o operador (+ - * /): ').strip()
        if operador in operadores_permitidos and len(operador) == 1:
            return operador
        print("Operador inválido.")

def deseja_sair():
    resposta = input('Quer sair? [s]im: ').strip().lower()
    return resposta.startswith('s')

def calcular(n1, n2, operador):
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '/':
        if n2 == 0:
            return 'Erro: divisão por zero.'
        return n1 / n2

# main
print("=== Calculadora Simples ===")

while True:
    num1 = ler_numero("Digite o primeiro número: ")
    num2 = ler_numero("Digite o segundo número: ")
    operador = ler_operador()

    resultado = calcular(num1, num2, operador)
    print(f'O resultado de {num1} {operador} {num2} é {resultado}')

    if deseja_sair():
        print("Encerrando a calculadora...")
        break
