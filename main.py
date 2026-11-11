#num1 = int(input())
#num2 = int(input())

#print(num1 + num2)

def calculadora():
    print("--- CALCULADORA SIMPLIFICADA ---")
    print("1. Restar (a - b)")
    print("2. Multiplicar (a * b)")
    print("3. Dividir (a / b)")
    print("4. Módulo (a % b)")
    print("5. Sumar 3 números")
    print("6. Expresión combinada (ej: 2 + 4 - 3 o 4 * 5 + 1 / 3)")

    opcion = input("Elige una opción (1-6): ")

if opcion in ['1', '2', '3', '4']:
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    
    if opcion == '1':
        print("Resultado:", a - b)
    elif opcion == '2':
        print("Resultado:", a * b)
    elif opcion == '3':
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Error: No se puede dividir entre cero.")
    elif opcion == '4':
        print("Resultado:", a % b)

elif opcion == '5':
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    c = float(input("Tercer número: "))
    print("Resultado:", a + b + c)

elif opcion == '6':
    operacion = input("Escribe la operación (ej. 4 * 5 + 1 / 3): ")
    print("Resultado:", eval(operacion))

else:
    print("Opción no válida.")