from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
@app.route("/teste")
def index():
	return 'Olá Mundo!'
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'your-secret-key'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

@login_manager.user_loader
def load_user(user_id):
    if user_id not in users:
        return
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out.'

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + str(current_user.get_id())

if __name__ == "__main__":
    
    app.run(debug=True,host='0.0.0.0', port=5000)