from flask import request, jsonify
import jwt

# Clave secreta para firmar los tokens JWT (cámbiala por una clave segura en producción)
SECRET_KEY = 'your_secret_key'

def token_required(f):
    def decorator(*args, **kwargs):
        token = None
        # Verificar si el token está en los encabezados de la solicitud
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decodificar el token para obtener los datos del usuario
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user_id']
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401
        
        return f(current_user, *args, **kwargs)
    
    decorator.__name__ = f.__name__
    return decorator