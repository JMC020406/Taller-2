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