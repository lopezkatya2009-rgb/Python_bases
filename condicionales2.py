print("Escribe tu nombre:")
nombre = input()
print("Escribe tu edad")
edad = int(input())

#elif
#Operadores lógicos
#and (y) / or (o)
#and: Todas las expresiones sean True
#or: Con que una de las expresiones sea True
#> <    >=    <=

#if nombre == "Katya" and edad > 20:
    #print("Saludos Katya, eres una adulta")
#elif nombre == "Katya" and edad <= 20:
    #print("Saludos Katya, eres una joven")
#else: 
    #print()    

if nombre == "Katya" or nombre == "María":
    print("Me gusta tu nombre")

else:
    print("Que nombre tan extraño") 
