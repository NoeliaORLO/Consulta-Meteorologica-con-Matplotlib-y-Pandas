# Proyecto de consulta meteorológica con Matplotlib y Pandas 🌡️⛈️
Proyecto que permite consultar las temperaturas máximas y mínimas de ciudades de Argentina en el año 2023, generando un gráfico con Matplotlib.

## ¿Qué pretende este proyecto?
Este es mi tercer proyecto en el ámbito del Data Science, en el cual introduzco Matplotlib para generar gráficos a partir de consultas sobre los datos de un DataFrame obtenido desde un archivo CSV.

Primero genero un DataFrame a partir del archivo csv, al cual aplico un análisis básico y tratamiento de datos. Posteriormente, según la ciudad y el mes elegidos por el usuario, creo un DataFrame filtrado por estos parámetros. 

A partir de él se genera un gráfico de tipo line plot con dos líneas: una para las temperaturas máximas y otra para las mínimas, ambas en el eje Y. El gráfico incluye cuadrícula (grid), labels para cada eje y su leyenda mediante legend(), rotación de fechas con tick_params(), y marcadores de distinto estilo y color para cada línea. 

Es un programa interactivo que permite generar tantos gráficos como se desee, combinando conocimientos de Python, Pandas y Matplotlib.

## Para ejecutar el script
Se necesita un intérprete de Python con las librerías Pandas y Matplotlib instaladas (en mis proyectos uso conda, obtenible mediante la descarga de Anaconda)
Respecto a Matplotlib, se importa el módulo pyplot, que es el que permite generar los gráficos `import matplotlib.pyplot as plt` 😊

