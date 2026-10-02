import pytest
from models.cardapio.itemcardapio import ItemCardapio
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida

def test_prato_e_item_cardapio():
    gerson_gameplays = Prato("cacetinho",12.99,"Cacetinho quentinho,coloca manteiga que derrete!")
    assert isinstance(gerson_gameplays, ItemCardapio)
    assert gerson_gameplays._nome == "cacetinho"
    assert gerson_gameplays._preco == 12.99
    assert gerson_gameplays.descricao == "Cacetinho quentinho,coloca manteiga que derrete!"