print("****************************")
print("**     BIENVENIDO  A      **")
print("** LA TIENDA DE MASCOTAS  **")
print("****************************")

num_perros = 23
num_gatos =10
num_pajaros = 14

animales_totales = num_perros + num_gatos + num_pajaros

print("Por favor ingresa tu nombre")
nombre = input()
print("Por favor escribe tu apellido")
apellido = input()

#Concatenación
nombre_completo = nombre + "  " + apellido

print("Gracias por visitarnos", nombre_completo)

while True:  
    print("")
    print("===========================")
    print("Selecciona la opcion que deseas:")
    print("1: Conocer cuántos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Salir del programa")

    respuesta = int(input())

    if respuesta == 1:    
        print("Actualmente contamos con:")
        print("Perros:", num_perros, "Gatos:", num_gatos, "Pajaros", num_pajaros)
        print("En total tenemos", animales_totales, "animales")  
    elif respuesta == 2:
        print("¿Que animal deseas comprar?")
        animal = input()
        print("Has comprado un", animal)
    elif respuesta == 3:
        print("Salir del programa")
        break