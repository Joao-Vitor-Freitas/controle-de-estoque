print("""
    
░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░  ██████╗░███████╗
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗  ██╔══██╗██╔════╝
╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║  ██║░░██║█████╗░░
░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║  ██║░░██║██╔══╝░░
██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║  ██████╔╝███████╗
╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚══════╝

░█████╗░░█████╗░███╗░░██╗████████╗██████╗░░█████╗░██╗░░░░░███████╗  ██████╗░███████╗
██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░██████╔╝██║░░██║██║░░░░░█████╗░░  ██║░░██║█████╗░░
██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██╗██║░░██║██║░░░░░██╔══╝░░  ██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║╚█████╔╝███████╗███████╗  ██████╔╝███████╗
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝  ╚═════╝░╚══════╝

███████╗░██████╗████████╗░█████╗░░██████╗░██╗░░░██╗███████╗
██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██║░░░██║██╔════╝
█████╗░░╚█████╗░░░░██║░░░██║░░██║██║██╗██║██║░░░██║█████╗░░
██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║╚██████╔╝██║░░░██║██╔══╝░░
███████╗██████╔╝░░░██║░░░╚█████╔╝░╚═██╔═╝░╚██████╔╝███████╗
╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░░╚═════╝░╚══════╝
""")

# Lista que armazena os produtos válidos
# Cada produto será armazenado como: [codigo, nome, quantidade]
estoque = []

# Lista que armazena produtos com erro de cadastro
# Usada para manter os dados inválidos separados
erros = []


# ================================
# FUNÇÕES DE VALIDAÇÃO
# ================================

def validar_codigo(codigo):
    """
    Verifica se o código do produto é válido.
    
    Regras:
    - Deve ter pelo menos 5 dígitos
    - Deve conter apenas números
    
    Retorna:
    True  -> se válido
    False -> se inválido
    """
    return len(codigo) >= 5 and codigo.isdigit()


def validar_quantidade(qtd):
    """
    Verifica se a quantidade do produto é válida.
    
    Regras:
    - Deve ser maior ou igual a zero
    
    Retorna:
    True  -> se válido
    False -> se inválido
    """
    return qtd >= 0


# ================================
# FUNÇÃO DE CADASTRO
# ================================

def cadastrar_produto():
    """
    Responsável por coletar os dados do usuário,
    validar as informações e armazenar o produto
    na lista correta (estoque ou erros).
    """
    
    # Entrada de dados do usuário
    codigo = input("Digite o código do produto[5 dígitos]: ")
    nome = input("Digite o nome do produto: ")
    
    # Tentativa de conversão da quantidade para inteiro
    try:
        quantidade = int(input("Digite a quantidade: "))
    except:
        # Caso o usuário digite algo inválido (ex: texto)
        print("Quantidade inválida! Digite apenas números.\n")
        return  # Encerra a função

    # ================================
    # VALIDAÇÃO DOS DADOS
    # ================================

    # Se qualquer validação falhar, o produto vai para a lista de erros
    if not validar_codigo(codigo) or not validar_quantidade(quantidade):
        erros.append([codigo, nome, quantidade])
        print("Produto inválido! Enviado para lista de erros.\n")
    
    # Caso contrário, o produto é considerado válido
    else:
        estoque.append([codigo, nome, quantidade])
        print("Produto cadastrado com sucesso!\n")


# ================================
# FUNÇÃO PARA LISTAR ESTOQUE
# ================================

def listar_estoque():
    """
    Exibe todos os produtos válidos cadastrados no estoque.
    """
    
    print("\n--- ESTOQUE ---")
    
    # Percorre a lista de produtos válidos
    for produto in estoque:
        print(f"Código: {produto[0]} | Nome: {produto[1]} | Qtd: {produto[2]}")
    
    print()  # Linha em branco para organização


# ================================
# FUNÇÃO PARA LISTAR ERROS
# ================================

def listar_erros():
    """
    Exibe todos os produtos que falharam na validação.
    """
    
    print("\n--- PRODUTOS COM ERRO ---")
    
    # Percorre a lista de produtos inválidos
    for produto in erros:
        print(f"Código: {produto[0]} | Nome: {produto[1]} | Qtd: {produto[2]}")
    
    print()


# ================================
# MENU PRINCIPAL
# ================================

# Loop infinito para manter o sistema rodando
while True:
    
    # Exibição do menu de opções
    print("1 - Cadastrar produto")
    print("2 - Listar estoque")
    print("3 - Listar erros")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # ==========================
    # TRATAMENTO DAS OPÇÕES 
    # ==========================

    match opcao:
        
        case "1":
            # Chama a função de cadastro
            cadastrar_produto()
        
        case "2":
            # Exibe os produtos válidos
            listar_estoque()
        
        case "3":
            # Exibe os produtos com erro
            listar_erros()
        
        case "4":
            # Encerra o sistema
            print("Encerrando sistema...")
            break
        
        case _:
            # Caso o usuário digite qualquer valor inválido
            print("Opção inválida! Tente novamente.\n")