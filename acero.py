# Importa las librerías necesarias
import subprocess

subprocess.run(["pip", "install", "requests"])
subprocess.run(["pip", "install", "pandas"])
subprocess.run(["pip", "install", "openpyxl"])

import requests
import pandas as pd
import openpyxl

# Lista de símbolos de acciones de compañías siderúrgicas en diferentes países
symbols = ["AA", "NUE", "CLF", "TS", "STLD"]

# Diccionario con los nombres de las compañías y los países correspondientes
companies = {
    "AA": "EE.UU.",
    "NUE": "EE.UU.",
    "CLF": "EE.UU.",
    "TS": "Canadá",
    "STLD": "EE.UU."
}

# Lista vacía donde se guardarán los precios del acero
prices = []

# Iteramos sobre la lista de símbolos
for symbol in symbols:
    # URL de la API de Alpha Vantage que proporciona precios del acero en tiempo real
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=YOUR_API_KEY"

    # Enviamos una solicitud HTTP a la API y obtenemos la respuesta
    response = requests.get(url)

    # Procesamos la respuesta de la API para obtener el precio del acero
    data = response.json()
    price = float(data["Global Quote"]["05. price"])

    # Creamos un diccionario con los datos del precio del acero
    data = {
        "company": companies[symbol],
        "price": price
    }

    # Añadimos el diccionario a la lista de precios
    prices.append(data)


# Función que escribe los datos en el archivo de Excel



# Creamos el archivo de Excel

writer = pd.ExcelWriter(r"C:\Users\gccic\OneDrive\Desktop\precios_del_acero.xlsx", engine="openpyxl")

# Creamos un dataframe con los datos
df = pd.DataFrame(prices)

# Escribimos el dataframe en la hoja de cálculo "Precios del acero"
df.to_excel(writer, index=False, sheet_name="Precios del acero")

# Guardamos el archivo de Excel
writer.save()

# Llamamos a la función para escribir los datos en el archivo de Excel
write_to_excel()

# Mostramos el precio promedio del acero a nivel mundial en diferentes intervalos de tiempo
print(f"Precio promedio del acero a nivel mundial hoy: ${day_avg:.2f}")
print(f"Precio promedio del acero a nivel mundial en los últimos 15 días: ${fifteen_day_avg:.2f}")
print(f"Precio promedio del acero a nivel mundial en el último mes: ${month_avg:.2f}")
print(f"Precio promedio del acero a nivel mundial en el último año: ${year_avg:.2f}")

# Mostramos los precios del acero en cada país
for price in prices:
    print(f"Precio del acero en {price['company']}: ${price['price']:.2f}")

