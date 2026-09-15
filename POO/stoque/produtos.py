# atividade 01
class Produto:
    produtos = []
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.disponivel = False
        Produto.produtos.append(self)
    # atividade 02
    def __str__(self):
        return f"Nome do produto:{self.nome}\nPreço:{self.preco}\nDisponível:{self.disponivel}"
    # atividade 03
    def aplicar_desconto(self, desconto):
        self.desconto = desconto
        self.preco -= desconto
    # Atividade 04
    def listar_produtos():
        for produto in Produto.produtos:
            print(f"Produto:{produto.nome} |Preço:{produto.preco}")

camisa = Produto("Camisa Air Jordan", 179.99)
dunk = Produto("Tenis Dunk Low", 799.99)
bola_basquete = Produto("Bola de Basquete", 159.99)
Produto.aplicar_desconto(dunk, 199.99)
# print(camisa)
# print(dunk)
# print(bola_basquete)
Produto.listar_produtos()