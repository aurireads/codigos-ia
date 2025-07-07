def calcular_preco_com_desconto(preco_original, desconto_percentual):
    desconto = preco_original * (desconto_percentual / 100)
    preco_final = preco_original - desconto
    return round(preco_final, 2)

preco = float(input("Digite o preço original do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))
novo_preco = calcular_preco_com_desconto(preco, desconto)
print(f"Preço final com desconto: R$ {novo_preco:.2f}")
