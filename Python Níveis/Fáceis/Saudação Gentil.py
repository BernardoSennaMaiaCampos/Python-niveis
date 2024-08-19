def main():
    # Solicitar o nome do usuário
    nome = input("Digite seu nome: ")

    # Solicitar o turno que o usuário estuda
    turno = input("Digite o turno que você estuda (M-matutino, V-vespertino, N-noturno): ").upper()

    # Determinar a mensagem apropriada com base no turno fornecido
    if turno == 'M':
        mensagem = f"Bom Dia, {nome}!"
    elif turno == 'V':
        mensagem = f"Boa Tarde, {nome}!"
    elif turno == 'N':
        mensagem = f"Boa Noite, {nome}!"
    else:
        mensagem = "Valor Inválido!"

    # Imprimir a mensagem
    print(mensagem)

# Executar o programa
main()
