#num1 = int(input())
#num2 = int(input())

#print(num1 + num2)


num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

print("La resta es:", num1 - num2 )
print("La multiplicacion es:", num1 * num2 )
print("La division es:", num1 / num2) 
print("El residuo es:", num1 % num2)

a = float(input("Enter num1: "))
op = input("Operador (+, -, *, /, %): ")
b =float(input("Enter num2: "))

if op == "+":
     print(a + b)
elif op == "-":
     print(a - b)
elif op == "*": 
     print(a * b)
elif op == "/":
     print(a / b)
elif op == "%":
     print(a % b)

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

print("La suma es :", num1 + num2 + num3)

numeros = input("Escribe la operacion:")
print("Resultado :", eval(numeros))

