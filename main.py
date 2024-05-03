from classes.Bebida import Bebida
from classes.Cliente import Cliente
from classes.Funcionario import Funcionario
from classes.Pizza import Pizza
from utils import *
from menus import *
from constants import *

contas_registradas = [
    Cliente("Enzo", "11111111111", 18, 0, pbkdf2_sha256.hash("1234")),
    Funcionario("Joao", "22222222222", 21, 0, pbkdf2_sha256.hash("1234")),
]

print(
    """
==============================
        Mario Pizzas
==============================
"""
)

usuario = None
while True:
    # Enquanto nenhuma conta foi acessada
    while not usuario:
        menu_inicial()
        opcao = input("Selecione a opcao que deseja: ")
        # Access account
        if opcao == "1":
            menu_acessar()

            cpf = input("Digite seu CPF (apenas numeros): ")
            while not valida_cpf(cpf):
                cpf = input("Digite novamente: ")

            conta_encontrada = busca_conta(cpf, contas_registradas)
            while not conta_encontrada:
                print(f"O CPF {cpf} nao possue nenhuma conta registrada")
                cpf = input("Digite seu CPF novamente: ")

            senha = input("Digite sua senha: ")
            while not valida_senha(senha, conta_encontrada.get_senha()):
                senha = input("Digite sua senha novamente: ")

            usuario = conta_encontrada

        # Cadastra conta
        elif opcao == "2":
            menu_cadastrar()

            nome = input("Digite seu nome: ")

            cpf = input("Digite seu CPF (apenas numeros): ")
            while not valida_cpf(cpf):
                cpf = input("Digite novamente: ")

            conta_encontrada = busca_conta(cpf, contas_registradas)
            while conta_encontrada:
                print(f"O CPF {cpf} ja possue conta registrada")
                cpf = input("Digite seu CPF novamente: ")
                conta_encontrada = busca_conta(cpf, contas_registradas)

            senha = input("Digite a senha (de pelo menos 4 caracteres): ")
            while not len(senha) >= 4:
                senha = input("Digite a senha novamente: ")
            hash_senha = pbkdf2_sha256.hash(senha)

            idade = int(input("Digite sua idade: "))
            while idade < 1:
                print("Idade invalida.")
                idade = int(input("Digite sua idade novamente: "))

            print("Deseja cadastrar-se como funcionario? [s/N]")
            if input("").upper() == "S":
                if idade < 18:
                    print("Idade insuficiente.")
                    continue
                nova_conta = Funcionario(nome, cpf, idade, 0, hash_senha)
            else:
                nova_conta = Cliente(nome, cpf, idade, 0, hash_senha)
            contas_registradas.append(nova_conta)

        # Nenhuma opcao selecionada
        else:
            print("Essa opcao nao existe")
            continue

    # Menu do cliente
    if isinstance(usuario, Cliente):
        cliente = usuario
        while True:
            menu_cliente(cliente.calcula_total_comanda(), cliente.get_saldo())
            cliente_escolha = input("Selecione a opcao o que deseja: ")

            # Menu do cliente - Adiciona itens na comanda
            if cliente_escolha == "1":
                cardapio()
                item_selecionado = input("Selecione o que deseja adicinar na comanda: ")

                # Pizzas
                if item_selecionado == "1":
                    menu_sabores_pizza()
                    sabores = []
                    while len(sabores) < 4:
                        sabor_opcao = input("Selecione o sabor que deseja adicinar: ")
                        if sabor_opcao in sabores_pizza:
                            sabores.append(sabores_pizza[sabor_opcao])
                        else:
                            print("Entrada invalida. ")
                            continue
                    menu_tamanhos_pizza()
                    tamanho_opcao = input("Selecione o tamanho da pizza que deseja: ")
                    while tamanho_opcao not in tamanhos_valores_pizza:
                        print("Entrada invalida. ")
                        tamanho_opcao = input(
                            "Selecione o tamanho da pizza que deseja: "
                        )
                    tamanho_valor = tamanhos_valores_pizza[tamanho_opcao]
                    mercadoria = Pizza(
                        "Pizza", tamanho_valor[0], tamanho_valor[1], sabores
                    )
                    cliente.adiciona_pedido(mercadoria)

                # Bebidas
                elif item_selecionado == "2":
                    menu_bebidas()
                    bebida_escolha = input("Selecione o bebida que deseja adicinar: ")
                    while bebida_escolha not in bebidas:
                        print("Entrada invalida. ")
                        bebida_escolha = input(
                            "Selecione o bebida que deseja adicinar: "
                        )
                    mercadoria = Bebida(*bebidas[bebida_escolha])
                    if mercadoria.is_alcoolica() and cliente.get_idade() < 18:
                        print("Idade insuficiente.")
                        continue
                    cliente.adiciona_pedido(mercadoria)

                # Nenhuma opcao selecionada
                else:
                    print("Essa opcao nao existe")
                    continue

            # Menu do cliente - Ve pedidos
            elif cliente_escolha == "2":
                cliente.olha_comanda()

            # Menu do cliente - Remove item da comanda
            elif cliente_escolha == "3":
                cliente.remove_pedido()

            # Menu do cliente - Finaliza comanda
            elif cliente_escolha == "4":
                if cliente.finaliza_comanda():
                    usuario = None
                    break

            # Menu do cliente - Adiciona saldo
            elif cliente_escolha == "5":
                cliente.adiciona_saldo()

            # Menu do cliente - Cancela comanda
            elif cliente_escolha == "6":
                cliente.cancela_comanda()
                usuario = None
                break

            # Menu do cliente - Nenhuma opcao selecionada
            else:
                print("Essa opcao nao existe")
                continue

    # Menu do Funcionario
    else:
        funcionario = usuario
        while True:
            menu_funcionario(funcionario.get_saldo())
            funcionario_escolha = input("Selecione a opcao o que deseja: ")

            # Menu do Funcionario - Olha a comanda de cada cliente
            if funcionario_escolha == "1":
                funcionario.olha_comandas(contas_registradas)

            # Menu do Funcionario - Ve detalhes da comanda de um cliente
            elif funcionario_escolha == "2":

                cliente = funcionario.busca_cliente(contas_registradas)
                if not cliente:
                    continue
                funcionario.busca_detalhes_do_cliente(cliente)

            # Menu do Funcionario - Finaliza a comanda e cobra o cliente
            elif funcionario_escolha == "3":
                cliente = funcionario.busca_cliente(contas_registradas)
                if not cliente:
                    continue
                funcionario.finaliza_comanda(cliente)

            # Menu do Funcionario - Termina expediente
            elif funcionario_escolha == "4":
                print("Expediente finalizado. ")
                usuario = None
                break
            else:
                print("Essa opcao nao existe")
