# Funcion para convertir a dolares
def conversor(tipo_moneda,valor_dolar):
    pesos = input("Cuantos pesos " + tipo_moneda + " tienes?: ")
    pesos = float(pesos)
    dolar = pesos/valor_dolar
    dolar = round(dolar,2)
    dolar = str(dolar)
    print("Tienes $" + dolar + " dolares")

menu = """
Bienvenido al conversor de monedas 👌
Para los emojis: windows + .

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos",3875)
elif opcion == 2:
    conversor("argentinos", 125)
elif opcion ==3 :
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción correcta")

