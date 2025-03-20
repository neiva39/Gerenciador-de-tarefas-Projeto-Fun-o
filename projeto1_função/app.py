
tarefas = []


def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso.")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i+1}. {tarefa['nome']} | {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")

# Função para marcar uma tarefa como concluída
def concluir_tarefa(indice):
    try:
        tarefas[indice]["concluida"] = True
        print(f"Tarefa '{tarefas[indice]['nome']}' marcada como concluída.")
    except IndexError:
        print("Índice de tarefa inválido.")

# Função para exibir tarefas por prioridade
def listar_por_prioridade(prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            print(f"{tarefa['nome']} | {tarefa['descricao']} | Categoria: {tarefa['categoria']} | Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}")
    else:
        print(f"Nenhuma tarefa com prioridade '{prioridade}' encontrada.")

# Função para exibir tarefas por categoria
def listar_por_categoria(categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["categoria"] == categoria]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            print(f"{tarefa['nome']} | {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}")
    else:
        print(f"Nenhuma tarefa na categoria '{categoria}' encontrada.")



def menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Listar tarefas por prioridade")
        print("5. Listar tarefas por categoria")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade (alta, media, baixa): ")
            categoria = input("Digite a categoria (trabalho, pessoal, estudo): ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        
        elif opcao == "2":
            listar_tarefas()
        
        elif opcao == "3":
            listar_tarefas()
            indice = int(input("Digite o número da tarefa que deseja concluir: ")) - 1
            concluir_tarefa(indice)
        
        elif opcao == "4":
            prioridade = input("Digite a prioridade (alta, media, baixa) para filtrar: ")
            listar_por_prioridade(prioridade)
        
        elif opcao == "5":
            categoria = input("Digite a categoria para filtrar: ")
            listar_por_categoria(categoria)
        
        elif opcao == "6":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Chamada do menu
menu()

