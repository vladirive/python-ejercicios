lista = input("Ingrese una cadena: ")
lista = list(lista)
lista_2 =  []
for i in reversed(lista):
       lista_2.append(i)
if( lista == lista_2):
  print("La cadena es Palindrome")
else:
  print("La cadena no es palindrome")
