from classes.Mercadoria import Mercadoria


class Pizza(Mercadoria):
    def __init__(
        self, nome: str, tamanho: str, valor: float, sabores: list[str]
    ) -> None:
        Mercadoria.__init__(self, nome, tamanho, valor)
        self.sabores = sabores

    def __str__(self) -> str:
        string = (
            f"{self.nome} "
            + f"\n    Tamanho: {self.tamanho} "
            + f"\n    Preco: R${self.valor:.2f} "
            + f"\n    Sabores:\n"
        )
        for sabor in self.sabores:
            string += f"    - {sabor}\n"
        return string
