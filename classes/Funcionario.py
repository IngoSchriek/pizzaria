from classes.Cliente import Cliente
from classes.Pessoa import Pessoa


class Funcionario(Pessoa):
    @staticmethod
    def olha_comandas(contas_registradas: list[Pessoa]):
        for usuario in contas_registradas:
            if isinstance(usuario, Cliente):
                if usuario.get_comanda():
                    print("CPF do cliente: ", usuario.get_cpf())
                    print(f"Valor total: R${usuario.calcula_total_comanda():.2f}")
                else:
                    print(
                        f"Cliente {usuario.get_cpf()} nao realizou nenhum pedido ainda."
                    )

    @staticmethod
    def busca_detalhes_do_cliente(cliente: Cliente):
        print("Detalhes do cliente: ")
        print("Nome: ", cliente.get_nome())
        print("CPF: ", cliente.get_cpf())
        print("Idade: ", cliente.get_idade())
        cliente.olha_comanda()

    @staticmethod
    def busca_cliente(contas_registradas: list[Pessoa]):
        cpf_cliente = input(
            "Digite o numero de CPF do Cliente que deseja buscar o pedido: "
        )
        for usuario in contas_registradas:
            if usuario.get_cpf() == cpf_cliente:
                return usuario
        print("Pedido com o CPF digitado nao foi encontrado. ")
        return None

    def finaliza_comanda(self, cliente: Cliente) -> None:
        if cliente.get_comanda():
            self.saldo += cliente.pagar()
        else:
            print("O cliente nao fez nenhum pedido. ")
