import pandas as pd
from dbfread import DBF

# ----------------- ETL  Taxis ------------------------------------ 

# DATASET 1 y 2
df1 = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\ElectricCarData_Clean.csv')
df2 = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\ElectricCarData_Norm.csv')

# Uno usando las columnas comunes
df_combined_1_2 = pd.merge(df1, df2, on=['Brand', 'Model'])

# Elimino columnas comunes
df_combined_1_2.drop(columns=['Accel', 'TopSpeed', 'Range', 'Efficiency', 'FastCharge', 'RapidCharge_y', 
                              'PowerTrain_y', 'PlugType_y', 'BodyStyle_y', 'Segment_y', 'Seats_y', 'PriceEuro_y'], inplace=True)

# Renombro las columnas
df_combined_1_2.columns = ['Brand', 'Model', 'Accel', 'TopSpeed', 'Range', 'Efficiency', 'FastCharge', 'RapidCharge', 'PowerTrain', 'PlugType', 'BodyStyle', 'Segment', 'Seats', 'PriceEuro']

# Diccionario de mapeo de columnas en inglés a español
column_mapping = {
    'Brand': 'Marca',
    'Model': 'Modelo',
    'Accel': 'Aceleracion',
    'TopSpeed': 'VelocidadMaxima',
    'Range': 'Autonomia',
    'Efficiency': 'Eficiencia',
    'FastCharge': 'CargaRapida',
    'RapidCharge': 'CargaRapidaRapida', 
    'PowerTrain': 'Motorizacion',
    'PlugType': 'TipoEnchufe',
    'BodyStyle': 'EstiloCarroceria',
    'Segment': 'Segmento',
    'Seats': 'Asientos',
    'PriceEuro': 'PrecioEuro'
}

# Renombro las columnas del DataFrame
df_combined_1_2 = df_combined_1_2.rename(columns=column_mapping)

# Elimino columnas duplicadas después de renombrar
df_combined_1_2 = df_combined_1_2.loc[:, ~df_combined_1_2.columns.duplicated()]

# Transformo el dataset a tipo .parquet
df_combined_1_2.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\autos_electricos.parquet', index=False)


# DATASET 3 y 4
df3 = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\taxi+_zone_lookup.csv')
table = DBF(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\taxi_zones.dbf')
df4 = pd.DataFrame(iter(table))

# Combino las columnas usando 'LocationID'
df_combined_3_4 = pd.merge(df3, df4, left_on=['LocationID', 'Borough'], right_on=['LocationID', 'borough'])

# Borro columnas
df_combined_3_4.drop(columns=['OBJECTID', 'zone', 'borough'], inplace=True)

# Cambio el nombre de las columnas
column_mapping = {
    'LocationID': 'ID_Ubicacion',
    'Borough': 'Distrito',
    'Zone': 'Zona',
    'service_zone': 'Zona_Servicio',
    'Shape_Leng': 'Longitud_Forma',
    'Shape_Area': 'Area_Forma'
}

df_combined_3_4 = df_combined_3_4.rename(columns=column_mapping)

# Elimino columnas duplicadas después de renombrar (solo si es necesario)
df_combined_3_4 = df_combined_3_4.loc[:, ~df_combined_3_4.columns.duplicated()]

# Transformo el dataset a tipo .parquet
df_combined_3_4.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\localizacion.parquet', index=False)


# DATASET 5, 6, 7
df5 = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\Light_Duty_Vehicles.csv')
df6 = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\Vehicle_Fuel_Economy_Data.csv', low_memory=False)
df7 = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\Alternative_Fuel_Vehicles_US.csv')

# Elimino columnas
df5.drop(columns=['Vehicle ID', 'Fuel ID', 'Fuel Configuration ID', 'Manufacturer ID', 'Category ID', 'Engine Description', 'Manufacturer URL', 'Fuel Code', 'Fuel Configuration Name', 'Electric-Only Range', 'PHEV Total Range', 'PHEV Type', 'Notes'], inplace=True)

df6.drop(columns=['drive', 'fuelCost08', 'range', 'rangeCity', 'rangeHwy', 'UCity', 'UHighway', 'co2A', 'co2TailpipeAGpm', 'barrels08', 'barrelsA08', 'charge240', 'city08', 'city08U', 'cityA08', 'cityA08U', 'cityCD', 'cityE', 'cityUF', 'comb08', 'comb08U', 'combA08', 'combA08U', 'combE', 'combinedCD', 'combinedUF', 'displ', 'engId', 'eng_dscr', 'feScore', 'fuelCostA08', 'fuelType1', 'ghgScore', 'ghgScoreA', 'highway08', 'highway08U', 'highwayA08', 'highwayA08U', 'VClass', 'highwayCD', 'highwayE', 'highwayUF', 'hlv', 'hpv', 'id', 'lv2', 'lv4', 'mpgData', 'phevBlended', 'pv2', 'pv4', 'rangeCityA', 'rangeHwyA', 'trany', 'UCityA', 'UHighwayA', 'youSaveSpend', 'guzzler', 'trans_dscr', 'tCharger', 'sCharger', 'atvType', 'fuelType2', 'rangeA', 'evMotor', 'mfrCode', 'c240Dscr', 'charge240b', 'c240bDscr', 'createdOn', 'modifiedOn', 'startStop', 'phevCity', 'phevHwy', 'phevComb'], inplace=True)

# Uno el Dataset 5 y el Dataset 6
df_combined_5_6 = pd.merge(df5, df6, left_on=['Model', 'Manufacturer', 'Model Year', 'Engine Cylinder Count'], right_on=['Model', 'Manufacturer', 'Year', 'cylinders'])

# Elimino columnas
df_combined_5_6.drop(columns=['cylinders', 'Year'], inplace=True)

df7.drop(columns=['Fuel', 'All-Electric Range', 'PHEV Total Range', 'Alternative Fuel Economy City', 'Alternative Fuel Economy Highway', 'Alternative Fuel Economy Combined', 'Conventional Fuel Economy City', 'Conventional Fuel Economy Highway', 'Conventional Fuel Economy Combined', 'Transmission Type', 'Transmission Make', 'Engine Type', 'Engine Size', 'Engine Cylinder Count', 'Number of Passengers', 'Heavy-Duty Power System', 'Notes', 'Drivetrain'], inplace=True)

# Convierto la columna a numérica
df7['Model Year'] = pd.to_numeric(df7['Model Year'], errors='coerce').astype('Int64')

# Uno el resultado con Dataset 7
df_combined_5_6_7 = pd.merge(df_combined_5_6, df7, on=['Model', 'Manufacturer', 'Model Year', 'Category'])

# Elimino columnas
df_combined_5_6_7.drop(columns=['Alternative Fuel Economy City', 'Alternative Fuel Economy Highway', 'Alternative Fuel Economy Combined'], inplace=True)

# Diccionario de mapeo de columnas en inglés a español
column_mapping = {
    'Model': 'Modelo',
    'Model Year': 'AnoModelo',
    'Conventional Fuel Economy City': 'EconomiaCombustibleCiudad',
    'Conventional Fuel Economy Highway': 'EconomiaCombustibleCarretera',
    'Conventional Fuel Economy Combined': 'EconomiaCombustibleCombinada',
    'Transmission Type': 'TipoTransmision',
    'Engine Type': 'TipoMotor',
    'Engine Size': 'TamanoMotor',
    'Engine Cylinder Count': 'CantidadCilindrosMotor',
    'Manufacturer': 'Fabricante',
    'Category': 'Categoria',
    'Fuel': 'Combustible',
    'Drivetrain': 'Traccion',
    'co2': 'CO2',
    'co2TailpipeGpm': 'CO2EscapeGpm',
    'fuelType': 'TipoCombustible'
}

# Renombro las columnas del DataFrame
df_combined_5_6_7 = df_combined_5_6_7.rename(columns=column_mapping)

# Elimino columnas duplicadas después de renombrar 
df_combined_5_6_7 = df_combined_5_6_7.loc[:, ~df_combined_5_6_7.columns.duplicated()]


# Transformo los Datasets en formato .parquet
df_combined_5_6_7.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\autos_combustion.parquet', index=False)
df_combined_1_2.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\autos_electricos.parquet', index=False)
df_combined_3_4.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\localizacion.parquet', index=False)

# DATASETS 8 y 9
df8 = pd.read_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\yellow_taxis.parquet')
df9 = pd.read_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\green_taxis.parquet')

# Agrego la columna 'taxi_type'
df8['taxi_type'] = 'yellow'
df9['taxi_type'] = 'green'

# Renombro columnas para que coincidan
yellow_taxis = df8.rename(columns={
    'tpep_pickup_datetime': 'pickup_datetime',
    'tpep_dropoff_datetime': 'dropoff_datetime'
})

green_taxis = df9.rename(columns={
    'lpep_pickup_datetime': 'pickup_datetime',
    'lpep_dropoff_datetime': 'dropoff_datetime'
})

# Aseguro que ambos DataFrames tengan las mismas columnas
yellow_taxis = yellow_taxis.assign(ehail_fee=pd.NA, trip_type=pd.NA, Airport_fee=pd.NA)
green_taxis = green_taxis.assign(Airport_fee=pd.NA)

# Ordeno las columnas para que coincidan
columns_order = ['VendorID', 'pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_distance',
                 'RatecodeID', 'store_and_fwd_flag', 'PULocationID', 'DOLocationID', 'payment_type',
                 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
                 'total_amount', 'congestion_surcharge', 'Airport_fee', 'ehail_fee', 'trip_type', 'taxi_type']

yellow_taxis = yellow_taxis[columns_order]
green_taxis = green_taxis[columns_order]

# Excluyo columnas vacías o con todos los valores como NA antes de concatenar
yellow_taxis_filtered = yellow_taxis.dropna(axis=1, how='all')
green_taxis_filtered = green_taxis.dropna(axis=1, how='all')

# Uno los DataFrames
combined_taxis = pd.concat([yellow_taxis_filtered, green_taxis_filtered], ignore_index=True)

# Defino los diccionarios de mapeo
vendor_id_map = {
    1: 'Creative Mobile Technologies, LLC',
    2: 'VeriFone Inc.'
}

rate_code_id_map = {
    1: 'Standard rate',
    2: 'JFK',
    3: 'Newark',
    4: 'Nassau or Westchester',
    5: 'Negotiated fare',
    6: 'Group ride'
}

store_and_fwd_flag_map = {
    'Y': 'store and forward trip',
    'N': 'not a store and forward trip'
}

payment_type_map = {
    1: 'Credit card',
    2: 'Cash',
    3: 'No charge',
    4: 'Dispute',
    5: 'Unknown',
    6: 'Voided trip'
}

# Aplico los mapeos a las columnas correspondientes
combined_taxis['VendorID'] = combined_taxis['VendorID'].map(vendor_id_map)
combined_taxis['RatecodeID'] = combined_taxis['RatecodeID'].map(rate_code_id_map)
combined_taxis['store_and_fwd_flag'] = combined_taxis['store_and_fwd_flag'].map(store_and_fwd_flag_map)
combined_taxis['payment_type'] = combined_taxis['payment_type'].map(payment_type_map)

# Convierto las columnas de fecha al formato de fecha adecuado si no están en ese formato
combined_taxis['pickup_datetime'] = pd.to_datetime(combined_taxis['pickup_datetime'])
combined_taxis['dropoff_datetime'] = pd.to_datetime(combined_taxis['dropoff_datetime'])

# Filtro los registros donde el año de pickup_datetime sea mayor o igual a 2024
combined_taxis = combined_taxis[combined_taxis['pickup_datetime'].dt.year >= 2024]

# Defino el diccionario de renombramiento
nuevos_nombres = {
     'VendorID': 'id_proveedor',
    'pickup_datetime': 'hora_recogida',
    'dropoff_datetime': 'hora_bajada',
    'passenger_count': 'cantidad_pasajeros',
    'total_amount': 'monto_total',
    'congestion_surcharge': 'recargo_congestion',
    'taxi_type': 'tipo_taxi',
    'trip_type': 'tipo_viaje',
    'trip_distance': 'distancia_viaje',
    'RatecodeID': 'ID_tarifa',
    'store_and_fwd_flag': 'almacenamiento_reenvio',
    'PULocationID': 'ID_ubicacion_recogida',
    'DOLocationID': 'ID_ubicacion_bajada',
    'payment_type': 'tipo_pago',
    'fare_amount': 'tarifa',
    'extra': 'extra',
    'mta_tax': 'impuesto_mta',
    'tip_amount': 'monto_propina',
    'tolls_amount': 'monto_peajes',
    'improvement_surcharge': 'recargo_mejora'
}

# Renombro las columnas usando el método rename
combined_taxis = combined_taxis.rename(columns=nuevos_nombres)


# Convierto los datasets a formato .parquet
combined_taxis.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\taxis.parquet', index='False')


#--------------------------------------------------------------------------------------------------------
# ----------------- ETL  Air-quality -------------------------------------------------------------------


#Leo el dataset
df_NYC_air_quality = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\Air_Quality_raw.csv')

# Vemos el contenido dentro de la columna 'Geo Place Name' con la finalidad de poder crear un diccionario para poder normalizar los 'Borough'.
#Listo los elementos únicos de la columna 'Geo Place Name'
lugares_unicos = df_NYC_air_quality['Geo Place Name'].unique()

#Muestro los lugares únicos
for lugar in lugares_unicos:
    print(lugar)

# Exporto todo el contenido de 'Geo Place Name' a un csv.
#Creo un DataFrame con los lugares únicos
df_lugares_unicos = pd.DataFrame(lugares_unicos, columns=['Geo Place Name'])


# Creo un diccionario con los lugares_unicos para poder asociarlos a cada 'Borough'.
#Mapeo de 'Geo Place Name' a 'Borough'
mapeo_lugares_a_borough = {
    'Morrisania and Crotona (CD3)': 'Bronx',
    'Bedford Stuyvesant (CD3)': 'Brooklyn',
    'Tottenville and Great Kills (CD3)': 'Staten Island',
    'Chelsea-Village': 'Manhattan',
    'Bedford Stuyvesant - Crown Heights': 'Brooklyn',
    'Flushing - Clearview': 'Queens',
    'Fordham - Bronx Pk': 'Bronx',
    'Pelham - Throgs Neck': 'Bronx',
    'East Harlem': 'Manhattan',
    'East New York': 'Brooklyn',
    'Upper East Side-Gramercy': 'Manhattan',
    'South Beach - Tottenville': 'Staten Island',
    'Bayside - Little Neck': 'Queens',
    'Flushing and Whitestone (CD7)': 'Queens',
    'Flatbush and Midwood (CD14)': 'Brooklyn',
    'Sunset Park': 'Brooklyn',
    'Bayside Little Neck-Fresh Meadows': 'Queens',
    'Southeast Queens': 'Queens',
    'Bensonhurst - Bay Ridge': 'Brooklyn',
    'Union Square-Lower Manhattan': 'Manhattan',
    'South Ozone Park and Howard Beach (CD10)': 'Queens',
    'Jamaica and Hollis (CD12)': 'Queens',
    'Throgs Neck and Co-op City (CD10)': 'Bronx',
    'Borough Park (CD12)': 'Brooklyn',
    'Williamsburg - Bushwick': 'Brooklyn',
    'Ridgewood - Forest Hills': 'Queens',
    'Willowbrook': 'Staten Island',
    'Hillcrest and Fresh Meadows (CD8)': 'Queens',
    'Rego Park and Forest Hills (CD6)': 'Queens',
    'Clinton and Chelsea (CD4)': 'Manhattan',
    'Stuyvesant Town and Turtle Bay (CD6)': 'Manhattan',
    'Riverdale and Fieldston (CD8)': 'Bronx',
    'South Beach and Willowbrook (CD2)': 'Staten Island',
    'Financial District (CD1)': 'Manhattan',
    'Woodside and Sunnyside (CD2)': 'Queens',
    'Greenpoint and Williamsburg (CD1)': 'Brooklyn',
    'St. George and Stapleton (CD1)': 'Staten Island',
    'Fort Greene and Brooklyn Heights (CD2)': 'Brooklyn',
    'Mott Haven and Melrose (CD1)': 'Bronx',
    'Upper West Side': 'Manhattan',
    'Hunts Point and Longwood (CD2)': 'Bronx',
    'Long Island City and Astoria (CD1)': 'Queens',
    'Coney Island - Sheepshead Bay': 'Brooklyn',
    'Manhattan': 'Manhattan',
    'High Bridge - Morrisania': 'Bronx',
    'Union Square - Lower East Side': 'Manhattan',
    'Greenwich Village and Soho (CD2)': 'Manhattan',
    'Kingsbridge - Riverdale': 'Bronx',
    'Northeast Bronx': 'Bronx',
    'West Queens': 'Queens',
    'Jackson Heights (CD3)': 'Queens',
    'Flatlands and Canarsie (CD18)': 'Brooklyn',
    'East Flatbush (CD17)': 'Brooklyn',
    'Central Harlem - Morningside Heights': 'Manhattan',
    'Downtown - Heights - Slope': 'Brooklyn',
    'Southwest Queens': 'Queens',
    'Washington Heights': 'Manhattan',
    'Upper West Side (CD7)': 'Manhattan',
    'Rockaway and Broad Channel (CD14)': 'Queens',
    'Kingsbridge Heights and Bedford (CD7)': 'Bronx',
    'Sunset Park (CD7)': 'Brooklyn',
    'Williamsbridge and Baychester (CD12)': 'Bronx',
    'Washington Heights and Inwood (CD12)': 'Manhattan',
    'Upper East Side (CD8)': 'Manhattan',
    'Long Island City - Astoria': 'Queens',
    'Port Richmond': 'Staten Island',
    'Bay Ridge and Dyker Heights (CD10)': 'Brooklyn',
    'Central Harlem (CD10)': 'Manhattan',
    'New York City': 'Manhattan',
    'Jamaica': 'Queens',
    'Canarsie - Flatlands': 'Brooklyn',
    'Coney Island (CD13)': 'Brooklyn',
    'Sheepshead Bay (CD15)': 'Brooklyn',
    'Queens': 'Queens',
    'Queens Village (CD13)': 'Queens',
    'Rockaways': 'Queens',
    'Lower Manhattan': 'Manhattan',
    'Crown Heights and Prospect Heights (CD8)': 'Brooklyn',
    'Belmont and East Tremont (CD6)': 'Bronx',
    'Park Slope and Carroll Gardens (CD6)': 'Brooklyn',
    'Crotona -Tremont': 'Bronx',
    'Upper East Side': 'Manhattan',
    'Ridgewood and Maspeth (CD5)': 'Queens',
    'Midtown (CD5)': 'Manhattan',
    'Fresh Meadows': 'Queens',
    'East Flatbush - Flatbush': 'Brooklyn',
    'Fordham and University Heights (CD5)': 'Bronx',
    'East New York and Starrett City (CD5)': 'Brooklyn',
    'Chelsea - Clinton': 'Manhattan',
    'Bayside and Little Neck (CD11)': 'Queens',
    'East Harlem (CD11)': 'Manhattan',
    'Morningside Heights and Hamilton Heights (CD9)': 'Manhattan',
    'Bensonhurst (CD11)': 'Brooklyn',
    'Morris Park and Bronxdale (CD11)': 'Bronx',
    'Kew Gardens and Woodhaven (CD9)': 'Queens',
    'Stapleton - St. George': 'Staten Island',
    'South Crown Heights and Lefferts Gardens (CD9)': 'Brooklyn',
    'Parkchester and Soundview (CD9)': 'Bronx',
    'Brownsville (CD16)': 'Brooklyn',
    'Gramercy Park - Murray Hill': 'Manhattan',
    'Greenwich Village - SoHo': 'Manhattan',
    'Hunts Point - Mott Haven': 'Bronx',
    'Bronx': 'Bronx',
    'Elmhurst and Corona (CD4)': 'Queens',
    'Highbridge and Concourse (CD4)': 'Bronx',
    'Bushwick (CD4)': 'Brooklyn',
    'Brooklyn': 'Brooklyn',
    'Lower East Side and Chinatown (CD3)': 'Manhattan',
    'South Bronx': 'Bronx',
    'Southern SI': 'Staten Island',
    'Northern SI': 'Staten Island'
}


# Agrego nueva columna 'Borough' al DataFrame original.
df_NYC_air_quality['Borough'] = df_NYC_air_quality['Geo Place Name'].map(mapeo_lugares_a_borough)

# Filtro para saber a qué elemento de 'Geo Place Name' no se le asignó su 'Borough'.
# Filtro el DataFrame para las filas donde 'Borough' es nulo
filas_sin_borough = df_NYC_air_quality[df_NYC_air_quality['Borough'].isnull()]

# Obtengo los elementos únicos de 'Geo Place Name' sin 'Borough'
lugares_sin_borough_unicos = filas_sin_borough['Geo Place Name'].unique()

# Imprimo los elementos únicos sin 'Borough'
for lugar in lugares_sin_borough_unicos:
    print(lugar)

# Mapeo adicional para los lugares identificados
mapeo_lugares_adicional = {
    'Borough Park': 'Brooklyn',
    'Greenpoint': 'Brooklyn',
    'Staten Island': 'Staten Island'
}

# Actualizo el DataFrame para asignar los Boroughs correspondientes
df_NYC_air_quality.loc[df_NYC_air_quality['Geo Place Name'].isin(mapeo_lugares_adicional.keys()), 'Borough'] = df_NYC_air_quality['Geo Place Name'].map(mapeo_lugares_adicional)

# Verifico que se hayan actualizado correctamente
print(df_NYC_air_quality[df_NYC_air_quality['Geo Place Name'].isin(mapeo_lugares_adicional.keys())][['Geo Place Name', 'Borough']])

# Obtengo los elementos únicos de la columna 'measure'
medidas_unicas = df_NYC_air_quality['Measure'].unique()

# Imprimo los elementos únicos
for medida in medidas_unicas:
    print(medida)


# Se eliminan las columnas que no son necesarias para el estudio del la contaminacion en NYC.
columnas_a_eliminar = ['Indicator ID','Measure','Geo Type Name','Geo Join ID','Geo Place Name','Time Period','Message','Unique ID']

# Elimino las columnas
df_NYC_air_quality = df_NYC_air_quality.drop(columnas_a_eliminar, axis=1)

# Elimino los valores que no hacen referencia a la contaminacion producto de los automoviles.

valores_a_eliminar = [
    'Asthma emergency department visits due to PM2.5',
    'Cardiac and respiratory deaths due to Ozone',
    'Deaths due to PM2.5',
    'Respiratory hospitalizations due to PM2.5 (age 20+)',
    'Asthma hospitalizations due to Ozone',
    'Asthma emergency departments visits due to Ozone',
    'Cardiovascular hospitalizations due to PM2.5 (age 40+)',
    'Boiler Emissions- Total NOx Emissions',
    'Boiler Emissions- Total PM2.5 Emissions',
    'Boiler Emissions- Total SO2 Emissions',
    'Annual vehicle miles traveled (trucks)',
    'Annual vehicle miles traveled (cars)',
    'Annual vehicle miles traveled'
]

#Elimino las filas que contienen los valores especificados en la columna 'contaminante'
df_NYC_air_quality = df_NYC_air_quality[~df_NYC_air_quality['Name'].isin(valores_a_eliminar)]

# Normalizo la unidad de medida.
#Reemplazar los valores "Âµg/m3" por "mcg/m3" en la columna 'measure_info' tratando la codificación incorrecta
df_NYC_air_quality.loc[:, 'Measure Info'] = df_NYC_air_quality['Measure Info'].str.replace("Âµg/m3", "mcg/m3", regex=False)

# Transformo la columna 'Start_Date' en datetime.
#Convierto la columna 'Start_Date' a tipo datetime usando .astype()
df_NYC_air_quality['Start_Date'] = df_NYC_air_quality['Start_Date'].astype('datetime64[ns]')

# Ordeno el dataset en función de 'Start_Date' de manera ascendente.
df_NYC_air_quality = df_NYC_air_quality.sort_values(by='Start_Date', ascending=True)

# Cambio el nombre a las columnas 'Name', 'Start_Date', 'Borough'.
df_NYC_air_quality = df_NYC_air_quality.rename(columns={
    'Name': 'contaminante',
    'Start_Date': 'fecha',
    'Borough': 'Barrio'
})

# Renombro las columnas
nuevos_nombres = {
    'contaminante': 'Contaminante',
    'Measure Info': 'Informacion_medida',
    'fecha': 'Fecha',
    'Data Value': 'Valor_dato',
    'Barrio': 'Distrito'
}

# Renombro usando rename
df_NYC_air_quality = df_NYC_air_quality.rename(columns=nuevos_nombres)

# Exporto a tipo parquet
df_NYC_air_quality.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\NYC_air_quality.parquet', index=False)


#--------------------------------------------------------------------------------------------------------
# ----------------- ETL sonidos -------------------------------------------------------------------

# Leo el dataset
df_NYC_sonidos = pd.read_csv(r'C:\Users\Alañ\Pictures\prueba\Datasets\sucios\NYC_sonidos_raw.csv')

# Lista de columnas a eliminar
columnas_a_eliminar = [
    '2-1_rock-drill_presence', '2-2_jackhammer_presence', '2-3_hoe-ram_presence', '2-4_pile-driver_presence', '2-X_other-unknown-impact-machinery_presence',
    '3-1_non-machinery-impact_presence',
    '4-1_chainsaw_presence', '4-2_small-medium-rotating-saw_presence', '4-3_large-rotating-saw_presence', '4-X_other-unknown-powered-saw_presence',
    '5-1_car-horn_presence', '5-2_car-alarm_presence', '5-3_siren_presence', '5-4_reverse-beeper_presence', '5-X_other-unknown-alert-signal_presence',
    '6-1_stationary-music_presence', '6-2_mobile-music_presence', '6-3_ice-cream-truck_presence', '6-X_music-from-uncertain-source_presence',
    '7-1_person-or-small-group-talking_presence', '7-2_person-or-small-group-shouting_presence', '7-3_large-crowd_presence', '7-4_amplified-speech_presence', '7-X_other-unknown-human-voice_presence',
    '8-1_dog-barking-whining_presence',
    '2-1_rock-drill_proximity', '2-2_jackhammer_proximity', '2-3_hoe-ram_proximity', '2-4_pile-driver_proximity', '2-X_other-unknown-impact-machinery_proximity',
    '3-1_non-machinery-impact_proximity',
    '4-1_chainsaw_proximity', '4-2_small-medium-rotating-saw_proximity', '4-3_large-rotating-saw_proximity', '4-X_other-unknown-powered-saw_proximity',
    '5-1_car-horn_proximity', '5-2_car-alarm_proximity', '5-3_siren_proximity', '5-4_reverse-beeper_proximity', '5-X_other-unknown-alert-signal_proximity',
    '6-1_stationary-music_proximity', '6-2_mobile-music_proximity', '6-3_ice-cream-truck_proximity', '6-X_music-from-uncertain-source_proximity',
    '7-1_person-or-small-group-talking_proximity', '7-2_person-or-small-group-shouting_proximity', '7-3_large-crowd_proximity', '7-4_amplified-speech_proximity', '7-X_other-unknown-human-voice_proximity',
    '8-1_dog-barking-whining_proximity',
    '2_machinery-impact_presence',
    '3_non-machinery-impact_presence',
    '4_powered-saw_presence',
    '5_alert-signal_presence',
    '6_music_presence',
    '7_human-voice_presence',
    '8_dog_presence',
    '1-1_small-sounding-engine_proximity',
    '1-2_medium-sounding-engine_proximity',
    '1-3_large-sounding-engine_proximity',
    '1-X_engine-of-uncertain-size_proximity',
    'split',
    'sensor_id',
    'audio_filename'
]

# Elimino las columnas
df_NYC_sonidos = df_NYC_sonidos.drop(columnas_a_eliminar, axis=1)

# Elimino filas donde '1_engine_presence' tiene valor -1
df_NYC_sonidos = df_NYC_sonidos[df_NYC_sonidos['1_engine_presence'] != -1]

# 'week' y 'day' son el número de la semana y el día de la semana respectivamente
# Convierto 'week' y 'day' a la fecha del primer día de la semana
df_NYC_sonidos['fecha'] = pd.to_datetime(df_NYC_sonidos['year'].astype(str) + 
                                         df_NYC_sonidos['week'].astype(str) + 
                                         df_NYC_sonidos['day'].astype(str), format='%Y%W%w')

# Sumo las horas correspondientes
df_NYC_sonidos['fecha'] += pd.to_timedelta(df_NYC_sonidos['hour'], unit='h')

# Listo todos los elementos dentro de la columna Borough
# Obtengo los elementos únicos de la columna 'borough'
boroughs_unicos = df_NYC_sonidos['borough'].unique()

# Se imprimen los elementos únicos
for borough in boroughs_unicos:
    print(borough)

# Transformo los valores que aparecen en 'borough', de tal manera que:
# - 1=Manhattan
# - 3=Brooklyn
# - 4=Queens

# Diccionario de mapeo de valores de 'borough'
mapeo_boroughs = {
    1: 'Manhattan',
    3: 'Brooklyn',
    4: 'Queens'
}

# Aplico la transformación a la columna 'borough'
df_NYC_sonidos['borough'] = df_NYC_sonidos['borough'].map(mapeo_boroughs)

# Elimino las columnas 'year', 'week', 'day' y 'hour', porque ahora tenemos la columna fecha.
columnas_a_eliminar = [
    'year',
    'week',
    'day',
    'hour',
    'annotator_id',
    'block',
    'latitude',
    'longitude'
]

df_NYC_sonidos = df_NYC_sonidos.drop(columnas_a_eliminar, axis=1)

# Renombro las columnas
column_mapping = {
    'borough': 'Barrio',
    '1-1_small-sounding-engine_presence': 'small_sounding_engine_presence',
    '1-2_medium-sounding-engine_presence': 'medium_sounding_engine_presence',
    '1-3_large-sounding-engine_presence': 'large_sounding_engine_presence',
    '1-X_engine-of-uncertain-size_presence': 'engine_of_uncertain_size_presence',
    '1_engine_presence': 'engine_presence'
}

# Renombro las columnas utilizando el diccionario
df_NYC_sonidos = df_NYC_sonidos.rename(columns=column_mapping)

# Ordeno los valores del DF por fecha
df_NYC_sonidos = df_NYC_sonidos.sort_values(by='fecha', ascending=True)

# Elimino las horas, minutos y segundos de las mediciones.
# Extraigo solo la parte de la fecha (año, mes, día)
df_NYC_sonidos['fecha'] = df_NYC_sonidos['fecha'].dt.date

# Renombro las columnas 
nuevos_nombres = {
    'Barrio': 'Distrito',
    'small_sounding_engine_presence': 'Presencia_motor_pequenio',
    'medium_sounding_engine_presence': 'Presencia_motor_mediano',
    'large_sounding_engine_presence': 'Presencia_motor_grande',
    'engine_of_uncertain_size_presence': 'Presencia_motor_tamanio_incertidumbre',
    'fecha': 'Fecha'
}

# Renombro las columnas usando el método rename
df_NYC_sonidos = df_NYC_sonidos.rename(columns=nuevos_nombres)

# Transformo el dataset a tipo .parquet
df_NYC_sonidos.to_parquet(r'C:\Users\Alañ\Pictures\prueba\Datasets\nuevos\NYC_sonidos.parquet', index=False)
