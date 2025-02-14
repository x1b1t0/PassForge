import random
import string
from werkzeug.security import generate_password_hash, check_password_hash

class PasswordService:
    @staticmethod
    def generate_password(length=12):
        """Genera una contraseña aleatoria de la longitud especificada."""
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    @staticmethod
    def hash_password(password):
        """Genera un hash para la contraseña proporcionada."""
        return generate_password_hash(password)

    @staticmethod
    def check_password(hash, password):
        """Verifica si una contraseña coincide con su hash."""
        return check_password_hash(hash, password)

    @staticmethod
    def validate_password(password):
        """Valida una contraseña según criterios específicos."""
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit."
        if not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter."
        if not any(char.islower() for char in password):
            return False, "Password must contain at least one lowercase letter."
        if not any(char in string.punctuation for char in password):
            return False, "Password must contain at least one special character."
        return True, "Password is valid."

# Ejemplo de uso
if __name__ == "__main__":
    password_service = PasswordService()
    
    # Generar una nueva contraseña
    new_password = password_service.generate_password()
    print(f"Generated Password: {new_password}")
    
    # Validar la nueva contraseña
    is_valid, message = password_service.validate_password(new_password)
    print(f"Password Validation: {message}")
    
    # Generar el hash de la contraseña
    hashed_password = password_service.hash_password(new_password)
    print(f"Hashed Password: {hashed_password}")
    
    # Verificar la contraseña
    is_correct = password_service.check_password(hashed_password, new_password)
    print(f"Password Check: {'Correct' if is_correct else 'Incorrect'}")