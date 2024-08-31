#programa que cadastra, mostra e exclui funcionários, cadastro de pessoas, setores, id e salário
def main():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(" *** Bem vindos a empresa Clarissa de Oliveira Coimbra ***")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    
    lista_funcionarios = []
    id_global = 4980518

    def cadastrar_funcionario(id):  #essa função inclui os dados do funcionário a partir da entrada de dados
        nome = input("Digite o nome do funcionário: ")
        setor = input("Digite o setor do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))

        funcionario = {  #este é um dicionário
            "id": id,
            "nome": nome,
            "setor": setor,
            "salario": salario
        }

        lista_funcionarios.append(funcionario.copy())  #essa linha indica que vamos adicionar um elemento à lista_funcionários

    def consultar_funcionarios():  #função de consulta
        while True:
            print("\nConsultar Funcionários:")
            print("1. Consultar Todos")
            print("2. Consultar por Id")
            print("3. Consultar por Setor")
            print("4. Retornar ao menu")
            opcao = int(input("Escolha uma opção(1/2/3/4): "))

            if opcao == 1:  # a condicional analisa qual a opção escolhida e pede a informação para exibir o resultado
                for funcionario in lista_funcionarios:
                    print(funcionario)
            elif opcao == 2:
                id_consulta = int(input("Digite o id do funcionário: "))
                encontrado = False
                for funcionario in lista_funcionarios:
                    if funcionario["id"] == id_consulta:
                        print(funcionario)
                        encontrado = True
                if not encontrado:
                    print("Funcionário não encontrado.")  #se o id não corresponde ao já cadastrado aparece essa informação
            elif opcao == 3:
                setor_consulta = input("Digite o setor: ")
                encontrados = [funcionario for funcionario in lista_funcionarios if funcionario["setor"] == setor_consulta]
                if encontrados:
                    for funcionario in encontrados:
                        print(funcionario)
                else:
                    print("Nenhum funcionário encontrado neste setor.")
            elif opcao == 4:
                return
            else:
                print("Opção inválida.")

    def remover_funcionario():  # função de remover funcionário
        id_remover = int(input("Digite o id do funcionário a ser removido: "))
        for funcionario in lista_funcionarios:
            if funcionario["id"] == id_remover:
                lista_funcionarios.remove(funcionario)
                print(f"Funcionário com id {id_remover} removido.")
                return
        print("Id inválido.")

    while True:  #esse loop rodará enquanto houver ações do usuário, ele é o menu principal
        print("\nMenu Principal:")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionário")
        print("3. Remover Funcionário")
        print("4. Encerrar Programa")
        opcao = int(input("Escolha uma opção(1/2/3/4): "))

        if opcao == 1:  #resultado da escolha no menu principal
            cadastrar_funcionario(id_global)
            id_global += 1  #essa variável incrementa o id para o próximo funcionário
        elif opcao == 2:
            consultar_funcionarios()
        elif opcao == 3:
            remover_funcionario()
        elif opcao == 4:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":  # o uso de __name__ é uma forma de verificar se a função main está presente e roda todo o código contido nela
    main()  # a função é executada depois que todos os parâmetros e os loops e laços são determinados
