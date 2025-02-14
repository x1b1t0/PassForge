from flask import Blueprint, request, jsonify
from passwordService import PasswordService
from authMiddleware import token_required

password_bp = Blueprint('password_bp', __name__)

# Ejemplo de almacenamiento en memoria (deberías usar una base de datos en producción)
passwords = {}

@password_bp.route('/passwords', methods=['POST'])
@token_required
def create_password(current_user):
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']
    
    # Aquí puedes agregar lógica para encriptar la contraseña antes de guardarla
    passwords[user_id] = PasswordService.hash_password(password)
    return jsonify({'message': 'Password created successfully'}), 201

@password_bp.route('/passwords/<user_id>', methods=['GET'])
@token_required
def get_password(current_user, user_id):
    password = passwords.get(user_id)
    if password is None:
        return jsonify({'message': 'Password not found'}), 404
    return jsonify({'user_id': user_id, 'password': password})

@password_bp.route('/passwords/<user_id>', methods=['PUT'])
@token_required
def update_password(current_user, user_id):
    data = request.get_json()
    new_password = data['password']
    
    if user_id not in passwords:
        return jsonify({'message': 'Password not found'}), 404
    
    # Aquí puedes agregar lógica para encriptar la nueva contraseña antes de actualizarla
    passwords[user_id] = PasswordService.hash_password(new_password)
    return jsonify({'message': 'Password updated successfully'})

@password_bp.route('/passwords/<user_id>', methods=['DELETE'])
@token_required
def delete_password(current_user, user_id):
    if user_id not in passwords:
        return jsonify({'message': 'Password not found'}), 404
    
    del passwords[user_id]
    return jsonify({'message': 'Password deleted successfully'})