from tabulate import tabulate
import re
#inicialização de variáveis
lista_produtos = []
lista_paises = []
matriz = []
mais_importacoes = 0
pais_maior_importador = ""
mais_exportacoes = 0
produto_mais_exportado = ""
cont = 0
#Mensagem de boas vindas
print("\n\033[96mBem-vindo(a) ao sistema de cadastro de exportação de produtos!\033[0m")
print("Neste sistema, você pode cadastrar produtos exportados juntamente com os países destinatários.")
print("Após cadastrar todos os produtos e países de sua escolha, você poderá inserir as quantidades exportadas para cada país.")
#cadastro de produtos
print("\nDigite abaixo o nome dos produtos que deseja adicionar ao sistema.")
print("Após digitar todos os produtos, digite 0 para avançar para próxima etapa.\n")
while not lista_produtos:
    while True:
        produto = input(f"Produto {cont+1}: ").lower()
        if re.match(r"^[a-zà-ÿ\s'-]+$", produto):
            lista_produtos.append(produto)
            cont+=1
        elif produto == "0":
            cont = 0
            break
        else:
            print(f"\n\033[91mNOME INVÁLIDO! Não podem haver números no nome do produto. Tente novamente.\033[0m\n")
    if not lista_produtos:
       print(f"\n\033[91mA lista está vazia! Adicione pelo menos um produto.\033[0m\n")
#cadastro de países        
print("\nDigite abaixo o nome dos países que deseja adicionar ao sistema.")
print("Após digitar todos os países, digite 0 para avançar para próxima etapa.\n")
while not lista_paises:
    while True:
        pais = input(f"País {cont+1}: ").lower()
        if re.match(r"^[a-zà-ÿ\s'-]+$", pais):
            lista_paises.append(pais)
            cont+=1
        elif pais == "0":
            break
        else:
            print(f"\n\033[91mPAÍS INVÁLIDO! Tente novamente.\033[0m\n")
    if not lista_paises:
        print(f"\n\033[91mA lista está vazia! Adicione pelo menos um produto.\033[0m\n")
#cadastro de quantidades de produtos exportados para cada país
print("\nDigite a quantidade de produtos que foram exportados para cada país.")
for i in range(len(lista_produtos)):
    linha = []
    for j in range(len(lista_paises)):
        while True:
            qtd_produtos = input(f"\nProduto exportado: {lista_produtos[i]}\nPaís de destino: {lista_paises[j]}\nQuantidade exportada: ")
            if qtd_produtos.isdigit():
                linha.append(qtd_produtos)
                break
            else:
                print(f"\n\033[91mQUANTIDADE INVÁLIDA! Tente novamente.\033[0m")
    matriz.append(linha)
#interface da tabela Produto / País
cabecalho = ["Produto / País"] + lista_paises
linha = []
for i, produto in enumerate(lista_produtos):
    linha.append([produto] + matriz[i])
#cadastro finalizado    
print("\n\033[92mCADASTRO FINALIZADO COM SUCESSO!\033[0m")  
#opções de pesquisa/alteração
while True:
    print("\n\033[96mEscolha uma das opções abaixo:\033[0m")
    print("Opção 1: Mostrar a tabela de exportações")
    print("Opção 2: Alterar a quantidade de produtos exportados para um país")
    print("Opção 3: Mostrar o nome do produto mais exportado, e a sua quantidade")
    print("Opção 4: Mostrar o nome do país que mais recebeu produtos, e a quantidade total enviada")
    print("Opção 0: Sair\n")
    opcao = int(input("Digite o número da opção escolhida: "))
    match opcao:
        case 0:
            break
        case 1:
            print("\n\033[96mTabela de exportações:\033[0m")
            print(tabulate(linha, headers=cabecalho, tablefmt="grid"))
        case 2:
            print("\n\033[96mTabela de exportações:\033[0m")
            print(tabulate(linha, headers=cabecalho, tablefmt="grid"))
            while True:
                pesquisa_produto = input("\nDigite o nome do produto (linhas): ").lower()
                pesquisa_pais = input("Digite o nome do país (colunas): ").lower()
                if pesquisa_produto in lista_produtos and pesquisa_pais in lista_paises:
                    while True:
                        nova_qtd = input(f"Digite a nova quantidade do produto '{pesquisa_produto}' exportado para o país '{pesquisa_pais}': ")
                        if nova_qtd.isdigit():
                            matriz[lista_produtos.index(pesquisa_produto)][lista_paises.index(pesquisa_pais)] = nova_qtd
                            linha = []
                            for i, produto in enumerate(lista_produtos):
                                linha.append([produto] + matriz[i])
                            print(f"\n\033[92mQuantidade atualizada com sucesso!\033[0m")    
                            break    
                        else:
                            print(f"\n\033[91mQUANTIDADE INVÁLIDA! Tente novamente.\033[0m\n")
                    break        
                else:
                    print("\n\033[91mPAÍS OU PRODUTO DIGITADO NÃO SE ENCONTRA NA LISTA! Tente novamente.\033[0m")
        case 3:
            for i in range(len(lista_produtos)):
                soma_exportacao = 0
                for j in range(len(lista_paises)):
                    soma_exportacao += int(matriz[i][j])
                    if soma_exportacao > mais_exportacoes:
                        mais_exportacoes = soma_exportacao
                        produto_mais_exportado = lista_produtos[i]
            print(f"\n\033[96mProduto mais exportado:\033[0m {produto_mais_exportado}")
            print(f"\033[96mQuantidade total de exportações:\033[0m {mais_exportacoes}")
        case 4:
            for j in range(len(lista_paises)):
                soma_importacao = 0
                for i in range(len(lista_produtos)):
                    soma_importacao += int(matriz[i][j])
                    if soma_importacao > mais_importacoes:
                        mais_importacoes = soma_importacao
                        pais_maior_importador = lista_paises[j]
            print(f"\n\033[96mPaís que mais recebeu produtos:\033[0m {pais_maior_importador}")
            print(f"\033[96mQuantidade total de produtos recebidos:\033[0m {mais_importacoes}")
        case _:
            print("\n\033[91mOPÇÃO INVÁLIDA! Tente novamente.\033[0m")             
#mensagem final
print("\n\033[92mNome do Desenvolvedor: VICTOR ALBERTO DOS PASSOS\033[0m\n")