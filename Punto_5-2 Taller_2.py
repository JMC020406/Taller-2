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
