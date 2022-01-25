

#Conversion de pesos colombianos a dolares 
pesos = input("¿Cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")


#conversion de quetzales a dolares 
quetzales = input("Cuantos quetzales tienes?")
quetzales = float(quetzales)
valor_dolar = 0.13
dolares =  round(quetzales * valor_dolar, 2)
dolares = str(dolares)
print("Tienes $"+ dolares + " dolares")

#conversion dolares a quetzales
dolares = input("Cuantos dolares tienes ")
dolares = float(dolares)
valor_quetzal = 7.69
quetzales = round(dolares * valor_quetzal)
quetzales = str(quetzales)
print("Tienes Q"+quetzales+" Quetzales")