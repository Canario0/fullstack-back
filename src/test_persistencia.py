""" Pruebas Persistencia """
from src import guardar_pedido


def test_guardar_pedido():
    """ Prueba general """
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        guardar_pedido("Pedro", "Gil de Diego")
        guardar_pedido("Michael", "Jordan")
        firstline = file.readline()
        secondline = file.readline()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
