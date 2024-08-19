class COPO:
    def __init__(self, capacidade):
        if capacidade not in [250, 300, 500]:
            raise ValueError("Capacidade inválida! Escolha entre 250, 300, ou 500 ml.")
        self.capacidade = capacidade
        self.volume_atual = 0

    def Fill(self, x):
        if x < 0:
            raise ValueError("O volume para encher deve ser positivo.")
        if self.volume_atual + x > self.capacidade:
            self.volume_atual = self.capacidade
        else:
            self.volume_atual += x

    def Empty(self):
        self.volume_atual = 0

    def Status(self):
        return f'O copo tem {self.volume_atual} ml de {self.capacidade} ml.'

# Testando o código
copo = COPO(300)
print(copo.Status())  # Estado inicial
copo.Fill(100)
print(copo.Status())  # Depois de encher 100 ml
copo.Fill(250)
print(copo.Status())  # Depois de tentar encher 250 ml (deve limitar à capacidade máxima)
copo.Empty()
print(copo.Status())  # Depois de esvaziar o copo
