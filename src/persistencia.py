"""
Persist User data into a file.

    Functions:
        guardar_pedido: (nombre: str, appellidos: str) -> None
"""
OUTPUT_FILE = 'prueba.txt'


def guardar_pedido(nombre: str, apellidos: str) -> None:
    """
    Stores order's user information into the file system.

        Parameters:
            nombre (str): user's name
            appellidos (str): user's surname
    """
    with open(OUTPUT_FILE, 'a', encoding='utf8') as f:
        f.write(f'-{nombre} {apellidos}\n')
        # CAVEAT: I did not include f.close() since "with"
        # is a context manager and is in charge of closing
        # the file at the end of the scope.
