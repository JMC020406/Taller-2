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