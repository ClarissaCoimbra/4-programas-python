#loja de marmitas que vende dois tipos de carne com três tamanhos diferentes
print("**************************************************************")
print("  Bem vindos à loja de Marmitas Comida Boa                    ") #Apresentação do menu de opções
print("-------------- Temos as seguintes opções: --------------------")
print("\n")
print("------------ Bife Acebolado (BA) - Pequeno: R$ 16.00 ---------")
print("------------ Bife Acebolado (BA) - Médio: R$ 18.00 -----------")
print("------------ Bife Acebolado (BA) - Grande: R$ 22.00 ----------")
print("\n")
print("------------ Filé de Frango (FF) - Pequeno: R$ 15.00 ---------")
print("------------ Filé de Frango (FF) - Médio: R$ 17.00 -----------")
print("------------ Filé de Frango (FF) - Grande: R$ 21.00 ----------")
print("**************************************************************")

def mostrar_menu(): #função para mostrar as opções do menu
    print("\n Menu de Marmitas:")
    

total = 0  #o total que acumulará os valores é iniciado em zero 

while True:
    mostrar_menu() #escolher tamanho e sabor
    

    while True: # loop infinito
        sabor = input("Escolha o sabor (BA/FF): ").upper()
        if sabor in ["BA", "FF"]:
            break
        else:
            print("Sabor inválido. Tente novamente.") #mensagem de erro caso seja digitado um código diferente de BA ou FF
    
    
    while True: #escolha de tamanho e sabor caso a opção seja válida
        tamanho = input("Escolha o tamanho (P/M/G): ").upper()
        if tamanho in ["P", "M", "G"]:
            break #se a opção estiver correta, o código para aqui, antes do else
        else:
            print("Tamanho inválido. Tente novamente.")
    
    
    if sabor == "BA": #definimos os preços em relação ao sabor e tamanho
        if tamanho == "P":
            preco = 16
        elif tamanho == "M":
            preco = 18
        elif tamanho == "G":
            preco = 22
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15
        elif tamanho == "M":
            preco = 17
        elif tamanho == "G":
            preco = 21
    
    total += preco #o total recebe o valor indicado para a variável preco, equivalente a total = total+preco
    
   
    while True:  #essa é a opção que indica a escolha de mais produtos:
        mais = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
        if mais == "S":
            break  #sai do loop de "mais produtos" para reiniciar o processo
        elif mais == "N":
            break  #sai do loop de "mais produtos" e vai para o final do loop principal
        else:
            print("Resposta inválida. Tente novamente.")
    
    if mais == "N":
        break  #sai do loop principal completamente

print(f"Valor total a pagar: R${total:.2f}") #imprime o valor da variável total, que recebeu os valores relacionados à total +=preco
