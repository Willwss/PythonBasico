def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

numero = int(input("Informe um número: "))

    fib_numero = fibonacci(numero)

    if fib_numero == numero:
     print(f"{numero} pertence à sequência de Fibonacci.")
    else:
     print(f"{numero} não pertence à sequência de Fibonacci.")

