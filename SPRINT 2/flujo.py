from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from google.cloud import storage
import os

# Obtener el mes actual y restarle doce meses
today = datetime.now().year
last_year = str(today - 1)
today = str(today)
current_directory = os.getcwd()

# Configura el cliente de GCS
storage_client = storage.Client()

def upload_to_gcs(file_path, bucket_name, destination_blob_name):
    """Sube un archivo a Google Cloud Storage."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    # Sube el archivo
    blob.upload_from_filename(file_path)

# Define el intervalo de tiempo para la ejecución del DAG
default_args = {
    'owner': 'user',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 24),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define el DAG
dag = DAG(
    'scraping_scripts',
    default_args=default_args,
    description='Ejecución de scripts de scraping',
    schedule_interval='@monthly',  # Ejecutar mensualmente
)

# Define las tareas (operadores) para cada script

def execute_scraping_aire():
    url = "https://cdn.who.int/media/docs/default-source/air-pollution-documents/air-quality-and-health/who_database_template_2022.xlsx?sfvrsn=c948d71a_11"
    response = requests.get(url)
    if response.status_code == 200:
        with open('Data-Dictionary-Air-Quality.xlsx', 'wb') as f:
            f.write(response.content)
        # Ejemplo de código para descargar y cargar un archivo
        file_path = os.path.join(current_directory, 'Data-Dictionary-Air-Quality.xlsx')
        upload_to_gcs(file_path, 'datasets_taxis', 'sucios/aire.xlsx')
        # Elimina el archivo local después de cargarlo
        os.remove(file_path)

scraping_aire_task = PythonOperator(
    task_id='scraping_aire_task',
    python_callable=execute_scraping_aire,
    dag=dag,
)

def execute_scraping_sonido():
    url = "https://zenodo.org/records/3966543/files/annotations.csv?download=1"
    response = requests.get(url)
    if response.status_code == 200:
        with open('annotations.csv', 'wb') as f:
            f.write(response.content)
        # Ejemplo de código para descargar y cargar un archivo
        file_path = os.path.join(current_directory, 'annotations.csv')
        upload_to_gcs(file_path, 'datasets_taxis', 'sucios/sonido.csv')
        # Elimina el archivo local después de cargarlo
        os.remove(file_path)

scraping_sonido_task = PythonOperator(
    task_id='scraping_sonido_task',
    python_callable=execute_scraping_sonido,
    dag=dag,
)

def url_taxis():
    # URL de la página con el div correspondiente
    url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
    # Obtener el HTML de la página
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def execute_scraping_taxis_actual():
    soup = url_taxis()
    # Encontrar el div con el ID correspondiente al año actual
    div_ant = soup.find('div', id=f'faq{today}')
    # Encontrar todos los enlaces dentro del div
    links = div_ant.find_all('a')
    # Filtrar los enlaces que son de Yellow Taxis o Green Taxis
    parquet_yellow_links = []
    parquet_green_links = []
    for link in links:
        if today in link['href'] and ('yellow_tripdata' in link['href']):
            parquet_yellow_links.append(link['href'])
        if today in link['href'] and ('green_tripdata' in link['href']):
            parquet_green_links.append(link['href'])
    # Descargar los archivos Parquet
    x = 0
    for link in parquet_yellow_links:
        x += 1
        with open(f'taxis_yellow_{today}-{x}', 'wb') as file:
            file.write(requests.get(link).content)
        # Ejemplo de código para descargar y cargar un archivo
        file_path = os.path.join(current_directory, f'taxis_yellow_{today}-{x}')
        upload_to_gcs(file_path, 'datasets_taxis', f'sucios/taxis_yellow_{today}-{x}.parquet')
        # Elimina el archivo local después de cargarlo
        os.remove(file_path)
    x = 0
    for link in parquet_green_links:
        x += 1
        with open(f'taxis_green_{today}-{x}', 'wb') as file:
            file.write(requests.get(link).content)
        # Ejemplo de código para descargar y cargar un archivo
        file_path = os.path.join(current_directory, f'taxis_green_{today}-{x}')
        upload_to_gcs(file_path, 'datasets_taxis', f'sucios/taxis_green_{today}-{x}.parquet')
        # Elimina el archivo local después de cargarlo
        os.remove(file_path)

scraping_taxis_actual_task = PythonOperator(
    task_id='scraping_taxis_actual_task',
    python_callable=execute_scraping_taxis_actual,
    dag=dag,
)

def execute_scraping_taxis_anterior():
    soup = url_taxis()
    # Encontrar el div con el ID correspondiente al año anterior
    div_ant = soup.find('div', id=f'faq{last_year}')
    # Encontrar todos los enlaces dentro del div
    links = div_ant.find_all('a')
    # Filtrar los enlaces que son de Yellow Taxis o Green Taxis
    parquet_yellow_links = []
    parquet_green_links = []
    for link in links:
        if last_year in link['href'] and ('yellow_tripdata' in link['href']):
            parquet_yellow_links.append(link['href'])
        if last_year in link['href'] and ('green_tripdata' in link['href']):
            parquet_green_links.append(link['href'])
    # Descargar los archivos Parquet
    x = 0
    for link in parquet_yellow_links:
        x += 1
        with open(f'taxis_yellow_{last_year}-{x}', 'wb') as file:
            file.write(requests.get(link).content)
                # Ejemplo de código para descargar y cargar un archivo
        file_path = os.path.join(current_directory, f'taxis_yellow_{last_year}-{x}')
        upload_to_gcs(file_path, 'datasets_taxis', f'sucios/taxis_yellow_{last_year}-{x}.parquet')
        # Elimina el archivo local después de cargarlo
        os.remove(file_path)
    x = 0
    for link in parquet_green_links:
        x += 1
        with open(f'taxis_green_{last_year}-{x}', 'wb') as file:
            file.write(requests.get(link).content)
                # Ejemplo de código para descargar y cargar un archivo
        file_path = os.path.join(current_directory, f'taxis_green_{last_year}-{x}')
        upload_to_gcs(file_path, 'datasets_taxis', f'sucios/taxis_green_{last_year}-{x}.parquet')
        # Elimina el archivo local después de cargarlo
        os.remove(file_path)

scraping_taxis_anterior_task = PythonOperator(
    task_id='scraping_taxis_anterior_task',
    python_callable=execute_scraping_taxis_anterior,
    dag=dag,
)

# Define las dependencias entre las tareas
scraping_aire_task >> scraping_sonido_task >> scraping_taxis_actual_task >> scraping_taxis_anterior_task