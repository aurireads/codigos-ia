def media_turma():
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
        if nota.lower() == 'sair':
            break
        if nota.strip() == '':
            print("Digite uma nota válida!")
            continue
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Digite uma nota válida!")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")
