# 1. Criar uma lista de números de 1 a 5
numeros = list(range(1, 6))

# 2. Calcular e imprimir o quadrado de cada número usando um loop for
print("Quadrados dos números de 1 a 5:")
for numero in numeros:
    print(f"{numero}^2 = {numero**2}")

# 3. Somar todos os números na lista usando um loop while
soma = 0
i = 0
while i < len(numeros):
    soma += numeros[i]
    i += 1
print(f"Soma dos números de 1 a 5: {soma}")