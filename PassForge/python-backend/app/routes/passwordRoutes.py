from flask import Blueprint, jsonify, request
from app.controllers.passwordController import generate_password

passwordRoutes = Blueprint('passwordRoutes', __name__)

@passwordRoutes.route('/generate-password', methods=['POST'])
def generate_new_password():
    # Obtener los parámetros del JSON enviado
    data = request.get_json()

    # Llamar al controlador que se encargará de la lógica de generación
    password = generate_password(data)

    # Retornar la contraseña generada como respuesta
    return jsonify({'password': password})
