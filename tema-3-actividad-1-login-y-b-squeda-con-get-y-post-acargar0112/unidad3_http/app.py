from flask import Flask, render_template
from login.login import login_bp
from buscar.buscar import buscar_bp
from config import Config

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(buscar_bp)
app.config.from_object(Config)

@app.route('/')
def inicio():
    return render_template('inicio.html',titulo="Inicio")

if __name__ == '__main__':
    app.run()