from flask import request, render_template, Blueprint

login_bp = Blueprint('login', __name__, template_folder='templates')

USUARIO_VALIDO = "alu"
PASS_VALIDA = "alu"


@login_bp.route('/login', methods=['GET', 'POST'])
def inicio_login():
    titulo="Login"
    error = None
    usuario = None

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        if not usuario or not password:
            error = "ERROR, hay un campo erroneo/incompleto"
        elif usuario == USUARIO_VALIDO and password == PASS_VALIDA:
            return f"Has iniciado sesión con {usuario}. Que disfrutes de tu estancia."
        else:
            error = "Usuario o contraseña incorrectos."

    return render_template('inicio_login.html', error=error, usuario=usuario, titulo=titulo)
