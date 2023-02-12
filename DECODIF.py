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

#########################################################
import os
os.system ("cls")
print("\n")
print(" -----------------------")
print("|   DECODIFICADOR       |")
print(" -----------------------")
msg = input(" Ingrese el mensaje codificado: " ) 
num =  "srorooc*a,rsmo*csodbl*ioreao*smilsc*tostoa*asmemb"

cadena = str(msg)
lista = []

#ignoramos los espacios
for i in cadena:
    if (i != " "):
     lista.append(i)

#llamamos a la funcion para determinar el rango de la matriz
rango = indice_matriz(lista)

#muestro la lista    
print("\n")
print(lista)

# crea y muestra la matriz en forma de arreglo
matriz_codificada = crear_matriz(rango, lista)

'''print("\n")
print("Matriz normal")
visor_matriz(rango,matriz_codificada)'''

matriz_vacia = crear_matriz_2()

'''
print("\n")
visor_matriz(rango,matriz_vacia)
'''

fila =  rango - 2
colu = 0

for i in range(rango - 1):
    fila = rango - 2
    for j in range(rango - 1):
        matriz_vacia[fila][colu] = matriz_codificada[i][j]
        fila = fila - 1
    colu = colu + 1

print("\n")
print("Matriz codifica rotada -90° \"decodificacion\" ")

# Muestro la matri 2 rotada 90°
visor_matriz(rango,matriz_vacia)

#vista en forma de arregl o lista
print("\n")
print(matriz_vacia)

print("\n")
#Formacion de cadena decodificada

union= ""
for i in range(rango - 1):
    for j in range(rango - 1):
        fragmento = matriz_vacia[i][j]
        union= union + fragmento 
print("\n")
print(" ¡Mensaje deodificado con exito¡ => ",union)
print("\n")
