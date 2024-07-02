def verificar_grupo(matricula):
    if matricula % 2 == 0:
        return "AZUL"
    else:
        return "AMARELO"

def separar_equipes(num_alunos):
    equipe_azul = []
    equipe_amarela = []

    for i in range(1, num_alunos + 1):
        grupo = verificar_grupo(i)
        if grupo == "AZUL":
            equipe_azul.append(i)
        else:
            equipe_amarela.append(i)
    
    return equipe_azul, equipe_amarela

# Solicitar o número de alunos do usuário
num_alunos = int(input("Digite o número de alunos: "))

# Separar os alunos em duas equipes
equipe_azul, equipe_amarela = separar_equipes(num_alunos)

# Imprimir as equipes
print("Equipe Azul:", equipe_azul)
print("Equipe Amarela:", equipe_amarela)
