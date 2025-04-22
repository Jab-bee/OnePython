inventario = 100
print("el inventario contiene {inventario} hamburguesas")

while inventario>0: 
    if inventario<10: 
        print("advertencia el Inventario esta casi vacio")
    num_hamburguesas = int(input("Cuantas hamburguesas quiere el cliente?"))
    if num_hamburguesas>inventario:
        print("No hay stock para tanta hamburguesa. Hay menos")
    else: 
        inventario -= num_hamburguesas
        print(f"El cliente ha pedido {num_hamburguesas} sin embargo tienes en el inventario {inventario}")
      
        
