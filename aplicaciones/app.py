from flask import Flask, render_template, request, session, redirect, url_for, request
from flask_session import Session
from aplicaciones.auto_combustible import recomendacionAuto
from aplicaciones.auto_electrico import recomendar_modelos
from aplicaciones.cantidad_viajes import predict_taxi_trips

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

# Rutas en Flask
@app.route('/CantidadViajes', methods=['GET', 'POST'])
def cantidad_viajes():
    if request.method == 'POST':
        distrito_subida = request.form.get('distrito_subida')
        hora = int(request.form.get('hora'))
        dia_semana = int(request.form.get('dia_semana'))

        # Realizar la predicción de cantidad de viajes
        cantidad_predicha = predict_taxi_trips(distrito_subida, hora, dia_semana)

        # Renderizar la plantilla con el resultado
        return render_template('cantidadviajes.html', cantidad_predicha=cantidad_predicha)
    else:
        return render_template('cantidadviajes.html')

@app.route('/resultadoCantidadViajes', methods=['POST'])
def resultado_cantidad_viajes():
    distrito_subida = request.form.get('distrito_subida')
    hora = int(request.form.get('hora'))
    dia_semana = int(request.form.get('dia_semana'))
    cantidad_predicha = predict_taxi_trips(distrito_subida, hora, dia_semana)
    return render_template('cantidadviajes.html', cantidad_aux=cantidad_predicha)

@app.route('/AutoCombustion', methods =['GET', 'POST'])
def autocombustion():
    if request.method == 'POST':
        fabricante = request.form.get('fabricante')
        session['recomendaciones'] = recomendacionAuto(fabricante)
        return render_template('autocombustion.html', recomendaciones=session['recomendaciones'])
    else:
        session.pop('recomendaciones', None)  # Limpiar recomendaciones al cargar la página
        return render_template('autocombustion.html')

@app.route('/resultadoAutoCombustion', methods=['POST'])
def resultado_autocombustion():
    fabricante = recomendacionAuto(request.form['fabricante'])
    return render_template('autocombustion.html', fabricante_aux=fabricante)

@app.route('/AutoElectrico', methods =['GET', 'POST'])
def autoelectrico():
    if request.method == 'POST':
        marca = request.form.get('marca')
        session['recomendaciones'] = recomendar_modelos(marca)
        return render_template('autoelectrico.html', recomendaciones=session['recomendaciones'])
    else:
        session.pop('recomendaciones', None)  # Limpiar recomendaciones al cargar la página
        return render_template('autoelectrico.html')

@app.route('/resultadoAutoElectrico', methods=['POST'])
def resultado_autoelectrico():
    marca = recomendar_modelos(request.form['marca'])
    return render_template('autoelectrico.html', marca_aux=marca)

@app.route('/Contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/Power Bi')
def powerbi():
    return render_template('powerbi.html')

if __name__ == '__main__':
    app.run(debug=True)
