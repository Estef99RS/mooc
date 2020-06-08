def sumatorio(num):
    result = 0
    for i in range(1, num + 1):
        result = result + i

    return result


name = input("Por favor, introduce tu nombre: ")
print("Hola " + name + "!")
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
result = num1 * num2
print("El resultado es: ", result)

suma = sumatorio(5)
print("La suma de los cinco primeros números naturales es: ", suma)
