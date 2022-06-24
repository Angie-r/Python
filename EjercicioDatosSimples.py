import imp
from xml.dom.expatbuilder import InternalSubsetExtractor
from pyrsistent import b



print('Hola Mundo')

# Imprimir un texto guardado en una variable
saludo = 'Hola mundo'
print(saludo)

# Solicitar nombre de la persona y que imprima el saludo.
nombre = input('Ingresa tu nombre ')
print('Hola! '+ nombre)

# resultado de la operacion (3+2/2*5)^2

operacion = ((3+2)/(2*5))**2
print(operacion)

# preguntar horas trabajadas y el valor por hora.
#hora_trabajada = int(input('Ingresa las horas laboradas '))
#valor_hora = int(input('Ingresa el coste de la hora '))
#coste_a_pagar = hora_trabajada * valor_hora
#print(str(coste_a_pagar))

# programa que lea un entero positivo, y sume todos los enteros desde 1 hasta n
#entero = int(input('Ingresa un numero entero '))
#suma = entero*(entero+1)/2
#print("La suma de los primeros numero enteros desde 1 hasta "+ str(entero) +" es "+ str(suma))

# Calcular la masa corporal 
peso = float(input('Ingrese su peso en kg'))
altura = float(input('Ingrese su altura en metros'))
imc = round(peso/(altura**2),2)
print('Su masa corporal es de ' + str(imc))

# Calcular el cociente y resto de la division.
#n = float(input('Ingresa el primer numero '))
#m = float(input('Ingresa el segundo numero '))
#c = round((n / m),2)
#r = n % m
#print('El cociente de la division es '+ str(c) + ' el resto es '+ str(r))

# calculo de capital obtenido, segun cantidad a invertir, interes y numero de años.
#cantidad_invertir = int(input('Ingrese la cantidad que desea invertir Q'))
#interes = float(input('ingrese el % de interes anual '))
#años = int(input('ingrese la cantidad de años de inversion '))
#capital = (cantidad_invertir * (interes /100))* años
#print('La cantidad inicial ' + str(cantidad_invertir)+ 'con el interes del %'+ str(interes)+ 
#' con plazo de '+ str(años) + ' años, se obtiene un capital de Q'+ str(capital))

#jugueteria payasos 112g, muñecas 75g
#p = int(input('Ingres la cantidad de payasos vendidos '))
#m = int(input('Ingrese la cantidad de muñecas '))
#peso = (p * 112) + (m * 75)
#print('Se vendieron '+ str(p)+' payasos '+ str(m)+' muñecas, el paquete tiene un peso de '
# + str(peso)+ ' kg')

# ahorro 4% anual calculo del primer, segundo y tercer año
ahorro = float(input('Ingrese la cantidad inicial ahorrada '))
interes = 0.04
saldo = ahorro * (1 + interes)
print('El interes sobre lo ahorrado en el primer año es '+ str(round(saldo,2)))
saldo2 = saldo * (1 + interes)
print('El interes sobre lo ahorrado en el segundo año es '+ str(round(saldo2,2)))
saldo3 = saldo2 * (1+ interes)
print('El interes sobre lo ahorrado en el tercer año es '+ str(round(saldo3,2)))

#Barras de pan Q3.49 c/u. si no es del dia tiene descuento de 60%. programa que lea
#las barras vendidas que no son del dia, luego mostrar el precio habitual, el descuento reali
#y el coste final total

barras_vendidas = int(input('Ingresa el no. de barras vendidas que no son del dia '))
precio_normal = 3.49
desc = 0.60

venta = barras_vendidas + precio_normal
print('El precio habitual es de Q'+ str(round(venta,2)))

venta_desc = barras_vendidas * desc
print('Se realiza descuento de %60 por no ser pan del dia, siendo un total de Q'
+ str(round(venta_desc,2)))


