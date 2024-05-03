from classes.Mercadoria import Mercadoria


class Bebida(Mercadoria):
    def __init__(self, nome: str, tamanho: str, valor: float, alcoolica: bool) -> None:
        Mercadoria.__init__(self, nome, tamanho, valor)
        self.alcoolica = alcoolica

    def is_alcoolica(self) -> bool:
        return self.alcoolica

    def __str__(self) -> str:
        return (
            f"{self.nome} "
            + f"\n    Tamanho: {self.tamanho} "
            + f"\n    Preco: R${self.valor:.2f} "
            + f"\n    Possue alcool: {"Sim" if self.alcoolica else "Nao"}"
        )
