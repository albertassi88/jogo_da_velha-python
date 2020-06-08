def erro():
    try:
        numero = int(input('Escolhe um número da tabela.'))
    except ValueError:
        letra = input('Opção Inválida! Escolhe um número da tabela novamente.')
        while not letra.isdigit():
            letra = input('Opção Inválida! Escolhe um número da tabela novamente.')
        numero = int(letra)
    return numero


