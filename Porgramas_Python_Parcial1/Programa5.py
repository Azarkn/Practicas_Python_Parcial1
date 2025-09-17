#Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un arreglo
# si es un caracter o caracteres se metera en una lista, cuando finalice el programa
# nos mostrara cuantos elementos numericos y cuantos caracteres hay en cada estructuras

car = 0   #Variable declared but unused 
#/Variable declarada pero no utilizada
Arreglo = 0  # Counter for total entered elements 
#/Contador para los elementos totales ingresados
n = 0     #Counter for total entered elements 
#/  Contador para los elementos ingresados
a = [0,0,0,0,0,0,0,0,0,0]  # Initialize list 'a' with one numeric element (10) 
#/  Inicializa la lista 'a' con un elemento numérico (10)
l = []    # Initialize empty list 'l' to store alphabetic characters 
#/ Inicializa la lista vacía 'l' para guardar caracteres alfabéticos

while (n < 10):  # Loop until 10 valid elements are entered 
    #/ Bucle hasta que se ingresen 10 elementos válidos
    b = input('Ingresa un dato: ')  #Request input from user / Solicita un dato al usuario

    if b.isdigit():  # Check if input is numeric /Verifica si el dato ingresado es numérico
        a[Arreglo]=(b)  #Add numeric input to list 'a' / Agrega el dato numérico a la lista 'a'
        Arreglo +=1  #Increase numeric counter / Incrementa el contador de numéricos
        n += 1       # Increment counter / Incrementa el contador
    elif b.isalpha():  #  Check if input is alphabetic 
        #/ Verifica si el dato ingresado es alfabético
        l.append(b)    #  Add alphabetic input to list 'l' 
        #/ Agrega el dato alfabético a la lista 'l'
        n += 1         #  Increment counter / Incrementa el contador
    else:
        print('No valido')  # Show error message for invalid input 
        #/ Muestra mensaje de error para datos no válidos

print(f'El total de elementos numericos guardados es {(Arreglo)}')  
#Show total numeric elements stored / Muestra el total de elementos numéricos guardados
print(f'El total de caracteres guardados es {len(l)}')  
# Show total alphabetic elements stored / Muestra el total de caracteres guardados
"""print(f'Elementos numericos guardados {a}')  
# Display list of numeric elements / Muestra la lista de elementos numéricos
print(f'Elementos de caracteres guardados {l}')  
# Display list of alphabetic elements / Muestra la lista de elementos alfabéticos"""