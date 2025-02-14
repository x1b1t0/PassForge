from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Fragmenttask API!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Placeholder for getting tasks
    tasks = []
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    # Placeholder for creating a new task
    task = request.json
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True)