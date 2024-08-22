def promedio_calculo (numeros=list)->float:                                         # Todas las funciones del problema 7 del Taller 1
    valor_promedio = sum(numeros) / len(numeros)
    return valor_promedio

def mediana_calculo (numeros=list)->float:
    numeros_ordenados = sorted(numeros)
    valor_mediana = numeros_ordenados[2]
    return valor_mediana

def promedio_multiplicativo_calculo (numeros=list)->float:
    multi = 1
    for num in numeros:
        multi = multi * num
    valor_pormedio_multi = multi**(1/5)
    return valor_pormedio_multi

def numeros_ascendentemente (numeros=list)->list:
    orden_numeros_ascendentes = sorted(numeros)
    return orden_numeros_ascendentes

def numeros_descendentemente (numeros=list)->list:
    orden_numeros_descendente = sorted(numeros, reverse = True)
    return orden_numeros_descendente

def mayor_elevado_menor_calculo (numeros=list)->float:
    numeros_ordenados = sorted(numeros)
    mayor_a_la_menor = numeros_ordenados[4] ** numeros_ordenados [0]
    return mayor_a_la_menor

def raiz_cubica_del_menor_calculo (numeros=list)->float:
    numeros_ordenados = sorted(numeros)
    menor_raiz_cubica = numeros_ordenados[0] ** (1/3)
    return menor_raiz_cubica

if __name__ == "__main__":

    numeros = []
    for i in range(5):
        num = float(input(f"Ingrese el número {i+1}: "))                                # Crear el vector con un total de cinco valores
        numeros.append(num)

promedio = promedio_calculo (numeros)                                                   # La totalidad de los llamados a las funciones
mediana = mediana_calculo (numeros)
promedio_multiplicativo = promedio_multiplicativo_calculo (numeros)
numeros_ascendente = numeros_ascendentemente (numeros)
numeros_descendente = numeros_descendentemente (numeros)
potencia = mayor_elevado_menor_calculo (numeros)
menor_raiz_cubica = raiz_cubica_del_menor_calculo (numeros)

print(f"El promedio es: {promedio}")                                                     # Resultados 
print(f"La mediana es: {mediana}")
print(f"El promedio multiplicativo es: {promedio_multiplicativo}")
print(f"Números ordenados de forma ascendente: {numeros_ascendente}")
print(f"Números ordenados de forma descendente: {numeros_descendente}")
print(f"La potencia del mayor número elevado al menor número es: {potencia}")
print(f"La raíz cúbica del menor número es: {menor_raiz_cubica}")