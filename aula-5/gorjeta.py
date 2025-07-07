def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Gorjeta: R$ {gorjeta:.2f}")
