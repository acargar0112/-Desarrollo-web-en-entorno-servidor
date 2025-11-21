from flask import Blueprint, render_template, Flask, url_for

productos = [
    {"id": 1, "nombre": "The Legend of Zelda TOTK", "precio": 60, "img": "The Legend of Zelda TOTK.jpg", "descripcion": "TOTK (Tears of the Kingdom) es un juego de aventura y acción en mundo abierto, secuela de Breath of the Wild.", "CPU": "Intel i5/i7 o equivalente", "GPU": "GTX 1060 / RTX 2060 o superior", "RAM": "16 GB", "Almacenamiento": "50 GB libres", "Sistema": "Windows 10/11 64-bit"},
    {"id": 2, "nombre": "Super Mario Odyssey", "precio": 60, "img": "Odyssey.jpg","descripcion": "Super Mario Odyssey es un juego de aventura en 3D donde exploras reinos variados y utilizas a Cappy para interactuar con el mundo de manera creativa.", "CPU": "Intel i5/i7 o equivalente", "GPU": "GTX 1060 / RTX 2060 o superior", "RAM": "16 GB", "Almacenamiento": "50 GB libres", "Sistema": "Windows 10/11 64-bit"},
    {"id": 3, "nombre": "Red Dead Redemption 2", "precio": 70, "img": "RDR2.jpg","descripcion": "Mundo abierto de acción y aventuras en el Viejo Oeste, con narrativa inmersiva, combates, exploración y caza.", "CPU": "Intel i5-2500K/Ryzen 3 1200", "GPU": "GTX 770/RX 470", "RAM": "8 GB", "Almacenamiento": "150 GB", "Sistema": "Windows 10 64-bit"},
    {"id": 4, "nombre": "God of War", "precio": 50, "img": "GOW.jpeg","descripcion": "God of War es un juego de acción y aventura con narrativa épica basada en la mitología nórdica.", "CPU": "Intel i5-6600K / Ryzen 5 2400G", "GPU": "GTX 970 / RX 470", "RAM": "8 GB", "Almacenamiento": "70 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 5, "nombre": "Horizon Zero Dawn", "precio": 50, "img": "Horizon.jpg","descripcion": "Horizon Zero Dawn es un RPG de acción en mundo abierto ambientado en un futuro postapocalíptico.", "CPU": "Intel i5-2500K", "GPU": "GTX 780 / RX 470", "RAM": "8 GB", "Almacenamiento": "50 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 6, "nombre": "Minecraft", "precio": 30, "img": "Minecraft.jpg","descripcion": "Minecraft es un sandbox de construcción y supervivencia en un mundo de bloques infinitos.", "CPU": "Intel Core i3", "GPU": "GPU integrada", "RAM": "4 GB", "Almacenamiento": "1 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 7, "nombre": "Call of Duty: Modern Warfare", "precio": 60, "img": "Modern_Warfare.jpg","descripcion": "Call of Duty: Modern Warfare es un shooter táctico con campañas intensas y multijugador competitivo.", "CPU": "Intel i5-2500K / AMD FX-6350", "GPU": "GTX 670 / RX 580", "RAM": "8 GB", "Almacenamiento": "175 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 8, "nombre": "The Witcher 3: Wild Hunt", "precio": 40, "img": "Witcher3.jpeg","descripcion": "The Witcher 3 es un RPG de mundo abierto con narrativa profunda y combate estratégico.", "CPU": "Intel i5-2500K / AMD Phenom II X4", "GPU": "GTX 660 / RX 470", "RAM": "8 GB", "Almacenamiento": "35 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 9, "nombre": "Overwatch 2", "precio": 0, "img": "Overwatch2.png","descripcion": "Overwatch 2 es un shooter en equipo con héroes únicos y habilidades especiales.", "CPU": "Intel Core i3", "GPU": "GTX 600 series", "RAM": "8 GB", "Almacenamiento": "30 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 10, "nombre": "Sekiro: Shadows Die Twice", "precio": 60, "img": "Sekiro.jpg","descripcion": "Sekiro es un juego de acción desafiante ambientado en un Japón feudal fantástico.", "CPU": "Intel Core i3-2100", "GPU": "GTX 760", "RAM": "4 GB", "Almacenamiento": "25 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 11, "nombre": "Fortnite", "precio": 0, "img": "Fortnite.jpg","descripcion": "Fortnite es un battle royale multijugador con construcción y combates dinámicos.", "CPU": "Intel Core i3 2.4 GHz", "GPU": "Intel HD 4000", "RAM": "4 GB", "Almacenamiento": "16 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 12, "nombre": "Bloodborne", "precio": 50, "img": "Bloodborne.jpg", "descripcion": "Bloodborne es un juego de acción y rol conocido por su dificultad desafiante, combate rápido y atmósfera oscura y gótica.", "CPU": "Intel i5/i7 o equivalente", "GPU": "GTX 1060 / RTX 2060 o superior", "RAM": "16 GB", "Almacenamiento": "50 GB libres", "Sistema": "Windows 10/11 64-bit"},
    {"id": 13, "nombre": "Assassin's Creed Valhalla", "precio": 60, "img": "Valhalla.jpg","descripcion": "Assassin s Creed Valhalla es un RPG de acción ambientado en la era vikinga.", "CPU": "Intel i5-4460 / Ryzen 3 1200", "GPU": "GTX 960 / RX 470", "RAM": "8 GB", "Almacenamiento": "50 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 14, "nombre": "Persona 5 Royal", "precio": 60, "img": "Persona5.jpg","descripcion": "Persona 5 Royal es un RPG por turnos con historia profunda y mecánicas de simulación social.", "CPU": "Intel Core i7-4790, 3.4 GHz | AMD Ryzen 5 1500X", "GPU": "Nvidia GeForce GTX 650 Ti, 2 GB | AMD Radeon R7 360", "RAM": "8 GB", "Almacenamiento": "41 GB libres", "Sistema": "Windows 10 64-bit"},
    {"id": 15, "nombre": "Final Fantasy VII Remake", "precio": 70, "img": "FFVII.jpeg","descripcion": "Final Fantasy VII Remake es un RPG de acción con combate en tiempo real y narrativa épica.", "CPU": "Intel Core i5-3330 / AMD Ryzen 3 1200", "GPU": "GTX 780 / RX 480", "RAM": "8 GB", "Almacenamiento": "100 GB libres", "Sistema": "Windows 10 64-bit"},
]

videojuegos_bp = Blueprint('videojuegos', __name__, template_folder='templates')



@videojuegos_bp.route('/videojuegos')
def inicio_videojuegos():
    return render_template(
        'index.html',
        titulo='Inicio',
        mensaje='Esto es una lista de 15 videojuegos.',
        productos=productos
    )

@videojuegos_bp.route('/videojuegos/<int:id>')
def detalle(id):
    producto = next((p for p in productos if p["id"] == id))
    return render_template('detalle.html', producto=producto)