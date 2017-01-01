from flask import Flask, render_template, request, jsonify, send_from_directory

from flask_misaka import Misaka as FlaskMisaka
from utils import MaterializeRenderer

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

FlaskMisaka(app, MaterializeRenderer())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon-96x96.png', mimetype='image/vnd.microsoft.icon')

app.secret_key = 'SECRETS_SECRETS_ARE_NO_FUN'

if __name__ == '__main__':
    app.run(debug=True)
