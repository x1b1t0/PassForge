from flask import Flask
from app.routes import task_routes, user_routes

app = Flask(__name__)

# Configura las rutas del proyecto
app.register_blueprint(task_routes)
app.register_blueprint(user_routes)

if __name__ == "__main__":
    app.run(debug=True)

