from flask import Blueprint, render_template, Flask, url_for

electrodomesticos_bp = Blueprint('electrodomesticos', __name__, template_folder='templates')


@electrodomesticos_bp.route('/electrodomésticos')
def inicio_electrodomesticos():
    productos = [
    {"id": 1, "nombre": "Refrigerador Samsung", "precio": 800, "img": "RSamsung.jpg"},
    {"id": 2, "nombre": "Lavadora LG", "precio": 500, "img": "Lavadora.jpg"},
    {"id": 3, "nombre": "Microondas Panasonic", "precio": 150, "img": "Microo.jpg"},
    {"id": 4, "nombre": "Aspiradora Dyson", "precio": 350, "img": "Aspiradora.jpeg"},
    {"id": 5, "nombre": "Cafetera Nespresso", "precio": 200, "img": "Cafetera.jpg"},
    {"id": 6, "nombre": "Horno eléctrico Whirlpool", "precio": 300, "img": "Horno.jpg"},
    {"id": 7, "nombre": "Ventilador Rowenta", "precio": 100, "img": "Ventilador.jpg"},
    {"id": 8, "nombre": "Licuadora Oster", "precio": 70, "img": "Licuadora.jpg"},
    {"id": 9, "nombre": "Plancha Philips", "precio": 50, "img": "Plancha.jpeg"},
    {"id": 10, "nombre": "Tostadora Cuisinart", "precio": 80, "img": "Tostadora.jpg"}
]

    return render_template(
        'index_electrodomesticos.html',
        titulo='Inicio',
        mensaje='Esto es una lista de 10 electrodomésticos.',
        productos=productos
    )
