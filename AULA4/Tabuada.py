def gerar_tabuada():
# Numero em string
    numero_str = input("Digite um número para ver a tabuada do 1 ao 10:")

    # Transformar a "," em "."
    numero_str = numero_str.replace(',', '.')

    # Solicita ao usuário que insira um número para a tabuada
    numero = float (numero_str)
    
    # Gera e exibe a tabuada do número fornecido
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Chama a função para gerar a tabuada
gerar_tabuada()