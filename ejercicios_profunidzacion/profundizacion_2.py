# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:

    
    try:

        numero_1 = float(input('Ingrese el primer número\n'))   
        
        numero_2 = float(input('Ingrese el segundo número\n'))

        operacion = input('''Introdusca la operacion a realizar 
        Suma (+)
        Resta (-)
        Multiplicación (*)
        División (/)
        Exponente/Potencia (**)
        Introdusca "Fin" para terminar\n''')  
    
    except ValueError:
        
        print("El valor introducido es erroneo, vuelva a intentarlo")
        continue

    if operacion.lower() == "fin":

        break

    elif operacion == "+":

        suma = numero_1 + numero_2

        print("la operacion introducida es Suma entre", numero_1, " y ", numero_2, " y el resultado es ", suma)

    elif operacion == "-":

        resta = numero_1 - numero_2

        print("la operacion introducida es Resta entre", numero_1, " y ", numero_2, " y el resultado es ", resta)

    elif operacion == "*":

        multiplicacion = numero_1 * numero_2

        print("la operacion introducida es Multipliicacion entre", numero_1, " y ", numero_2, " y el resultado es ", multiplicacion)

    elif operacion == "/":

        division = numero_1 / numero_2
        
        print("la operacion introducida es Division entre", numero_1, " y ", numero_2, " y el resultado es ", division)

    elif operacion == "**":

        exponente = numero_1 ** numero_2
        
        print("la operacion introducida es Esponente/Potencia entre", numero_1, " y ", numero_2, " y el resultado es ", exponente)

    else:

        print("Error, no se introdujo un operador correcto. Vuelva a Intentarlo")

print("Fin del Programa")