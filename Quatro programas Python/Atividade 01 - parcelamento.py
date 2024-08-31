#primeira atividade, calcular valor de parcelamento com juros 
print("******************************************************")
print("--- Bem-vindos à loja Clarissa de Oliveira Coimbra ---")
print("******************************************************")


valor_do_pedido = float(input("Digite o valor do pedido a ser parcelado:"))  # Valor do pedido em reais, usando o float caso haja um valor com centavos #valores a serem calculados
quantidade_parcelas = int(input("Digite o número de parcelas: "))  #número de parcelas que serão analisadas na estrutura if/else para o cálculo


if quantidade_parcelas < 4: #indicação de como as parcelas devem ser calculadas conforme o indicado na atividade #processamento dos dados
    juros = 0
elif quantidade_parcelas >= 4 and quantidade_parcelas < 6:
    juros = 0.04
elif quantidade_parcelas >= 6 and quantidade_parcelas < 9:
    juros = 0.08
elif quantidade_parcelas <= 9 and quantidade_parcelas < 13:
    juros = 0.16
else:
    juros = 0.32


valor_da_parcela = (valor_do_pedido * (1 + juros)) / quantidade_parcelas #calculamos o valor da parcela


valor_total_parcelado = valor_da_parcela * quantidade_parcelas #calculamos o valor total parcelado


print(f"Valor da parcela: R$ {valor_da_parcela:.2f}") #usamos o float, pois temos juros que indicarão a existência de centavos #saída de dados : valor da parcela e total parcelado
print(f"Valor total parcelado: R$ {valor_total_parcelado:.2f}") #usamos o float neste campo pelo mesmo motivo que a anterior
