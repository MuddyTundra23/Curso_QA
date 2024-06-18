idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Indivíduo possui idade mínima para dirigir.")
elif 17 >= idade and idade <= 18:
    print("Indivíduo tem ente 17 e 18 e ainda NÃO é apto para dirigir.")
else:
    print("Indivíduo NÃO possui idade mínima para dirigir.")