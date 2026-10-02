class Filme:
    filmes = []
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        Filme.filmes.append(self)
    @classmethod
    def listar_filmes(cls):
        print(f"{'Titulo'.ljust(27)}|{'Genêro'.ljust(27)}|{'Ano de Lançamento'.ljust(27)}")
        for filme in cls.filmes:
            print(f"{filme.titulo.ljust(27)}|{filme.genero.ljust(27)}|{str(filme.ano).ljust(27)}")

filme01 = Filme("Titanico", "Romance e Drama", 1997)
filme02 = Filme("Invocação do Melman", "Terror", 2013)
filme03 = Filme("As belas carecas", "Comédia", 2004)
filme04 = Filme("Até o último homenino", "Ação", 2016)
filme05 = Filme("O pijama do menino Listrado", "Romance e Drama", 2008)

Filme.listar_filmes()