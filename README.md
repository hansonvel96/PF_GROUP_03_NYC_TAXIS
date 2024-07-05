![Banner](https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/henry.jfif)
<h1 align="center">DATA SCIENCE - PROYECTO FINAL GRUPAL</h1>
<h1 align="center">Taxis sustentables en Nueva York</h1>

<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/taxi.png" height="350" width="auto" alt="Imagen">
</p>

<h1>Herramientas  y Tecnologias</h1>
Para este proyecto de <strong>Data Science</strong> utilizamos las siguientes <strong>herramientas</strong>: 
<br>
<br>
<strong>1. Github</strong>
<br>
Se empleará GitHub para la <strong>gestión del código fuente, seguimiento de cambios, colaboración en el desarrollo y documentación del proyecto,</strong> garantizando un flujo de trabajo organizado y eficiente en el desarrollo de software y análisis de datos.
<br>
<br>
<strong>2. Google Drive</strong>
<br>
Será utilizado para la colaboración en equipo, <strong>la gestión de documentos, presentaciones</strong>, facilitando la comunicación y el trabajo coordinado entre los miembros del equipo.
<br>
<br>
<strong>3. Python</strong>
<br>
Será utilizado para analizar grandes conjuntos de datos de tráfico, calidad del aire y sonora, aprovechando <strong>librerías como Pandas</strong> para la manipulación y análisis de datos estructurados, <strong>y Scikit-learn</strong> para el desarrollo de modelos de machine learning. <strong>Python nos permitirá procesar y analizar eficientemente los datos</strong>, así como desarrollar algoritmos predictivos y de clasificación necesarios para entender las dinámicas del tráfico y su impacto ambiental.
<br>
<br>
<strong>4. Google Cloud Storage</strong>
<br>
Cloud Storage <strong>será utilizado para almacenar de manera segura y eficiente los grandes volúmenes de datos recopilados durante el proyecto</strong>, desde datos brutos hasta resultados procesados y modelos de machine learning.
<br>
<br>
<strong>5. Google Cloud BigQuery</strong>
<br><strong>Será utilizado BigQuery para consolidar y analizar grandes volúmenes de datos de diferentes fuentes</strong>. Su capacidad para manejar consultas complejas y grandes conjuntos de datos nos permitirá identificar patrones y tendencias en el tráfico.
<br>
<br>
<strong>6. Power BI </strong>
<br>
Se utilizará esta herramienta <strong>para crear un dashboard interactivo </strong>que refleje el análisis de datos hecho.
<br>
<br>


<h1>Contexto</h1>
<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/taxi-sustemtable.png" height="350" width="auto" alt="Imagen">
</p>

<p>Los servicios de transporte en Nueva York, como los <strong>taxis</strong> y Uber, han <strong>revolucionado la movilidad urbana</strong>. Estas alternativas ofrecen una forma conveniente y accesible de desplazarse, transformando la percepción sobre el transporte público y el alquiler de coches.</p>

<p><strong>El problema del cambio climático</strong>, provocado en gran medida por el uso de energías provenientes de combustibles fósiles en los vehículos, <strong>ha alcanzado niveles críticos</strong>. Las compañías se ven instadas a actuar frente a estos desafíos ambientales, lo que implica la necesidad de medir y mejorar los niveles de consumo y generación energética. <strong>Esta conciencia conduce a la búsqueda de soluciones</strong> para mitigar dicho impacto en el medio ambiente.</p>
<br>

<h1>Cliente</h1>
<p> <strong>Una empresa de transporte de larga y media distancia</strong>, que hace uso de vehículos tipo “ómnibus”, quiere dar el salto a brindar el servicio de transporte a través de automóviles, con la considerable diferencia de que estos “taxis” ayuden a crear un <strong>futuro menos contaminante</strong>, tanto del aire como del espacio sonoro, manteniendo un buen servicio a la hora de brindarlo. El problema es que la empresa no cuenta aún con la información necesaria.</p>
<br>

<h1>Objetivos</h1>
<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/dasb.png" height="350" width="auto" alt="Imagen">
</p>
Teniendo en cuenta el contexto, proponemos los siguientes objetivos a cumplir:
<ul>
  <br>
  <li><strong>Recopilar, depurar y disponibilizar información</strong> que el cliente solicita para ayudar a la toma de decisiones.</li>
  <li><strong>Desarrollar un MVP</strong> (Mínimo Producto Viable) para mostrar al cliente.</li>
</ul>​
<br>
<br>

<h1>ETL</h1>
<br>
En esta instancia <strong>realizamos un proceso de ETL (Extracción, Transformación y Carga) de los datos </strong>y validación de los mismos, para posteriormente generar un proceso de automatización en la nube. En este proceso de ETL <strong>se eliminaron columnas que no se iban a utilizar, se renombraron otras, y se transformaron los archivos a la extensión .parquet</strong> para poder ser disponibilizados en la nube.

<br>
<h1>EDA</h1>
Para este proyecto realizamos un EDA (Análisis Exploratorio de los datos) que nos permitió entre otras cosas:
<ul>
  <br>
  <li><strong>Verificar la existencia de valores nulos</strong></li>
  <li><strong>Verificar la existencia</strong> de <strong>valores duplicados</strong></li>
  <li><strong>Verificar la existencia</strong> de <strong>valores outliers</strong></li>
  <li><strong>Crear gráficos</strong> de <strong>para representar los datos obtenidos</strong></li>
</ul>
<br>
<strong>Algunos de los gráficos</strong> representados son los siguientes:
<br>
<br>
<ins>Cantidad de viajes por distrito</ins>
<br>
<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/distrito.png" height="450" width="auto" alt="Imagen">
</p>
En este gráfico podemos observar <strong>Manhattan es el distrito con màs viajes hechos en taxi en Nueva York</strong>, seguido de Queens y luego Brooklyn. Sorprendentemente, si analizamos los datos, vemos que Manhattan no es el distrito con mayor cantidad de habitantes (1.593.200), sino que es Brooklyn con 2.511.408 habitantes. Sin embargo, <strong>al ser el núcleo financiero de Nueva York y al ser un centro turístico muy importante genera una enorme movilidad de los ciudadanos y los turistas a través de medios como los taxis</strong>.
<br>
<br>
<ins>Histórico de viajes de taxis verdes</ins>
<br>
<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/historico-taxis.png" height="350" width="auto" alt="Imagen">
</p>
En este gráfico podemos observar que en lo que fue <strong>Enero de 2024</strong>, los taxis verdes tuvieron una gran amplitud en lo que respecta al número de viajes, ubicandose <strong>la menor cantidad de viajes en torno a los 1000 en un día</strong> y llegando a un <strong>pico máximo de 2220 viajes en otro día</strong>. Es decir, en un día se realizaron el doble de viajes de lo que fue el peor día.
<br>
<br>
<ins>Duración promedio por viaje de taxis verdes</ins>
<br>
<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/duracion.png" height="350" width="auto" alt="Imagen">
</p>
En este gráfico podemos observar que la duración de los viajes en taxis verdes en Enero de 2024 tiene una gran amplitud. <strong>El viaje con menos duración ronda los 13.7 minutos, mientras que el viaje con mayor duración es de aproximadamente 23.3 minutos.</strong>
<br>
<br>
<h1>Pipeline</h1>
Para este proyecto realizamos el siguiente Pipeline teniendo en cuenta el <strong>ciclo de vida del dato: </strong>
<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/pipeline.png" height="450" width="auto" alt="Imagen">
</p>
<br>
<h1>KPI'S</h1>
Teniendo en cuenta los objetivos planteados <strong>proponemos los siguientes KPI’s</strong>:
<ul>
  <br>
  <li><strong>Aumento de un 5% del uso de los taxis verdes</strong> con <strong>respecto al último semestre.</strong></li>
  <br>
  <li><strong>Reducción de un 5% en la Emisión de CO2</strong> por kilómetro recorrido para el último año que el cliente solicita para ayudar a la toma de decisiones.</li>
  <br>
  <li><strong>Reducción en un 2% los niveles de nontaminación sonora </strong>por zona para el total de viajes realizados el último semestre, con la utilización de vehículos eléctricos vs vehículos a combustión para lo que va de año</li>
</ul>

<br>

<h1>Machine Learning</h1>
<br>
Teniendo en cuenta los objetivos planteados <strong>creamos 3 modelos de Machine Learning</strong>:
<ul>
  <br>
  <li><strong>Modelo que recomienda 5 modelos de automóviles a combustión</strong> de una marca especifica que produzcan menos contaminación utilizando Regresión Logística.</li>
  <br>
  <li><strong>Modelo que recomienda 5 modelos de automóviles eléctricos</strong> de una marca especifica que tengan la mejor eficiencia y autonomia, utilizando Regresión Lineal.</li>
  <br>
  <li><strong>Modelo que predice la cantidad de viajes de taxis por hora y localización </strong> utilizando Random forest.</li>
</ul>
<br>
<h1>Dashboard</h1>
<br>
Teniendo en cuenta los objetivos planteados <strong>propusimos el siguiente dashboard</strong>:
<br>
<br>
<br>
<p align="center">
  <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/blob/main/Imagenes/logo.png" height="450" width="auto" alt="Imagen">
</p>
<br>
<h1>Observaciones finales</h1>
<br>
<br>
En base a los datos recopilados llegamos a las siguientes <strong>observaciones finales</strong>:
<ul>
  <br>
  <li><strong>Los taxis amarillos generan altos niveles de contaminación por C02 a diferencia de los taxis verdes</strong>, cuya contaminación en este nivel es nula.</li>
  <br>
  <li><strong>Manhattan es el distrito con más cantidad de viajes hechos</strong>, llegando a los 46 millones de viajes por año, muy por encima de Queens que es el segundo con 5 millones.</li>
  <br>
  <li><strong>Brooklyn es el distrito con más contaminación medioambiental y Manhattanes el distrito con más contaminación sonora</strong>.</li>
  <br>
  <li><strong>Chevrolet y GMC</strong> son las marcas de autos más contaminantes.</li>
  <br>
  <li><strong>Los modelos Silverado 4WD y Sierra 4WD son los autos que más C02 producen.</strong></li>
</ul>
<br>
<h1>Integrantes</h1>
<br>
<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: nowrap; overflow-x: auto;">
    <div style="display: flex; flex-direction:row">
        <div style="display: flex; justify-content:center" >
           <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/raw/main/Imagenes/agusto.png" alt="agusto" style="width: 150px; height: 200px; border-radius: 50%;">
           <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/raw/main/Imagenes/alan.png" alt="alan" style="width: 150px; height: 200px; border-radius: 50%;">
           <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/raw/main/Imagenes/hanson.png" alt="hanson" style="width: 150px; height: 200px; border-radius: 50%;">
           <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/raw/main/Imagenes/ian.png" alt="ian" style="width: 150px; height: 200px; border-radius: 50%;">
           <img src="https://github.com/hansonvel96/PF_GROUP_03_NYC_TAXIS/raw/main/Imagenes/octavio.png" alt="octavio" style="width: 150px; height: 200px; border-radius: 50%;">
        </div>
  </div>
    
           
       
</div>


