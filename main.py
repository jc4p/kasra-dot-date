from flask import Flask, render_template, request, jsonify

from flask_misaka import Misaka as FlaskMisaka
from utils import MaterializeRenderer

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

FlaskMisaka(app, MaterializeRenderer())

@app.route('/')
def index():
    return render_template('index.html')

app.secret_key = 'SECRETS_SECRETS_ARE_NO_FUN'

if __name__ == '__main__':
    app.run(debug=True)
