class Pessoa:
    def __init__(
        self, nome: str, cpf: str, idade: int, saldo: float, senha: str
    ) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo
        self.senha = senha

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_idade(self) -> int:
        return self.idade

    def get_saldo(self) -> float:
        return self.saldo

    def get_senha(self) -> str:
        return self.senha

    def set_senha(self, senha: str) -> None:
        self.senha = senha

    def set_saldo(self, saldo: float) -> None:
        self.saldo = saldo

    def add_saldo(self, valor: float) -> None:
        self.saldo += valor
