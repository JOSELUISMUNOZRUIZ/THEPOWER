# 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.


def fibonacci(n):
    a = 1
    b = 1
    if n == 1:
        print("0")
    elif n == 2:
        print("0", "1")
    else:
        print("0")
        print(a)
        print(b)
        for i in range(n - 3):
            total = a + b
            b = a
            a = total
            print(total)


fibonacci(8)

# Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.


def divisores(numero):
    resultado = [i for i in range(1, numero + 1) if numero % i == 0]
    return resultado


print(divisores(6))

# Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original


def unicos(lista):
    return set(lista)


nlista = [2, 3, 4, 5, 5, 6]
resultado = unicos(nlista)
print(resultado)

# Define una función que tome un número y retorne la suma de sus dígitos.
