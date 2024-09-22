#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTemperature' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/weather?name=<name>
#
# The function is expected to return an Integer.
# The function accepts a singe parameter name.
#

import requests


def getTemperature(name):
    # URL de la API con el nombre de la ciudad
    url = f"https://jsonmock.hackerrank.com/api/weather?name={name}"

    # Realizar la solicitud GET a la API
    response = requests.get(url)

    # Convertir la respuesta a formato JSON
    data = response.json()

    # Obtener el primer registro de la respuesta
    if data['data']:
        weather_info = data['data'][0]

        # Extraer la cadena de temperatura del campo "weather"
        weather_str = weather_info['weather']

        # Extraer el número de la temperatura (que está antes de la palabra "degree")
        temperature = int(weather_str.split()[0])

        return temperature
    else:
        # Si no hay datos, devolver None o algún valor apropiado
        return None


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    name = input()

    result = getTemperature(name)

    fptr.write(str(result) + '\n')

    fptr.close()
