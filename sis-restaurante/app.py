from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "restaurante2026"

USUARIO = "admin"
PASSWORD = "1234"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validar', methods=['POST'])
def validar():

    usuario = request.form['usuario']
    password = request.form['password']

    if usuario == USUARIO and password == PASSWORD:
        session['usuario'] = usuario
        return redirect('/dashboard')

    return """
    <script>
    alert('Usuario o contraseña incorrectos');
    window.location='/';
    </script>
    """

@app.route('/dashboard')
def dashboard():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('dashboard.html')

@app.route('/platos')
def platos():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('platos.html')


@app.route('/inventario')
def inventario():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('inventario.html')


@app.route('/pedidos')
def pedidos():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('pedidos.html')


@app.route('/mesas')
def mesas():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('mesas.html')


@app.route('/reportes')
def reportes():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('reportes.html')


@app.route('/ventas')
def ventas():

    if 'usuario' not in session:
        return redirect('/')

    return render_template('ventas.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)