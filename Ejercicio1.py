##Declarar varialbes
#nombre= input("¿Cual es tu nombre?")
edad= int(input("¿Cual es tu edad?"))
#print(f"Hola {nombre} San! tienes {edad} has vivido mucho. Te felicito")

#def robot(nombre):
#    print(f"Hola, {nombre}! Te esperabamos para iniciarte en las artes de la IA. Sabemos que has esperado {edad} años para esto. Pero no te precupes avanzaremos")
#robot(nombre)

#for miprimerbucle in range(0,10):
#    print(miprimerbucle)
    
    
#(casa)
#0 1 2 3

def esMayordeEdad(edad):
    if edad>=18:
        return "Eres Mayor de edad"
    else:
        return "Aun no eres mayor de edad"
print(esMayordeEdad(edad))