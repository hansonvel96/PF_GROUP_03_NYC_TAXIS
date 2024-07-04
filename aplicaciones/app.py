from flask import Flask, render_template, request, session, redirect, url_for, request
from flask_session import Session
from auto_combustible import recomendacionAuto
from auto_electrico import recomendar_modelos

app = Flask(__name__)

# Configuración de la sesión
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def main():
    return render_template('modeloML.html')

@app.route('/ModeloML')
def modeloML():
    return render_template('modeloML.html')

@app.route('/TercerModelo', methods =['GET', 'POST'])
def tercermodelo():
    return render_template('tercermodelo.html')

@app.route('/resultadoTercerModelo', methods=['POST'])
def resultado_tercermodelo():
    return render_template('tercermodelo.html')

@app.route('/AutoCombustion', methods =['GET', 'POST'])
def autocombustion():
    if request.method == 'POST':
        fabricante = request.form.get('fabricante')
        session['recomendaciones'] = recomendacionAuto(fabricante)
        return render_template('autoCombustion.html', recomendaciones=session['recomendaciones'])
    else:
        session.pop('recomendaciones', None)  # Limpiar recomendaciones al cargar la página
        return render_template('autoCombustion.html')

@app.route('/resultadoAutoCombustion', methods=['POST'])
def resultado_autocombustion():
    fabricante = recomendacionAuto(request.form['fabricante'])
    return render_template('autocombustion.html', fabricante_aux=fabricante)

@app.route('/AutoElectrico', methods =['GET', 'POST'])
def autoelectrico():
    if request.method == 'POST':
        marca = request.form.get('marca')
        session['recomendaciones'] = recomendar_modelos(marca)
        return render_template('autoElectrico.html', recomendaciones=session['recomendaciones'])
    else:
        session.pop('recomendaciones', None)  # Limpiar recomendaciones al cargar la página
        return render_template('autoElectrico.html')

@app.route('/resultadoAutoElectrico', methods=['POST'])
def resultado_autoelectrico():
    marca = recomendar_modelos(request.form['marca'])
    return render_template('autoelectrico.html', marca_aux=marca)

@app.route('/Contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)
