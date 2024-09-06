# Atendimento ao CLiente
def menu_principal():
    # Exibe o menu de atendimento e captura a opção escolhida.
    print('Menu de atendimento, escolha uma opção:')
    opcao = input('1 - NORMAL | 2 - PREFERENCIAL | 3 - GERÊNCIA | 0 - SAIR: ')
    return opcao

def registrar_atendimento(nome, tipo):
    # Cria um dicionário para armazenar o nome do cliente e o tipo de atendimento.
    return {"nome": nome, "tipo": tipo}

def main():
    atendimentos = []  # Lista vazia para armazenar os atendimentos.
    contador_tipos = {"NORMAL": 0, "PREFERENCIAL": 0, "GERÊNCIA": 0}  # Dicionário para contar os tipos de atendimento.

    while True:
        opcao = menu_principal()  # Chama a função do menu para capturar a opção.

        if opcao == '1':
            nome_cliente = input('Digite seu nome: ')
            tipo_atendimento = "NORMAL"
            atendimentos.append(registrar_atendimento(nome_cliente, tipo_atendimento))
            contador_tipos[tipo_atendimento] += 1  # Incrementa o contador do tipo de atendimento.
            print(f'Atendimento Normal registrado, ESPERE NA FILA.')
        elif opcao == '2':
            nome_cliente = input('Digite seu nome: ')
            tipo_atendimento = "PREFERENCIAL"
            atendimentos.append(registrar_atendimento(nome_cliente, tipo_atendimento))
            contador_tipos[tipo_atendimento] += 1
            print(f'Atendimento Preferencial registrado, ESPERE NA FILA.')
        elif opcao == '3':
            nome_cliente = input('Digite seu nome: ')
            tipo_atendimento = "GERÊNCIA"
            atendimentos.append(registrar_atendimento(nome_cliente, tipo_atendimento))
            contador_tipos[tipo_atendimento] += 1
            print(f'Atendimento Gerência registrado, ESPERE NA FILA.')
        elif opcao == '0':
            # Se a opção for "0", encerra o loop principal e finaliza o programa.
            print('Encerrando o atendimento!')
            break
        else:
            print('Opção inválida! Tente novamente.')

    # Exibe um resumo de todos os atendimentos registrados.
    print('\nResumo dos Atendimentos:')
    for atendimento in atendimentos:
        print(f"Cliente: {atendimento['nome']} - Tipo de Atendimento: {atendimento['tipo']}")

    # Exibe a quantidade de atendimentos por tipo.
    print("\nQuantidade de Atendimentos por Tipo:")
    for tipo, quantidade in contador_tipos.items():
        print(f"{tipo}: {quantidade} atendimentos")

if __name__ == '__main__':
    main()