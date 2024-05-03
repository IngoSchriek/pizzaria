from passlib.hash import pbkdf2_sha256


def valida_cpf(cpf):
    if len(cpf) != 11:
        print("CPF invalido: deve conter 11 digitos")
        return False

    numero_cpf = cpf[:9]
    soma_dos_produtos1 = sum([int(x) * (10 - i) for i, x in enumerate(numero_cpf)])
    if soma_dos_produtos1 % 11 <= 1:
        digito_verificador_dezena = 0
    else:
        digito_verificador_dezena = 11 - soma_dos_produtos1 % 11

    numero_cpf = numero_cpf + str(digito_verificador_dezena)
    soma_dos_produtos2 = sum([int(x) * (11 - i) for i, x in enumerate(numero_cpf)])
    if soma_dos_produtos2 % 11 <= 1:
        digito_verificador_unidade = 0
    else:
        digito_verificador_unidade = 11 - soma_dos_produtos2 % 11

    if digito_verificador_unidade != int(cpf[-1]) or digito_verificador_dezena != int(
        cpf[-2]
    ):
        print("CPF invalido: digito verificador invalido")
        return False

    return True


def valida_senha(senha_digitada, hash_senha_esperada):
    if pbkdf2_sha256.verify(senha_digitada, hash_senha_esperada):
        return True
    return False


def busca_conta(cpf, contas):
    for conta in contas:
        if conta.get_cpf() == cpf:
            return conta

    return None
