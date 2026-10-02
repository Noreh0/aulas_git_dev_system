from models.avaliacoes import Avaliacoes

def test_confirmar_avaliacao():
    avaliacao = Avaliacoes("Ana", 5.0)
    assert avaliacao._cliente == "Ana"
    assert avaliacao._nota == 5.0