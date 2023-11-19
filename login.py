from flask import Flask, redirect, url_for, render_template, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return 'You are not logged in.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['userid']
        user = User(user_id)
        login_user(user)
        return redirect(url_for('protected'))
    return 'login '

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
    app.run(debug=True)