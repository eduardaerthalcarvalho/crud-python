from estado import Estado

def estado():
    est = Estado()
    
    while True:
        print("\n--- MENU ESTADO ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nCadastro de Estado")
            est.nome = input("Digite o nome do estado: ")
            est.sigla = input("Digite a sigla do estado (ex: RS): ")
            est.salvar()
            
        elif opcao == "2":
            print("\nLista de Estados:")
            estados = est.listar()
            for item in estados:
                print(f"ID: {item['id']} - Nome: {item['nome']} - Sigla: {item['sigla']}")
                
        elif opcao == "3":
            print("\nAtualizar Estado")
            est.id = int(input("Digite o ID do estado que deseja atualizar: "))
            est.nome = input("Digite o novo nome do estado: ")
            est.sigla = input("Digite a nova sigla do estado: ")
            est.atualizar()
            
        elif opcao == "4":
            print("\nExcluir Estado")
            est.id = int(input("Digite o ID do estado que deseja excluir: "))
            est.excluir()
            
        elif opcao == "0":
            print("Saindo...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")