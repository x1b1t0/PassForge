from app import create_app  # Importa la función para crear la aplicación

app = create_app()  # Crea la aplicación Flask

if __name__ == "__main__":
    app.run(debug=True)  # Inicia el servidor en modo de desarrollo
