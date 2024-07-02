import requests

# Definindo os estados das regiões Norte e Nordeste
estados_norte = ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]
estados_nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if 'erro' not in dados:
            return dados
        else:
            return None
    else:
        return None

def verificar_frete_gratis(cep):
    dados_cep = consultar_cep(cep)
    if dados_cep:
        estado = dados_cep.get('uf')
        if estado in estados_norte or estado in estados_nordeste:
            return True, dados_cep
        else:
            return False, dados_cep
    else:
        return None, None

# Pedir o CEP ao usuário
cep = input("Por favor, insira o CEP: ")

eligibilidade, dados = verificar_frete_gratis(cep)
if eligibilidade is not None:
    if eligibilidade:
        print(f"O CEP {cep} é elegível para frete grátis.")
    else:
        print(f"O CEP {cep} não é elegível para frete grátis.")
    print(dados)
else:
    print("CEP não encontrado ou inválido.")
