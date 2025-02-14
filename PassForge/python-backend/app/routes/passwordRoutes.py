from flask import Blueprint, jsonify, request
from app.controllers.passwordController import create_password

password_routes = Blueprint('password_routes', __name__)

@password_routes.route('/generate-password', methods=['POST'])
def generate_password():
    data = request.get_json()  # Obtén los datos del cuerpo de la solicitud
    password = create_password(data)  # Llama a la función que genera la contraseña
    return jsonify({"password": password}), 200  # Devuelve la contraseña generada en formato JSON
