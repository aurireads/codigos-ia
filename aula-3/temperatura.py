temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F ou K): ").upper()

def converter_temperatura(temp, origem, destino):
    if origem == destino:
        return temp

    if origem == 'F':
        temp_c = (temp - 32) * 5/9
    elif origem == 'K':
        temp_c = temp - 273.15
    else:  
        temp_c = temp

    if destino == 'F':
        return (temp_c * 9/5) + 32
    elif destino == 'K':
        return temp_c + 273.15
    else:  
        return temp_c

resultado = converter_temperatura(temperatura, unidade_origem, unidade_destino)

print(f"{temperatura}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}")
