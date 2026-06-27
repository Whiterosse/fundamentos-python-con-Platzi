import operadores

print(operadores.sumar(5, 2))
print(operadores.dividir(5, 2))
print(operadores.restar(5, 2))
print(operadores.multiplicar(5, 2))

print("=======================================================\n")
# la otra manera para evitar llamarlo desde la impresion es:

from operadores import dividir, multiplicar, restar, sumar

print(sumar(7, 20))
print(dividir(7, 20))
print(restar(7, 20))
print(multiplicar(7, 20))
