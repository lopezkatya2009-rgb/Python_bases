nombres = ["Katya", "Ana", "Lisseth", "Jeferson", "Mabel"]
print(nombres)
#f-strings
for i, nombre in enumerate(nombres):
    #print("se escribió", i, "en la lista:", i, nombre)
    print( f"se escribió {nombre} en la lista con el índice {i}")

print("Bienvenidos a la fiesta", nombres[:3])
print("Lo sentimos", nombres[3:])    
