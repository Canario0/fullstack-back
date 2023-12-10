OUTPUT_FILE = 'prueba.txt'


def guardar_pedido(nombre: str, apellidos: str) -> None:
    with open(OUTPUT_FILE, 'a', encoding='utf8') as f:
        f.write(f'{nombre} {apellidos}\n')
        # CAVEAT: I did not include f.close() since "with"
        # is a context manager and is in charge of closing
        # the file at the end of the scope.
