class PONTO:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0

    def setX1(self, x):
        self.x1 = x

    def setY1(self, y):
        self.y1 = y

    def __str__(self):
        return f'({self.x1}, {self.y1})'

# Testando o código
ponto = PONTO()
ponto.setX1(1)
ponto.setY1(1)
print(ponto)
