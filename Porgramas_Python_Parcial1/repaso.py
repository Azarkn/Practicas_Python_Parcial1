# Instrucciones de entrada y salida
# print() o print(f)
#print('Hola Mundo')
#print(f'Hola mundo numeros {10}')
# Entrada de datos
#input('Escribe un numero') # se introducen solo letras
# casting para convertir a valores especificos
#f = 0.0
#f = float(input('Escribe un numero con decimales'))
#a = 0
#a = int(input('Escribe un numero con decimales'))
#c = 120
#print(str(c))
#v = ""
#v = str(c)
#NOTA: solo las variables que no se introducen por teclado se obliga a inicializarlas

'''
Hacer un programa que lea nombre y precio de un producto, el programa calculara el costo y precio de venta
El costo involucra el 12% y IVA 16%
'''

# for i in range(1,5): #rango valor inicial hasta valor final sin incluirlo

while(True):  #Inicia un bucle infinito que repetirá el bloque hasta encontrar un break.
    #/Start an infinite loop that repeats the block until a break is found.
    n = input('Escribe el nombre de tu producto: ')  #Lee el nombre del producto como cadena y lo guarda en `n`.
    #/Read the product name as a string and store it in `n`.
    p = float(input('Escribe el precio del producto: '))  #Lee el precio (texto) y lo convierte a float, luego lo asigna a `p`. 
    #Read the price (text), convert it to float, then assign it to `p`.
    c = p * 1.12  #Calcula el costo aplicando un 12% (c = p * 1.12).  
    #Calculate the cost applying 12% (c = p * 1.12).
    pv = c * 1.16  #Calcula el precio de venta aplicando IVA del 16% sobre el costo (pv = c * 1.16).
    #Calculate the selling price applying 16% VAT on the cost (pv = c * 1.16).
    print(f'El costo es: {c:.2f}')  #imprime el costo con 2 decimales.
    #Print the cost with 2 decimal places.
    print(f'El precio de venta es: {pv:.2f}')  #Imprime el precio de venta con 2 decimales.
    #Print the selling price with 2 decimal places.

    res = input('Deseas otro numero (s/n) \n')  #Pregunta si desea procesar otro producto; guarda la respuesta en `res`.
    #Ask if the user wants to process another product; store the response in `res`.
    if res == 'n' or res == 'N':  #si la respuesta es 'n' o 'N', se sale del bucle.
        #If the response is 'n' or 'N', exit the loop.
        break  #Rompe el while y termina el programa. 
    #Break the while and end the program.


