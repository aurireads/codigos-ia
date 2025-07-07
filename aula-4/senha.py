def verificar_senha():
    senha = input("Digite a senha: ")

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return

    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
        return

    print("Senha válida!")

verificar_senha()
