
#----------------------------------------------------#
# ---- EJERCICIOS DE MATEMATICAS APLICADA ----- # 
#----------------------------------------------------#

#Problema 1 Escribe un código que pida al usuario ingresar un número real y determine si el número ingresado es positivo, negativo o cero.
# numero = float(input("Ingrese un número: "))

# if numero > 0: 
#     print("El número es positivo.")
# elif numero < 0:
#     print("El número es negativo.")
# else:
#     print("El número es cero.")

#------------------------------------------------------------------------------------------------
    
#Problema 2 Escribe un codigo que pida al usuario ingresar un numero entero y que determine si es par o impar.

# numero = int(input("Ingrese un número entero: "))

# if numero % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")

#------------------------------------------------------------------------------------------------
#Problema 3 Escribe un código que, mediante un ciclo *while*, sume los primeros 100 números naturales.


# contador = 1
# suma = 0

# while contador <= 100:                    
#     suma = suma + contador
#     contador = contador + 1
    
# print("La suma de los primeros 100 números naturales es:", suma)

#------------------------------------------------------------------------------------------------
#Problema 4 escribe un codigo que almacene en una variable el string "contraseña", luego el programa debe solicitar al usuario "introducir la contraseña" hasta que la palabra ingresada sea correcta.

# contraseña = "contraseña"
# entrada = ""

# while entrada != contraseña:
#     entrada = input("Introducir la contraseña: ")

#     if entrada == contraseña:
#         print("Contraseña correcta, puedes continuar.")
#         break

#     else:
#         print("Contraseña incorrecta. Inténtalo de nuevo.")

#------------------------------------------------------------------------------------------------

#Problema 5 escribe un codigo que, utilizando un ciclo for, pida al usuario ingresar un numero entero y muestre la tabla de multiplicar desde el 1 al 12  de dicho numero.
 
# numero = int(input("Ingrese un número entero: "))

# for i in range (1, 13):
#     resultado = numero * i
#     print(numero, "x", i, "=", resultado)   

