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

