from constants import *


def menu(conteudo):
    print("=" * 30)
    for conteudo in conteudo:
        print(conteudo)
    print("=" * 30)


def menu_inicial():
    menu(
        [
            "1 - Acessar conta",
            "2 - Cadastrar conta",
        ]
    )


def menu_acessar():
    menu(["Acessar conta"])
    print("( Digite -1 para voltar )")


def menu_cadastrar():
    menu(["Cadastrar conta"])
    print("( Digite -1 para voltar )")


def menu_cliente(valor_total_comanda, saldo):
    menu(
        [
            "1 - Adicionar item na comanda",
            "2 - Ver itens da comanda",
            "3 - Remover item da comanda",
            "4 - Finalizar comanda",
            "5 - Adiciona saldo",
            "6 - Cancelar comanda",
            "",
            f"Valor total da comanda: R$ {valor_total_comanda:.2f}",
            f"Seu saldo: R${saldo:.2f}",
        ]
    )
    print("( Digite -1 para voltar )")


def menu_funcionario(saldo):
    menu(
        [
            "1 - Visualizar comandas",
            "2 - Mostrar itens da comanda",
            "3 - Cobrar cliente e entregar pedido",
            "4 - Terminar expediente",
            "" f"Saldo: R$ {saldo:.2f}",
        ]
    )


def menu_sabores_pizza():
    menu([f"{i} - {sabor}" for i, sabor in sabores_pizza.items()])
    print("(1/4 da pizza para cada sabor)")


def menu_tamanhos_pizza():
    menu(
        [
            f"{i} - {tamanho_valor[0]} R${tamanho_valor[1]:.2f}"
            for i, tamanho_valor in tamanhos_valores_pizza.items()
        ]
    )


def menu_bebidas():
    menu(
        [
            f"{i} - {bebida[0]} {bebida[1]} R${bebida[2]:.2f}"
            for i, bebida in bebidas.items()
        ]
    )


def cardapio():
    menu(
        [
            "1 - Pizzas",
            "2 - Bebidas",
        ]
    )
