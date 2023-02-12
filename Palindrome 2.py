palabra = input("Porfavor ingrese una palabra: ")
lista = list(palabra)
fin = len(lista) - 1
ini = 0                                                                                     
for i in lista:                               
    if (i == lista[fin]):                              
        ini +=1 
        fin -= 1
    else:
        print("No es palindrome")
        break
if (ini >= fin):
    print("Es palindrome")