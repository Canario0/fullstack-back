"""
Backend Entrypoint

    Functions:
        post_order() -> BaseResponse
"""
from flask import Flask, redirect, request
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
