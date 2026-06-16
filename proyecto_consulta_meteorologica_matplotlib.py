import matplotlib.pyplot as plt
import pandas as pd

# PROGRAMA DE CONSULTA METEOROLÓGICA INTERACTIVA (ARGENTINA - AÑO 2023)
ruta = "C:/Users/noeli/Desktop/Big Data IA/Matplotlib/Proyecto Consulta Meteorológica Matplotlib/Datos+Meteorológicos_Arg_2023.csv"
df = pd.read_csv(ruta)

# 1. Limpieza de datos
print(df.info()) # Con info vemos varios datos del archivo, entre ellos que no tiene datos nulos
print(df.duplicated().any()) # tampoco tiene filas duplicadas
print(df.head(10)) # mostramos los 10 primeros registros para formarnos una idea

# Corregimos el tipo de dato de "Fecha"
df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%Y")

# 2. Pedimos al usuario los datos de consulta (ciudad y mes) a través de la función consultar_temperaturas(), lo cual genera un código más
# limpio, ordenado y reutilizable.

ciudades = df["Ciudad"].drop_duplicates() # generamos una Serie con los nombres de las ciudades

df["Mes"] = df["Fecha"].dt.month_name(locale="es_ES") # añadimos la columna Mes a nuestro df, con el nombre del mes en español.
meses = df["Mes"].drop_duplicates() # generamos una Serie con los nombres de los meses

def consultar_temperaturas():
    while True:    
        ciudad_encontrada = "" # añadimos las variables de búsqueda al inicio para resetearlas
        mes_encontrado = ""
        print(f"Estas son las ciudades disponibles: \n{ciudades}")
        ciudad_buscada = input("Elija una ciudad para consultar sus temperaturas  máximas y mínimas: ")

        for c in ciudades:
            if c.lower() == ciudad_buscada.lower():
                ciudad_encontrada = c
                mes_buscado = input("Indique el nombre del mes: ")
                for m in meses:
                    if m.lower() == mes_buscado.lower():
                        mes_encontrado = m
                        
                        # 3. Generación del gráfico
                        # 3.1 Generamos un nuevo df filtrado por la ciudad y el mes escogidos
                        df_filtrado = df[(df["Ciudad"] == ciudad_encontrada) & (df["Mes"] == mes_encontrado)]

                        # 3.2 Ahora creamos el gráfico de tipo line plot. Es un solo gráfico con dos líneas (temp. máximas y temp. mínimas)
                        fig, ax = plt.subplots() # creamos la figura y sus axs para configurar el gráfico con la interfaz POO 

                        ax.plot(df_filtrado["Fecha"], df_filtrado["Temperatura Maxima"], label="Temperatura Máxima", 
                                color="red", marker="o")
                        ax.plot(df_filtrado["Fecha"], df_filtrado["Temperatura Minima"], label="Temperatura Mínima", 
                                color="blue", marker="d")
                        
                        ax.legend() # con legend permitimos que las labels se visualicen dentro del gráfico
                        
                        ax.tick_params(axis="x", rotation=45) # rotamos las fechas de la x para que quepan en la figura.

                        ax.grid(True) # activamos la cuadrícula de fondo

                        ax.set_xlabel("Fecha") # agregamos labels al eje de las x y de las y
                        ax.set_ylabel("Temperatura (°C)")

                        ax.set_title(f"Temperaturas de {ciudad_encontrada} en {mes_encontrado}")
                        
                        plt.show()

        if not ciudad_encontrada:
            print("No se ha encontrado ninguna ciudad con dicho nombre")
            continue
        if not mes_encontrado:
            print("No existe ningún mes con ese nombre")
            continue

        otra_consulta = input("¿Desea hacer otra consulta? (si/no): ")
        if otra_consulta.lower() != "si":
            print("Hasta luego!")
            break

consultar_temperaturas()