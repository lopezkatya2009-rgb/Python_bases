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

def mostrar_menu(): 
    print("")
    print("===========================")
    print("Selecciona la opcion que deseas:")
    print("1: Conocer cuántos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Salir del programa")

def mostrar_inventario():    
    print("Actualmente contamos con:")
    print("Perros:", num_perros, "Gatos:", num_gatos, "Pajaros", num_pajaros)
    print("En total tenemos", animales_totales, "animales")  

def comprar_animal():

    carrito = []

    while True:
        print("¿Que animal deseas comprar? Solo puedes elegir 1 de cada especie")
        print("Escribe F para terminar la lista, o V para ver tu carrito")
        animal = input()
        if animal == "F": break

        if animal == "V":
          print(f"Tu carrito de compras contiene {carrito}")
            


        if animal not in carrito:
              carrito.append(animal)
        else:
            print("Ese animal ya se encunetra en tu carrito")      
        #print("Has comprado un", animal)

    print("El contenido de tu carrito es")
    for animal in carrito:
        print("    ", animal)
 
while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:    
       mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        print("Salir del programa")
        break