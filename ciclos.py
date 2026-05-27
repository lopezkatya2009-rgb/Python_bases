#Ciclo, interacion, bucle

#while
"""
i = 0
while i < 10:
    if i < 5:
        print("El numero ",  i, "es menor a 5")
    else:
        print("El numero",  i, "es mayor o igual a 5")
    i += 1 

print("Terminó la interación")
"""

#for x in "Katya":
    # print(x)

while True:
    print("Escribe la opcion deseada")
    print("1: Saludar")
    print("2: Salir")

    respuesta = int(input())

    if respuesta == 1:
        print("Saludos chicos!")
    elif respuesta == 2:
        break
  
print("Terminando programa")

