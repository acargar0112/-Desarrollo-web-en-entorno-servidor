from flask import Flask, render_template, url_for
from blueprint.juegos import videojuegos_bp
from blueprint.electrodomesticos import electrodomesticos_bp

app = Flask(__name__)

app.register_blueprint(videojuegos_bp)
app.register_blueprint(electrodomesticos_bp)


@app.route('/')
def catalogo():
    return render_template(
        'catalogo.html',
        titulo='Catálogo',
    )


if __name__ == '__main__':
    app.run(debug=True)