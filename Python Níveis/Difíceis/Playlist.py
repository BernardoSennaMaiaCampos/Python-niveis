class Musica:
    def __init__(self, nome_musica, nome_cantor):
        self.nome_musica = nome_musica
        self.nome_cantor = nome_cantor

    def music(self):
        return self.nome_musica

    def singer(self):
        return self.nome_cantor

class Playlist:
    def __init__(self):
        self.lista_de_execucao = []

    def adicionar_musica(self, musica):
        self.lista_de_execucao.append(musica)

    def play(self):
        if not self.lista_de_execucao:
            print("A playlist está vazia.")
        else:
            for musica in self.lista_de_execucao:
                print(f'Tocando "{musica.music()}" de {musica.singer()}.')

# Testando o código
musica1 = Musica('Imagine', 'John Lennon')
musica2 = Musica('Bohemian Rhapsody', 'Queen')
musica3 = Musica('Hotel California', 'Eagles')

playlist = Playlist()
playlist.adicionar_musica(musica1)
playlist.adicionar_musica(musica2)
playlist.adicionar_musica(musica3)

playlist.play()
