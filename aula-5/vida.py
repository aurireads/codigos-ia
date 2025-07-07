from datetime import datetime

def dias_vivo(data_nascimento):
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    diferenca = hoje - nascimento
    return diferenca.days

nascimento_input = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias = dias_vivo(nascimento_input)
print(f"Você está vivo há {dias} dias.")
