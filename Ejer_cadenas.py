# https://aprendeconalf.es/docencia/python/ejercicios/cadenas/ - se agrega link de los ejecicios


# Pedir nombre y numero entero, imprimir el nombre las veces que se ingreso al inicio.
#nombre = input('Ingresa tu nombre')
#numero = int(input('Ingresa un numero entero '))

#print((nombre + '\n') * int(numero))

#Programa que solicite el ingreso del nombre completo, y luego lo imprima 3 veces
# 1. todas las letras minisculas 2. Todas las letras mayus, 3. Primera inicial mayus 
#nombre = input(str('Ingresa tu nombre completo '))
#print(nombre.lower())
#print(nombre.upper())
#print(nombre.title())

# Programa que pregunte nombre, lo imprima y e indique el numero de letas.
#nombre = input(str('Ingresa tu nombre '))
#nombre = nombre.replace(' ','')
#print('Gracias '+ nombre.upper() + ' su nombre tiene ' + str(len(nombre.replace(' ','')))+ 
#' letras')

# programa que pida no. telefono con prefijo- numero - extension.
#numero = input('Ingrese numero de telefono prefijo + numero + extension ')
#print('El numero es '+ numero[4:-3])

#Ingresa frase y que lo imprima de forma invertida
frase = input('Ingresa una frase ')
print(frase[::-1])

#ingresa una frase y una vocal, al imprimir agregara la vocal que se agrego en mayusculas
frase = input('Ingresa una frase ')
vocal = input('Ingresa una vocal ')
frase = frase.replace(vocal,vocal.upper())
print(frase)
