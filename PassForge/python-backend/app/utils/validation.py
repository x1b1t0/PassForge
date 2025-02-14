import re

class Validation:
    @staticmethod
    def validate_email(email):
        """Valida si el correo electrónico proporcionado tiene un formato válido."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, email):
            return True, "Email is valid."
        return False, "Invalid email format."

    @staticmethod
    def validate_username(username):
        """Valida si el nombre de usuario proporcionado tiene un formato válido."""
        username_regex = r'^[a-zA-Z0-9._-]{3,20}$'
        if re.match(username_regex, username):
            return True, "Username is valid."
        return False, "Username must be 3-20 characters long and can only contain letters, numbers, dots, underscores, and hyphens."

    @staticmethod
    def validate_password(password):
        """Valida si la contraseña proporcionada cumple con los criterios de seguridad."""
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit."
        if not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter."
        if not any(char.islower() for char in password):
            return False, "Password must contain at least one lowercase letter."
        if not any(char in re.escape('!@#$%^&*()-_=+[]{}|;:,.<>?/`~') for char in password):
            return False, "Password must contain at least one special character."
        return True, "Password is valid."

# Ejemplo de uso
if __name__ == "__main__":
    validation = Validation()
    
    # Validar un correo electrónico
    email = "test@example.com"
    is_valid, message = validation.validate_email(email)
    print(f"Email Validation: {message}")
    
    # Validar un nombre de usuario
    username = "user_name"
    is_valid, message = validation.validate_username(username)
    print(f"Username Validation: {message}")
    
    # Validar una contraseña
    password = "Password123!"
    is_valid, message = validation.validate_password(password)
    print(f"Password Validation: {message}")