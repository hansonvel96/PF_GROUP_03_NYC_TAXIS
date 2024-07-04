import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Procesamiento de datos y entrenamiento del modelo
df = pd.read_parquet(r'C:\Users\Alañ\Documents\Henry\Proyecto 1\Proyecto Final\PF_GROUP_03_NYC_TAXIS\Datasets\nuevos\autos_combustion.parquet')

df_combustion = df.copy()
df_combustion.drop(columns=['EconomiaCombustibleCiudad','EconomiaCombustibleCarretera', 'EconomiaCombustibleCombinada','TipoTransmision',
                            'TipoMotor', 'TamanoMotor', 'CantidadCilindrosMotor','Traccion','CO2EscapeGpm', 'TipoCombustible'], inplace=True)
df_combustion.replace(to_replace=pd.NA, value=0, inplace=True)
df_combustion['CO2_Tipo'] = (df_combustion['CO2'] > df_combustion['CO2'].median()).astype(int)

df_combustion = pd.get_dummies(df_combustion, columns=['Fabricante', 'Categoria'])

X = df_combustion.drop(['Modelo', 'Combustible', 'CO2','CO2_Tipo'], axis=1)
y = df_combustion['CO2_Tipo']

modelo = LogisticRegression(max_iter=1000)
modelo.fit(X, y)

# Función de recomendación de autos menos contaminantes
def recomendacionAuto(fabricante):
    Fabricante_dummie = 'Fabricante_' + fabricante
    if not Fabricante_dummie in df_combustion.columns:
        return 'No hay nada'
    df_fabricante = df_combustion[df_combustion[Fabricante_dummie] == 1].copy()

    modelos_autos = df_fabricante['Modelo']
    modelo_combustible = df_fabricante['Combustible']
    modelo_co2 = df_fabricante['CO2']
    df_fabricante.drop(['Modelo', 'Combustible', 'CO2','CO2_Tipo'], axis=1, inplace=True)
    
    df_fabricante = pd.get_dummies(df_fabricante)

    probabilidad_emision_alta = modelo.predict_proba(df_fabricante)[:, 1]
    df_fabricante['Probabilidad_Emision_Alta'] = probabilidad_emision_alta

    df_fabricante['Modelo'] = modelos_autos
    df_fabricante['Combustible'] = modelo_combustible
    df_fabricante['CO2'] = modelo_co2

    df_fabricante = df_fabricante.sort_values(by='Probabilidad_Emision_Alta', ascending=True)

    modelos_final = pd.DataFrame(df_fabricante['Modelo'])
    modelos_final['AnoModelo'] = df_fabricante['AnoModelo']
    modelos_final['Combustible'] = df_fabricante['Combustible']
    modelos_final['CO2'] = df_fabricante['CO2']
    
    recomendaciones_modelo = modelos_final.head(5)['Modelo'].tolist()
    recomendaciones_anio = modelos_final.head(5)['AnoModelo'].tolist()
    recomendaciones_combustible = modelos_final.head(5)['Combustible'].tolist()
    
    recomendaciones = 'Estas son modelos de autos que nosotros recomendamos para la marca ' + str(fabricante) + ' que tienen un menor impacto ambiental.\n'
    for i in range(0, len(recomendaciones_modelo)):
        recomendaciones += 'Modelo ' + str(i+1) + ': ' + str(recomendaciones_modelo[i]) + ' del año ' + str(recomendaciones_anio[i]) + ', Combustible: ' + str(recomendaciones_combustible[i]) + '\n'
    return recomendaciones