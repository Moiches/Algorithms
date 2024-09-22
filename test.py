def ajustar_arreglo(arr):
    # Asegurarse de que el primer elemento sea 1
    arr[0] = 1

    # Ajustar el resto de los elementos
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1] + 1:  # Verificar si el valor actual es mayor que el anterior + 1
            arr[i] = arr[i - 1] + 1  # Ajustar para que cumpla la restricción

    return arr


# Ejemplo de uso
arr = [5, 3, 8, 10, 2]
ajustado = ajustar_arreglo(arr)
print(ajustado)
