'''print(len(str(12)))
   num = 12
'''
def narcisista(num):
  while not num.isnumeric(): 
    num = input("Debe ingresar un valor numerico; por favor ingrese un numero: " ) 
  cifra = str(num)
  exponente = len(cifra)
  suma = 0
  for x in cifra:
     suma = suma + int(x) ** exponente
  if( suma == int(num)):
       print("Numero Narcisista")
  else:
       print("Numero Normal")
  
def primo(num):                                       
    cont = 0
    for i in range(num):
       if( num % (i + 1) == 0 ):
        cont = cont + 1
    if (cont == 2):
      print("Es numero Primo")
    else:
      print("No es numero Primo")

def sumar_digitos(num):
    cadena = str(num)
    suma = 0
    for i in cadena:
       suma = suma + int(i)
    return suma

valor = "S"
while valor == "S" or valor == "s":
    num = input("Por favor ingrese un numero: " )
    narcisista(num)
    primo(sumar_digitos(num))
    valor = input("Desea ingresar otro numero (S/N): " )
    while valor != "s" and valor != "n":
        valor = input("Desea ingresar otro numero (S/N); solo se acepta s o n cono respuesta: " )
print("Hasta pronto")




