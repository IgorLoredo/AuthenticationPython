from flask import Flask, request, jsonify
from flask_login import current_user
from flask_login import LoginManager, UserMixin, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'key'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {}

@login_manager.user_loader
def load_user(user_id):
    if user_id not in users:
        return
    return User(user_id)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Bad Request'}), 400
    username = data['username']
    password = data['password']
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = {'password': generate_password_hash(password)}
    return jsonify({'message': 'User created'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Bad Request'}), 400
    username = data['username']
    password = data['password']

    if username in users and check_password_hash(users[username]['password'], password):
        user = User(username)
        login_user(user)
        
        return jsonify({'message': 'Logged in'}), 200
    return jsonify({'message': 'Unauthorized'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        username = current_user.id
        logout_user()
        return f"Usuário {username} deslogado com sucesso", 200
    else:
        return "Nenhum usuário está logado", 400

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)