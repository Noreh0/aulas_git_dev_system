class Livro:
    livros = []
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._disponivel = True
        Livro.livros.append(self)
    def __str__(self):
        return f"|Titulo: {self.titulo} \n|Autor: {self.autor} \n|Ano de Lançamento: {self.ano} \n|Disponível: {self.disponibilidade}"
    @property
    def disponibilidade(self):
        return "Disponível" if self._disponivel else "Emprestado"
    def emprestar(self):
        self._disponivel = not self._disponivel
    def devolver(self):
        if self._disponivel == False:
            self._disponivel = True
        else:
            return self._disponivel
livro01 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
livro02 = Livro("Harry Potter e a pedra de crack", "J. K. Rowling", 1997)
livro03 = Livro("Caminhos dos Ratos", "Brandon Sanderson", 2019)
livro04 = Livro("O chamado de Cuturno", "H.P. Lovecraft", 1928)
Livro.emprestar(livro01)
Livro.emprestar(livro03)
Livro.devolver(livro01)
print(livro01)
print(livro02)
print(livro03)
print(livro04)