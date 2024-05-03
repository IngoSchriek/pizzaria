from classes.Mercadoria import Mercadoria
from classes.Pessoa import Pessoa


class Cliente(Pessoa):
    comanda = []

    def get_comanda(self) -> list[Mercadoria]:
        return self.comanda

    def set_comanda(self, comanda: list[Mercadoria]) -> None:
        self.comanda = comanda

    def adiciona_pedido(self, item: Mercadoria) -> None:
        self.comanda.append(item)

    def calcula_total_comanda(self) -> float:
        return sum([x.get_valor() for x in self.comanda])

    def remove_pedido(self) -> None:
        try:
            if self.comanda:
                numero_do_item = (
                    int(input("Digite o numero do item que deseja remover: ")) - 1
                )
                self.comanda.pop(numero_do_item)
            else:
                print("Nao ha nenhum item para remover.")
        except:
            print("Entrada invalida. ")

    def finaliza_comanda(self) -> bool:
        if not self.comanda:
            print("Pedido invalido. Necessario haver uma mercadoria pelo menos.")
            return False

        valor_total_comanda = self.calcula_total_comanda()
        if self.get_saldo() < valor_total_comanda:
            print("Saldo insuficiente.")
            return False

        print("Pedido finalizado!")
        return True

    def olha_comanda(self) -> None:
        if self.comanda:
            print("Itens: ")
            for i, item in enumerate(self.comanda):
                print(str(i + 1) + " - " + str(item))
        else:
            print("Nao ha nenhum item para ver. ")

    def adiciona_saldo(self) -> None:
        try:
            self.add_saldo(float(input("Quanto deseja adicionar na conta? R$")))
        except:
            print("Entrada invalida. ")

    def cancela_comanda(self) -> None:
        self.comanda = []
        print("Pedido cancelado!")

    def pagar(self) -> float:
        valor = self.calcula_total_comanda()
        self.saldo -= valor
        self.comanda = []
        return valor
