# Toda vez que vocês fizerem uma função para teste, ela deve conter o test_
import pytest
from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

def test_media_avaliacao_calcula_corretamente():
    restaurante = Restaurante('Coco Bambu','Frutos do Mar','Rua Açai, 123', 30)
    restaurante.receber_avaliacoes("Heron", 5.0)
    restaurante.receber_avaliacoes("Paulo", 3.0)
    assert restaurante.media_avaliacoes == 4.0

def test_adicionar_item_invalido_lanca_erro():
    restaurante = Restaurante('Casa da Vovó', 'Comida Caseira', 'Rua das Carmens, Sitio Loko',3)
    with pytest.raises(ValueError):
        restaurante.adicionar_cardapio('isso não é um item de cardápio')

def test_exibir_cardapio_restaurante_vazio_nao_quebra(capsys):
    restaurante = Restaurante('Coco Bambu','Frutos do Mar','Rua Açai, 123', 30)
    restaurante.exibir_cardapio
    saida = capsys.readouterr().out
    assert f"Cardápio do Restaurante: {restaurante.nome}" in saida