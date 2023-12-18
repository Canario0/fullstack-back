""" Pruebas Persistencia """
from src import guardar_pedido
from src.persistencia import OUTPUT_FILE


def test_guardar_pedido():
    """ Prueba general """
    with open(OUTPUT_FILE, "w+", encoding="utf-8") as file:
        guardar_pedido("Pedro", "Gil de Diego")
        guardar_pedido("Michael", "Jordan")
        firstline = file.readline()
        secondline = file.readline()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
