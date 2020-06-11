from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__, static_folder='../static')

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'perfil do {username}'

@app.route('/user/id/<int:id>')
def profile_id(id):
    return f'user id {id}'

@app.route("/api/user")
def get_data():
    return app.send_static_file("user.json")
 
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Murillo'))
    print(url_for('static', filename='user.json'))