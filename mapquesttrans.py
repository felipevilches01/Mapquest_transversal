import requests

# Función para calcular la distancia entre dos ciudades utilizando la API de MapQuest
def calcular_distancia(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=Nxsj6yJM8witnxTXhsjf6YppZyL1LmZm&from={ciudad_origen}&to={ciudad_destino}&locale=es'
    response = requests.get(url)
    data = response.json()
    distancia = data['route']['distance']
    return distancia

# Función para calcular la duración del viaje en horas, minutos y segundos
def calcular_duracion(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=Nxsj6yJM8witnxTXhsjf6YppZyL1LmZm&from={ciudad_origen}&to={ciudad_destino}&locale=es'
    response = requests.get(url)
    data = response.json()
    duracion = data['route']['formattedTime']
    return duracion

# Función para obtener las instrucciones paso a paso utilizando la API de MapQuest
def obtener_instrucciones(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=Nxsj6yJM8witnxTXhsjf6YppZyL1LmZm&from={ciudad_origen}&to={ciudad_destino}&locale=es'
    response = requests.get(url)
    data = response.json()
    instrucciones = data['route']['legs'][0]['maneuvers']
    return instrucciones

# Función para calcular el combustible requerido para el viaje en litros
def calcular_combustible(distancia):
    consumo_litros_por_km = 0.12  # Consumo promedio de combustible por kilómetro
    combustible = distancia * consumo_litros_por_km
    return combustible

# Función para imprimir la narrativa del viaje
def imprimir_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible):
    print(f"Viaje de {ciudad_origen} a {ciudad_destino}:")
    print(f"Distancia: {distancia:.1f} km")
    print(f"Duración: {duracion}")
    print(f"Combustible requerido: {combustible:.1f} litros")


# Función para imprimir las instrucciones paso a paso
def imprimir_instrucciones(instrucciones):
    print("Instrucciones para llegar al destino:")
    for i, instruccion in enumerate(instrucciones, 1):
        print(f"{i}. {instruccion['narrative']}")

# Programa principal
print("Programa Tu Viaje Con MapQuest!")
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

distancia = calcular_distancia(ciudad_origen, ciudad_destino)
duracion = calcular_duracion(ciudad_origen, ciudad_destino)
combustible = calcular_combustible(distancia)
instrucciones = obtener_instrucciones(ciudad_origen, ciudad_destino)

imprimir_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible)
imprimir_instrucciones(instrucciones)

while True:
    opcion = input("Presione 's' para salir: ")
    if opcion.lower() == 's':
        break

import requests

# Función para calcular la distancia entre dos ciudades utilizando la API de MapQuest
def calcular_distancia(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=Nxsj6yJM8witnxTXhsjf6YppZyL1LmZm&from={ciudad_origen}&to={ciudad_destino}&locale=es'
    response = requests.get(url)
    data = response.json()
    distancia = data['route']['distance']
    return distancia

# Función para calcular la duración del viaje en horas, minutos y segundos
def calcular_duracion(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=Nxsj6yJM8witnxTXhsjf6YppZyL1LmZm&from={ciudad_origen}&to={ciudad_destino}&locale=es'
    response = requests.get(url)
    data = response.json()
    duracion = data['route']['formattedTime']
    return duracion

# Función para obtener las instrucciones paso a paso utilizando la API de MapQuest
def obtener_instrucciones(ciudad_origen, ciudad_destino):
    url = f'http://www.mapquestapi.com/directions/v2/route?key=Nxsj6yJM8witnxTXhsjf6YppZyL1LmZm&from={ciudad_origen}&to={ciudad_destino}&locale=es'
    response = requests.get(url)
    data = response.json()
    instrucciones = data['route']['legs'][0]['maneuvers']
    return instrucciones

# Función para calcular el combustible requerido para el viaje en litros
def calcular_combustible(distancia):
    consumo_litros_por_km = 0.12  # Consumo promedio de combustible por kilómetro
    combustible = distancia * consumo_litros_por_km
    return combustible

# Función para imprimir la narrativa del viaje
def imprimir_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible):
    print(f"Viaje de {ciudad_origen} a {ciudad_destino}:")
    print(f"Distancia: {distancia:.1f} km")
    print(f"Duración: {duracion}")
    print(f"Combustible requerido: {combustible:.1f} litros")

# Función para imprimir las instrucciones paso a paso
def imprimir_instrucciones(instrucciones):
    print("Instrucciones para llegar al destino:")
    for i, instruccion in enumerate(instrucciones, 1):
        print(f"{i}. {instruccion['narrative']}")

# Programa principal
print("Programa Tu Viaje Con MapQuest!")
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

distancia = calcular_distancia(ciudad_origen, ciudad_destino)
duracion = calcular_duracion(ciudad_origen, ciudad_destino)
combustible = calcular_combustible(distancia)
instrucciones = obtener_instrucciones(ciudad_origen, ciudad_destino)

imprimir_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible)
imprimir_instrucciones(instrucciones)


while True:
    opcion = input("Presione 's' para salir: ")
    if opcion.lower() == 's':
        break
