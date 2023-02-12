def PRODUCTOS():
    productos= {
     "hogar": [
        {
            "id": 1,
            "name": "Cama",
            "price": 600 	
        },
        {
            "id": 2,
            "name": "Mueble",
            "price": 1430
        },
        {
            "id": 3,
            "name": "Nevera",
            "price": 800
        },
        {
            "id": 4,
            "name": "Microondas",
            "price": 70
        }
     ],
     "ropa": [
        {
            "id": 5,
            "name": "Pantalón",
            "price": 25 	
        },
        {
            "id": 6,
            "name": "Camiseta",
            "price": 12
        },
        {
            "id": 7,
            "name": "Suéter",
            "price": 25
        },
        {
            "id": 8,
            "name": "Zapatos",
            "price": 5
        }
    ],
    "Gaming": [
        {
            "id": 9,
            "name": "Xbox One X",
            "price": 700	
        },
        {
            "id": 10,
            "name": "Nintendo Switch OLED",
            "price": 400
        },
        {
            "id": 11,
            "name": "Playstation 5",
            "price": 800
        },
        {
            "id": 12,
            "name": "Nintendo 3DS",
            "price": 150
        },
        {
            "id": 13,
            "name": "Juego Nintendo Switch",
            "price": 60
        },
        {
            "id": 14,
            "name": "Laptop Gamer",
            "price":  2500
        }
    ],   
    }
    return productos

def LISTADO_PRODUCTOS():
    productos = PRODUCTOS()
    print(" -----------------------")
    print("| LISTADO DE PRODUCTOS |")
    print(" -----------------------")
    for key, value in productos.items():
     for element in value: 
      print("id:",element["id"], "|producto:", element["name"], "| precio =", element["price"])

def detalle_producto(productos,id_producto):
    for key, value in productos.items():
     for element in value: 
      if(element["id"] == int(id_producto)):
        renglon = key
        elemento = element["name"] 
        precio = element["price"]
    return renglon,elemento,precio

def detalle_cliente(cliente,cedula_cliente): 
    for i, v in enumerate(cliente):
        if (cliente[i][0] == cedula_cliente):
            print("Cliente nro:",i + 1,"Cedula:",cliente[i][0], "Nombre:",cliente[i][1])
    
def registrar_cobrar():
    os.system ("cls")
    print("-------------------")
    print("Registro de Cliente")
    print("-------------------")
    num = input(" Ingrese cedula:" )
    nombre = input(" Ingrese nombre:")
    apellido = input(" Ingrese apellido:" )
    cliente.append([num,nombre,apellido])
    print("\n")
    print("A continuacion seleccione el producto por el \"ID\" ")
    LISTADO_PRODUCTOS()
    print("\n")
    id_producto = input("PoR favor ingrese el ID del producto: " )
    pedidos.append([num,id_producto])
    productos = PRODUCTOS()
    renglon,elemento,precio = detalle_producto(productos, id_producto)
    print("\n")
    print("--------------------------------------")
    print("FACTURA")
    print(" |Datos del Cliente|")
    print("  Cedula:",num, "Nombre:",nombre, "Apellido:",apellido)
    print(" |Producto|")
    print("  -Nro del Producto (ID): ",id_producto)
    print("   Renglon:",renglon, "Nombre:",elemento,"Precio:",precio)
    print("-------------------------------------")
    menu(cliente,pedidos)

def pedido(cliente,pedidos):
    os.system ("cls")
    print("-----------")
    print("Ver Pedido:")
    print("-----------")
    id_producto = input(" Por favor ingrese el ID del producto: " )
    productos = PRODUCTOS()
    renglon,elemento,precio = detalle_producto(productos, id_producto)
    print("Producto: ",elemento," - ","Renglon: ",renglon )
    print("--------------------")
    print("Clientes con Pedido:")
    print("--------------------")
    c = 0
    for i, v in enumerate(pedidos):
        if (pedidos[i][1] == id_producto):
            c = c + 1
            cedula_cliente = pedidos[i][0]
            detalle_cliente(cliente,cedula_cliente)
    if(len(cliente) == 0 or c == 0):
        print(" !No hay Clientes con Pedido del Producto!")
    menu(cliente,pedidos)

def menu(cliente,pedidos):
    print("\n")
    print("--------------------")
    print("""
    MENU
    1. Registrar y cobrar el pedido
    2. Ver pedidos
    3. Salir del programa
    """)
    option = input("Ingrese una opcion: ")
    option = int(option)
    if option  == 1:
     	registrar_cobrar()
    elif option  == 2:
     pedido(cliente,pedidos)
    elif option == 3:
        print(" Hasta luego")
    else:
        print("error")

import os
os.system ("cls")
os.system ("color 70")
cliente = []
pedidos = []
menu(cliente,pedidos)    
