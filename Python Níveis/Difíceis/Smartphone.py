class Smartphone:
    def __init__(self, nome, memoria_disponivel):
        self.nome = nome
        self.memoria_disponivel = memoria_disponivel
        self.apps_instalados = []
        self.estado = 'OFF'

    def Install(self, app, tam):
        if self.estado == 'ON':
            if tam <= self.memoria_disponivel:
                self.apps_instalados.append(app)
                self.memoria_disponivel -= tam
                print(f'App {app} instalado com sucesso.')
            else:
                print('Memória insuficiente para instalar o app.')
        else:
            print('O smartphone está desligado. Não é possível instalar apps.')

    def Power(self, onOff):
        if onOff in ['ON', 'OFF']:
            self.estado = onOff
            print(f'Smartphone {self.estado}.')
        else:
            print('Comando inválido. Use "ON" ou "OFF".')

    def Lista(self):
        if self.apps_instalados:
            print('Apps instalados:', ', '.join(self.apps_instalados))
        else:
            print('Nenhum app instalado.')

# Testando o código
smartphone = Smartphone('Meu Smartphone', 500)

# Tentando instalar apps com o smartphone desligado
smartphone.Install('WhatsApp', 50)
smartphone.Lista()

# Ligando o smartphone
smartphone.Power('ON')

# Instalando apps
smartphone.Install('WhatsApp', 50)
smartphone.Lista()

smartphone.Install('Facebook', 200)
smartphone.Lista()

smartphone.Install('Instagram', 300)
smartphone.Lista()

# Tentando instalar um app que excede a memória disponível
smartphone.Install('Spotify', 300)

# Desligando o smartphone
smartphone.Power('OFF')
