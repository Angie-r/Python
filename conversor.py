menu = """
Bienvenido al conversor de monedas 

1. Pesos colombianos
2. Quetzales
3. Dolares a quetzales

"""
opcion = input(menu)

if opcion == '1':
    #Conversion de pesos colombianos a dolares 
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

elif opcion == '2':
    #conversion de quetzales a dolares 
    quetzales = input("Cuantos quetzales tienes?")
    quetzales = float(quetzales)
    valor_dolar = 0.13
    dolares =  round(quetzales * valor_dolar, 2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dolares")

elif opcion == '3':
    #conversion dolares a quetzales
    dolares = input("Cuantos dolares tienes ")
    dolares = float(dolares)
    valor_quetzal = 7.69
    quetzales = round(dolares * valor_quetzal)
    quetzales = str(quetzales)
    print("Tienes Q"+quetzales+" Quetzales")
else:
    print('Selecciona una opcion valida')