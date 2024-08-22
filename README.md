# Taller 2
### Taller 2 de programación de computadoras.
Integrantes: Jeyson Fernando Romero, Bryan Felipe Jaime y Juan Manuel Coronell.
<p align="center">
<img src="https://github.com/user-attachments/assets/1f82b68c-b627-471d-90cb-879caf078409" />
</p

En este Taller de la materia de programación de computadoras se podrá apreciar cual ha sido nuestro progreso como solucionadores de situaciones problema las cuales son bien definidas y finitas. Para hacer estos programas hicimos de uso de las últimas sesiones las cuales fueron: Funciones 2, Ciclos 2 y Arreglos y listas.

### Punto 1 / Separar los dígitos que componen un número entero.
```py

def digitos_de_un_numero (n=int)-> list:        # Función de órden de los dígitos de un número entero cualquiera
    if n>0:
        n = n
    elif n<0:
        n = n * (-1)
    while n>0:
        x_0 = n%10      # Último dígito del número
        A.append(x_0)   # Indexación del último dígito a la lista A
        n = n//10       # Tomar el siguiente dígito
    return A[::-1]

if __name__ == "__main__" :
    n = int(input("Ingrese un numero entero: "))
    A = []

    digitos = digitos_de_un_numero(n)

print(f"Los dígitos que componen a {n} son {digitos}")

```
Para este punto empezamos por ingresar un número entero por teclado, luego  a partir de calculos de módulo (%) y división entera (//) empezamos a sacar las unidades del número e indexarlas en una lista la cual llamamos A. Con eso fuimos sacando los dígitos, es decir que lo cálculamos repetidas veces aplicando un ciclo while, el cual sesaba cuando el residuo de la división entera fuera 0. 

Todos esos dígitos indexados en A estaban en sentido contrario, entonces para reorganizarlos de la misma manera en la que venian en el número original se aplico slicing de la siguiente forma [::-1], lo cual permite invertir el orden de los elementos en una lista.

Así lo único que faltaba era imprimir la lista y demostrar que esta contenía todos los dígitos del número ingresado por teclado.

### Punto 2 / Separar dígitos que componen unnúmero real.
```py

def digitos_de_un_numero_2 (n=float)->list:     # Función de separar los dífitos de un numero real
    if n < 0:
        n = n * (-1)

    n_entera = n // 1                           # Parte entera del número n
    n_decimal = n % 1                           # Parte decimal del número n

    while n_entera > 0:
        x_0 = n_entera % 10
        A.append(x_0)                           # Indexación de los dígitos de la parte entera
        n_entera = n_entera // 10

    while n_decimal < 1:
        x_1 = (n_decimal * 10) // 1 
        B.append(x_1)                           # Indexación de los dígitos de la parte decimal
        n_decimal = (n_decimal * 10) - x_1
        if n_decimal == 0:
            break

    lista_final= A[::-1] + B
    return lista_final

if __name__ == "__main__":
    n=float(input("Ingrese un numero real: "))
    A = []
    B = []

    resultado = digitos_de_un_numero_2(n)

print(f"Los dígitos del número {n} son {resultado}")    # Nota: Las aproximaciones que hace el sistema a los dígitos decimales hace que el programa funcione por más tiempo del que se requiere

```
El proceso para el punto dos fue bastante similar al previo, ya que se uso lo mismo para encontrar los dígitos de la parte entera, pero para la parte decimal se uso otro procedimiento. Primero se separo la parte entera de la decimal, luego la entera se descompuso con el método usado en el primer punto, y luego los decimales pasaron por el siguiente proceso:

Para poder sacar el primer decimal se multiplicaba por 10, así estos valores se moverian a la izquierda, haciendo que fueran posibles de acceder a partir de la división entera (//) y luego ser indexados en una lista distina a la usada con los enteros. Luego se repite este procedimiento hasta que los decimales sean iguales a 0. 

Una vez armadas ambas listas estas se concatenan siendo A[::-1] (invertida) y B (normal), B no se tuvo que reorganizar ya que el órden en el que se iban indexando sus dígitos era el correcto.

Ya para finalizar solo se imprimia la unión de las dos listas y se comparaba con el número original, al igual que se hacía en el punto 1.

Nota: En la parte decimal pasan cosas extrañas por la aproximación de la computadora. Literalmente aparecen valores de la nada.

### Punto 3 / ¿Son números espejo?
```py

def numero_espejo (n=int, m=int):

    n_respaldo = n                          # Se hace una copia para poder escribir el número luego
    m_respaldo = m

    while n > 0:
        x_0 = n % 10                        
        A.append(x_0)                       # Separación de los dígitos e indexación de estos
        n = n // 10                         # Tomar siguiente dígito

    while m > 0:
        x_1 = m % 10
        B.append(x_1)                       # Separación de los dígitos e indexación de estos
        m = m // 10                         # Tomar siguiente dígito

    if A[::-1] == B:                                                                # Comparar la organización de los números
        return (f"Los números {n_respaldo} y {m_respaldo} son números espejo")      # Si son números espejo

    else:
        return (f"Los números {n_respaldo} y {m_respaldo} no son números espejo")   # No son números espejo

if __name__ == "__main__":
    n = int(input("Ingrese el primer número entero: "))
    m = int(input("Ingrese el segundo número entero: "))
    A = []
    B = []

    resultado = numero_espejo (n,m)

print(resultado)

```
Como el título lo explica el problema es si don números pareciera que son uno el real y el otra la afectación de este en un espejo. EJ: 69 | 96

La solución a este problema era bastante sencillo ya que lo único que se tenía que hacer era los mismo que en los anteriores puntos con respecto a la parte entera. Siendo así lo que hicimos fue ingresar dos numeros por teclado y luego pasarlos a listas con el método ya antes usado. Luego una de estas listas se reorganiza con slicing [::-1] para poder compararla con la otra. Si ambas listas terminaron siendo iguales eso significa que los números en efecto son números espejo.

### Punto 4 / Calcule a partir de la sumatoria de Taylor una aproximación a Coseno.
```py

import math

def aproximación_de_coseno (x = float)->float:

    cosx = 0

    for wa in range (86):                               # Nota: el rango del ciclo for es 86 ya que de ahi en adelante empieza a aparecer error de que el enetero es muy largo como para convertirlo en un real

        factorial = 1                                   # Casos base para el cálculo de la aproximación de coseno       
        n = 1

        while n <= wa*2:                                # Valor del denominador en  la sumatoria
            factorial *= n          
            n += 1

        potencia = x**(2*wa)                            # Valor del numerador en la sumatoria

        signo = (-1)**wa

        cosx = cosx + (signo * (potencia/factorial))    # Sumatoria para dar la aproximación de coseno

    return cosx

if __name__ == "__main__":

    x=float(input("Ingrese el número del cual quiere saber el coseno: "))

valor_real = math.cos(x)                                # Valor real
valor_aprox = aproximación_de_coseno(x)
porcentaje = (valor_aprox * 100)/math.cos(x) - 100      # Comparación de que tan lejos está la aproximación al valor real

print (f"Con 86 iteraciones la aproximación es {valor_aprox}, mientras que el valor real es {valor_aprox}. Eso quiere decir que hay una diferencia porcentual de {porcentaje}")

```
Este punto fue retador ya que nos exigio interpretar una sumatoria matemática un tanto confusa al lenguaje de python.
![image](https://github.com/user-attachments/assets/b5ca4f30-3113-4813-95a0-8ae9240694c2)
La sumatoria de Taylor es una forma de aproximación a algun valor a partir de una sumatoria, en este caso fue Coseno.

Primero definimos por teclado el valor de x para luego ser seguido por el calculo del factorial de 2 por la cantidad de iteraciones hechas, luego el sencillo calculo de la potencia de x elevada a la 2 por iteraciones y para finalizar elevamos -1 a la iteración. Todos estos valores estan dentro de una sumatoria lo que quiere decir que se necesita ir sumando el valor de cada iteración con el previo lo cual lo hace un poco complejo. AL final solo se tuvo que definir el valor inicial del coseno el cual era 0 y en la primera iteración ya se convertia en 1 y así.

En cuanto a como funcionan la aproximación diriamos que funciona bien y la unica razón por la que se ve limitada es porque el sistema no puede llegar a cargar con tanta información que surgue d estos cálculos.

### Punto 5 / Hallar el Mínimo Común Múltiplo con metodos recursivos y iterativos.
#### 5.1 / Método recursivo.
```py

def mcd_recursivo(a, b):
    if b == 0:                                                          # Caso Base
        return a
    return mcd_recursivo(b, a % b)                                      # Cálculo del Máximo común divisor

def mcm_recursivo(a, b):
    return (a * b) // mcd_recursivo(a, b)                               # Cálculo del Mínimo común múltiplo

if __name__ == "__main__":
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

print(f"El MCM de {num1} y {num2} es: {mcm_recursivo(num1, num2)}")

```
#### 5.2 / Método iterativo.
```py

def mcd_iterativo(a, b):
    while b:
        a, b = b, a % b                                       # Cálculo del Mácimo común divisor
    return a

def mcm_iterativo(a, b):
    return (a * b) // mcd_iterativo(a, b)                     # Cálculo del Mínimo común múltiplo

if __name__ == "__main__":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

print(f"El MCM de {a} y {b} es: {mcm_iterativo(a, b)}")

```
### Punto 6 / Confirme si hay algun elemento en alguna de las dos listas que se repita en la otra.
```py

def chequeo_listas (A=list, B=list, c=int)->list:

    for i in range (c):
        if A[i] in B:                                               # Los elementos que contienen las listas se repiten
            verdadero_o_falso = True

        else:                                                       # Los elementos que contienen las no listas se repiten
            verdadero_o_falso = False

    return verdadero_o_falso


if __name__ == "__main__":
    c=int(input("Ingrese la cantidad de elementos que va a agregar a las listas: "))    # Límite para llenar las listas
    A=[]
    B=[]
    verdadero_o_falso : bool = False

    for i in range (c):
        a=input(f"Ingrese el {i+1} elemento de la primera lista: ")                     # Indexar los elementos que se quieren para la lista A
        A.append(a)

    for i in range (c):
        b=input(f"Ingrese el {i+1} elemento de la segunda lista: ")                     # Indexar los elementos que se quieren para la lista B
        B.append(b)

if chequeo_listas(A, B, c) == True:                                                     # Es verdadero
    print (f"Las listas A = {A} y B = {B} tienen elementos repetidos")

else:                                                                                   # Es falso
    print (f"Las listas A = {A} y B = {B} no tienen elementos repetidos")

```
### Punto 7 / Imprima de una lista aquellas cadenas las cuales tengan 2 o más vocales.
```py

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

```
### Punto 8 / Haga una lista de los elementos existenetes en la primera lista y ausentes en la segunda.
```py

def elementos_de_a_ausentes_en_b (A=list, B=list, c=int):

    for i in range (c):
        if A[i] in B:                                                                   # Condicional
            continue
        else:
            C.append(A[i])                                                              # Indexación elementos ausentes en B pero existentes en A

    return C

if __name__ == "__main__":
    c=int(input("Ingrese la cantidad de elementos que va a agregar a las listas: "))    # Límite para llenar las listas
    A=[]
    B=[]
    C=[]

    for i in range (c):
        a=input(f"Ingrese el {i+1} elemento de la primera lista: ")                     # Indexar los elementos que se quieren para la lista A
        A.append(a)

    for i in range (c):
        b=input(f"Ingrese el {i+1} elemento de la segunda lista: ")                     # Indexar los elementos que se quieren para la lista B
        B.append(b)

elementos_ausentes = elementos_de_a_ausentes_en_b (A, B, c)

print (f"Los elementos que estan en A = {A} y no en B = {B}, son C = {elementos_ausentes}")

```
### Punto 9 / Haga los cálculos del punto 7 del Taller 1 con un vector.
```py

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

```
### Punto 10 / Saque lo numeros divisibles por tres de un vector cualquiera (use la propiedad de divisivilidad del 3).
```py


```
