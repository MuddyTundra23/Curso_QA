class JuntofitPromo:
    def _init_(self):
        self.contagem_atual = 0
        self.consecutivas = 0
        self.participando_promo = False

    def registrar_presenca(self, presente):
        if presente:
            self.contagem_atual += 1
            self.consecutivas += 1
            if self.consecutivas == 21:
                self.participando_promo = True
                return "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ."
        else:
            self.consecutivas = 0
            if self.participando_promo:
                self.participando_promo = False
                self.contagem_atual = 0
            else:
                self.contagem_atual = 1
        
        if self.contagem_atual == 1:
            return "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
        return "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

# Exemplo de uso:
juntofit = JuntofitPromo()

# Simulação de passagem na catraca
print(juntofit.registrar_presenca(True))  # Primeira presença
print(juntofit.registrar_presenca(True))  # Segunda presença
print(juntofit.registrar_presenca(False))  # Faltou um dia
print(juntofit.registrar_presenca(True))  # Retornou após falta
print(juntofit.registrar_presenca(True))  # Mais uma presença

# Simulação de 21 presenças consecutivas
for _ in range(21):
    print(juntofit.registrar_presenca(True))

# Verificação após completar 21 presenças
print(juntofit.registrar_presenca(True))