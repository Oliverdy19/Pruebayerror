num1 = 5
num2 = 5
print("""
    ----LISTA DE OPCIOES----
    1 - SUMAR
    2 - RESTAR
    3 - MULTIPLICAR
    4 - DIVIDIR
    5 - SALIR
    """)
def carculadora(num1, num2):
     opcion = 0
     while opcion != 5:
        opcion = int(input("Introce una opcion :> "))
        if opcion == 1:
            resultado = num1 + num2
            print(f"La suma de {num1} + {num2} = {resultado} ")
        elif opcion == 2:
            resultado = num1 - num2
            print(f"La suma de {num1} - {num2} = {resultado} ")
        elif opcion == 3:
            resultado = num1 * num2
            print(f"La suma de {num1} + {num2} = {resultado} ")
        elif opcion == 4:
            resultado = num1 / num2
            print(f"La suma de {num1} + {num2} = {resultado} ")
        elif opcion == 5:
            print("Gracias por usar nuestro programa") 
        else: print("Digite una opcion valida") 

carculadora(num1, num2)