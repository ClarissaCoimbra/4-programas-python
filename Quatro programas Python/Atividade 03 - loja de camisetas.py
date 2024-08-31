print("╬═════════════════════════════════════════════════════════════╬")
print("           Bem-vindos à fábrica de camisetas Tudo Shirt        ")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::: Temos as seguintes opções de camisetas: :::::::::")
print("(Preço unitário) Camiseta manga curta simples (MCS) - R$1.80 ::")
print("(Preço unitário) Camiseta manga longa simples (MLS) - R$2.10 ::")
print("(Preço unitário) Camiseta manga curta com estampa (MCE) - R$2.90")
print("(Preço unitário) Camiseta manga longa com estampa (MLE) - R$3.20")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::: Essas são nossas opções de frete: :::::::::::::::::::::")
print("Frete por transportadora (1): - R$100 + valor do pedido")
print("Frete por Sedex (2): - R$200 + valor do pedido")
print("Retirada na fábrica (3): - Sem acréscimo no pedido")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("╬═══════════════════════════════════════════════════════════════╬")
print("\n")


def escolha_modelo():
    
    itens = { #pergunta o modelo desejado, usamos este dicionário para as opções
        'MCS': 1.80,
        'MLS': 2.10,
        'MCE': 2.90,
        'MLE': 3.20
    }

    while True:
        item_escolhido = input("Digite o código do item desejado (MCS, MLS, MCE, MLE): ").upper()

        if item_escolhido in itens:  # verifica se o código digitado é válido
            return itens[item_escolhido]
        else:
            print("Código inválido! Por favor, escolha entre: MCS, MLS, MCE, MLE.")


def num_camisetas():
   
    while True: #pergunta o número de camisetas everifica o que é digitado, se for algo errado ou além do limite ele permite digitar novamente o código correto
        try:
            quantidade = int(input("Digite o número de camisetas: "))

            if quantidade > 20000:  # verifica se o número de camisetas é maior que o permitido
                print("Erro! Não podemos enviar mais de 20000 camisetas por pedido.")
                continue

            
            if quantidade < 20: #desconto com base na quantidade de camisetas
                desconto = 0
            elif 20 <= quantidade < 200:
                desconto = 0.05
            elif 200 <= quantidade < 2000:
                desconto = 0.07
            else:  # 2000 <= quantidade <= 20000
                desconto = 0.12

            return quantidade, desconto

        except ValueError:
            print("Erro! Por favor, digite um número válido.")


def frete():
    
    frete_opcoes = { #pergunta pelo serviço adicional de frete e retorna o valor do frete escolhido, usamos este dicionário para as opções
        1: 100,
        2: 200,
        3: 0
    }

    while True:
        try:
            escolha_frete = int(input("Escolha uma modalidade de entrega (1 - Transportadora, 2 - Sedex, 3 - Retirada na fábrica): "))

            if escolha_frete in frete_opcoes:  # Verifica se o código do frete é válido
                return frete_opcoes[escolha_frete]
            else:
                print("Código não encontrado. Por favor, escolha entre 1, 2 ou 3.") #mensagem que mostra a opção escolhida errada
        except ValueError:
            print("Erro! Por favor, digite um número válido.")


def main(): #função principal do programa
    
    preco_item = escolha_modelo()

    resultado = num_camisetas()
    quantidade, desconto = resultado

    preco_total = preco_item * quantidade
    preco_com_desconto = preco_total * (1 - desconto)

    valor_frete = frete()

    
    total = preco_com_desconto + valor_frete #cálculo do valor total




    mensagem_final = (
        f"\n *************** Detalhes do seu pedido: **************\n"
        f" ******** Preço unitário do modelo escolhido: {preco_item} ******\n"
        f" ******** Total com desconto aplicado: {preco_com_desconto} *********\n"
        f" ******** Número de camisetas: {quantidade} ********************\n"
        f" ******** Frete escolhido: {valor_frete} ************************\n"
        f" ******** O total do pedido: R${total:.2f} *****************"
    )

    print(mensagem_final)


main() #aqui a função principal é executada
