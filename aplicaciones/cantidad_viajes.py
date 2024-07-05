import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

def predict_taxi_trips(distrito_subida, hora, dia_semana):
    # Cargar el modelo guardado
    model = joblib.load("../aplicaciones/rf_green_model_2024_07_05.pkl")

    # Inicializar y ajustar el LabelEncoder
    label_encoder = LabelEncoder()
    label_encoder.fit(['Bronx', 'Manhattan', 'Queens', 'Brooklyn', 'Staten Island'])  # Ajustar con las categorías utilizadas durante el entrenamiento

    # Codificar distrito_subida
    distrito_encoded = label_encoder.transform([distrito_subida])[0]

    # Preparar los datos de entrada
    X_pred = pd.DataFrame({'distrito_subida': [distrito_encoded], 'hora': [hora], 'dia_semana': [dia_semana]})

    # Realizar la predicción
    prediction = int(model.predict(X_pred))

    return f"La cantidad de viajes en {distrito_subida} a las {hora} en ese día será de aproximadamente {prediction} viajes."

def main():
    distrito_subida = input("Ingrese el distrito de subida (Bronx, Manhattan, Queens, Brooklyn, Staten Island): ")
    hora = int(input("Ingrese la hora del día (0-23): "))
    dia_semana = int(input("Ingrese el día de la semana (1-7): "))

    # Realizar la predicción
    prediction = predict_taxi_trips(distrito_subida, hora, dia_semana)

    print(f"Predicción de cantidad de viajes: {prediction}")

if __name__ == "__main__":
    main()
