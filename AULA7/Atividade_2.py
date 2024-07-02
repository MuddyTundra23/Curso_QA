import pandas as pd

# Dados iniciais
dados = {
    "Nome": ["Lucas", "Mariana", "Pedro", "Joana", "Rafael", "Tatiana", "Clara"],
    "Idade": [26, 34, 21, 29, 33, 38, 24],
    "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Filtragem dos dados para exibir apenas os moradores de Recife
df_recife = df[df["Cidade"] == "Recife"]

# Exibição do DataFrame filtrado
print(df_recife)