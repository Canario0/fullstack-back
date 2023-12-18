"""
Backend Entrypoint

    Functions:
        post_order() -> BaseResponse
"""
from enum import StrEnum
from flask import Flask, Response, redirect, request
from dotenv import dotenv_values
from src import guardar_pedido

# By default it load env variables and take REDIRECT_URI
REDIRECT_URI = dotenv_values().get(
    "REDIRECT_URI") or "http://localhost/solicita_pedido.html"
app = Flask(__name__)


@app.post("/pizza")
def post_order():
    """
    HTTP controller for creating a new order

        Returns:
            BaseResponse: That redirects to the processing order page.
    """
    nombre = request.form.get("nombre", "")
    apellidos = request.form.get("apellidos", "")
    print(f'{nombre} {apellidos}')
    guardar_pedido(nombre, apellidos)
    return redirect(REDIRECT_URI, code=302)


class PizzaSizes(StrEnum):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XXL'


@app.post("/checksize")
def checksize():
    """
    HTTP controller for checking piza size availability

        Returns:
            Response: With the availability. It can be 'Disponible' or 'No disponible'.
    """
    size = request.form.get("size", "")
    if size not in PizzaSizes:
        return Response(f'"{size}" is not a valid pizza size.', 400, {'Access-Control-Allow-Origin': '*'})
    if size == PizzaSizes.SMALL:
        message = 'No disponible'
    else:
        message = 'Disponible'
    return Response(message, 200, {'Access-Control-Allow-Origin': '*'})
