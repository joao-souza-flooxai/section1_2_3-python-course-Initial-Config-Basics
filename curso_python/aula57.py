def mostrar_menu():
    print("\nMenu:")
    print("1 - Inserir item na lista")
    print("2 - Deletar item da lista")
    print("3 - Listar itens da lista")
    print("4 - Sair")

def inserir_item(lista):
    item = input("Digite o item para inserir: ")
    lista.append(item)
    print(f"'{item}' foi adicionado à lista.")

def deletar_item(lista):
    if not lista:
        print("A lista está vazia. Nada para deletar.")
        return
    try:
        index = int(input("Digite o índice do item que deseja remover: "))
        item_removido = lista.pop(index)
        print(f"Item '{item_removido}' removido com sucesso.")
    except (ValueError, IndexError):
        print("Índice inválido. Tente novamente.")

def listar_itens(lista):
    if not lista:
        print("A lista está vazia.")
    else:
        print("\nItens da lista:")
        for i, item in enumerate(lista):
            print(f"{i} - {item}")


def main():
    lista = []
    opcoes = {
        "1": inserir_item,
        "2": deletar_item,
        "3": listar_itens,
    }

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        acao = opcoes.get(escolha)
        if acao:
            if(acao != "4"):
                acao(lista)
            else:
                break;
        else:
            print("Opção inválida. Tente novamente.")

main()
