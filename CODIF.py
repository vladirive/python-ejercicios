############### FUNCIONES ################
def indice_matriz(lista):
    size_matriz = 1
    c = 1 
    while size_matriz < len(lista):
        size_matriz = c * c
        c = c + 1
    return c 

def crear_matriz(rango,lista):
    cont = 0
    matriz =[]
    for i in range(rango - 1):
        matriz.append([])                          
        for j in range(rango - 1):
         matriz[i].append(lista[cont])
         cont =  cont + 1
    return matriz

def crear_matriz_2():
    #crea matriz 2 con datos vacios 
    matriz_2 =[]
    for i in range(rango - 1):
      matriz_2.append([])
      for j in range(rango - 1):
        matriz_2[i].append("")
    return matriz_2

def visor_matriz(rango,matriz):
    # Vista de MAtriz
    for r in range(rango - 1):
        print(matriz[r])


###########################################

###Inicio del Programa ####################

import os
os.system ("cls")
print("\n")
print(" -----------------------")
print("|   CODIFICADOR        |")
print(" -----------------------")
msg = input(" Ingrese el mensaje a ser codificado: " ) 
cadena = str(msg)
print("\n")
lista = []

#ignoramos los espacios
for i in cadena:
    if (i != " "):
     lista.append(i)   

#llamamos a la funcion para determinar el rango de la matriz
#rango = indice_matriz(lista)

largo = len(lista)

rango = indice_matriz(lista)


#completamos con * hasta llegar al total de espacios de la matriz
total_matriz = (rango - 1)**2
resto_matriz = total_matriz - largo
c = 0
while c < resto_matriz: 
    lista.append("*")
    c = c + 1

#muestro la lista    
print(lista)
'''print(len(lista))'''

# crea y muestra la matriz en forma de arreglo
matriz = crear_matriz(rango, lista)


print(matriz)


print("\n")
print("Matriz normal")
visor_matriz(rango,matriz)


#crear matriz_2
matriz_2 = crear_matriz_2()

#lleno la matriz 2 con los datos de la 1era rotados 90°
indice  = rango - 1
contador = 0
for i in range(rango - 1):
    indice =  indice - 1
    contador = 0
    for j in range(rango - 1):
        matriz_2[contador][indice] = matriz[i][j]
        contador = contador + 1

print("\n")
print("Matriz normal rotada 90° \"codificacion\" ")
# Muestro la matri 2 rotada 90°
visor_matriz(rango,matriz_2)

#vista en forma de arregl o lista
print("\n")
print(matriz_2)


print("\n")
#Formacion de cadena codificada
union= ""
for i in range(rango - 1):
    for j in range(rango - 1):
        fragmento = matriz_2[i][j]
        union= union + fragmento 
print("¡Mensaje condificado con exito¡")        
print("=> ",union)
