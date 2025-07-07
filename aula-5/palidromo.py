def eh_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())  # remove espaços e pontuação
    return texto == texto[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")
