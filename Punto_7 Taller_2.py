def tiene_dos_o_mas_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = sum(1 for char in cadena if char in vocales)     # A partir del código ASCII se busca en las cadenas las vocales presentes
    return contador >= 2                                        # Cantidad de vocales en una cadena

def buscar_cadena_con_vocales(lista):
    for cadena in lista:                                        # Pasar por las cadenas buscando cual cumple la propiedad asignada
        if tiene_dos_o_mas_vocales(cadena):         
            return cadena
    return "No existe"                                          # Caso de no encontrar una cadena con dos vocales


if __name__ == "__main__":

    lista_cadenas = []
    n = int(input("¿Cuántas cadenas desea ingresar? "))         # Cantidad de cadenas

    for i in range(n):
        cadena = input(f"Ingrese la cadena {i+1}: ")
        lista_cadenas.append(cadena)                            # Indexación a la lista que se va a pasar por las funciones 

resultado = buscar_cadena_con_vocales(lista_cadenas)
print(resultado)
