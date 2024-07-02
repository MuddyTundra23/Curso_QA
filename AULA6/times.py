def determinar_time(numero_matricula):
    if numero_matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

# Solicita ao usuário para inserir o número de matrícula
numero_matricula = int(input("Digite o número de matrícula: "))
determinar_time(numero_matricula)


