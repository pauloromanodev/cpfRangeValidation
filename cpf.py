def validar_cpf(cpf):
    cpf = str(cpf).zfill(11)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11
    resto = 0 if resto == 10 else resto
    if resto != int(cpf[9]):
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = (soma * 10) % 11
    resto = 0 if resto == 10 else resto
    if resto != int(cpf[10]):
        return False

    return True

def validar_faixa_cpf(inicio, fim):
    cpfs_validos = []
    cpfs_invalidos = []

    for cpf in range(inicio, fim + 1):
        if validar_cpf(cpf):
            cpfs_validos.append(str(cpf).zfill(11))
        else:
            cpfs_invalidos.append(str(cpf).zfill(11))

    return cpfs_validos, cpfs_invalidos

def obter_entrada_usuario():
    try:
        inicio_cpf = int(input("Digite a sequência inicial do CPF: "))
        fim_cpf = int(input("Digite a sequência final do CPF: "))
        if inicio_cpf > fim_cpf:
            print("A sequência inicial deve ser menor ou igual à sequência final.")
            return None, None
        return inicio_cpf, fim_cpf
    except ValueError:
        print("Por favor, insira números válidos.")
        return None, None

# Script principal
inicio_cpf, fim_cpf = obter_entrada_usuario()
if inicio_cpf is not None and fim_cpf is not None:
    cpfs_validos, cpfs_invalidos = validar_faixa_cpf(inicio_cpf, fim_cpf)
    print('CPFs válidos:', len(cpfs_validos))
    print('Lista de CPFs válidos:', cpfs_validos)
    print('CPFs inválidos:', len(cpfs_invalidos))
else:
    print("Entrada inválida, encerrando o programa.")
