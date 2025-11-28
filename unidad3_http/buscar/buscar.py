from flask import request, render_template, Blueprint

buscar_bp = Blueprint('buscar', __name__, template_folder='templates')

@buscar_bp.route('/buscar')
def inicio_buscar():
    termino = request.args.get('q', '')
    if not termino:
        return "Indica un término de búsqueda con ?q=algo"
    return f"Resultados de búsqueda para: {termino}"