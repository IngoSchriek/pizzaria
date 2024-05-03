class Mercadoria:
    def __init__(self, nome: str, tamanho: str, valor: float) -> None:
        self.nome = nome
        self.tamanho = tamanho
        self.valor = valor

    def get_valor(self) -> float:
        return self.valor
