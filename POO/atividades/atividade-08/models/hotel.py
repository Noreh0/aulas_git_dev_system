from models.avaliacoes import Avaliacao

class Hotel:
    hoteis = []
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self._avaliacoes = []
        Hotel.hoteis.append(self)
    def __str__(self):
        return f"Nome do Hotel: {self.nome.ljust(25)}|Cidade: {self.cidade.ljust(25)}|Nota: {self.media_avaliacoes}"

    def receber_avaliacao(self, cliente, nota):
        avalicao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avalicao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        else:
            total_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacoes)
            quantidade_avaliacoes = len(self._avaliacoes)
            media = round(total_avaliacoes/quantidade_avaliacoes, 1)
            return media