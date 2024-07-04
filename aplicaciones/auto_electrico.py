import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Cargar un archivo Parquet
df = pd.read_parquet(r'C:\Users\Alañ\Documents\Henry\Proyecto 1\Proyecto Final\PF_GROUP_03_NYC_TAXIS\Datasets\nuevos\autos_electricos.parquet')
df['Marca'].str.strip()


# Separar características y variable objetivo
X = df.drop(columns=['Eficiencia', 'CargaRapidaRapida'])
y = df['Eficiencia']

# Preprocesamiento: Codificación de variables categóricas y normalización
categorical_features = ['Marca', 'Modelo', 'CargaRapida', 'Motorizacion', 'TipoEnchufe', 'EstiloCarroceria', 'Segmento']
numeric_features = ['Aceleracion', 'VelocidadMaxima', 'Autonomia', 'Asientos', 'PrecioEuro']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Definir el modelo
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Función para recomendar modelos basados en eficiencia predicha
def recomendar_modelos(marca, top_n=5):
    # Filtrar los datos por la marca especificada
    filtered_data = df[df['Marca'] == marca]
    
    if filtered_data.empty:
        return f"No hay datos disponibles para la marca {marca}."
    
    # Separar las características de los datos filtrados
    X_filtered = filtered_data.drop(columns=['Eficiencia'])
    
    # Predecir la eficiencia usando el modelo entrenado
    filtered_data['Eficiencia_Predicha'] = model.predict(X_filtered)
    
    # Ordenar los datos por la eficiencia predicha en orden descendente
    sorted_data = filtered_data.sort_values(by='Eficiencia_Predicha', ascending=False)
    
    # Seleccionar los top_n modelos con mayor eficiencia predicha
    top_modelos = sorted_data.head(top_n)['Modelo'].tolist()
    
    return top_modelos
