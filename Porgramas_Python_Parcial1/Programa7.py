# Hacer un programa que lea nombre, edad, y sexo de 5 personas, estos elementos tienen que estar dentro de una lista

def inicio():  #Define la función 'inicio' que controla el flujo principal. 
    #/Define the 'inicio' function that controls the main flow.
    c= 0  #Inicializa el contador 'c' en 0. /Initialize the counter 'c' to 0.
    while (True):  #Inicia un bucle infinito que repetirá la lectura hasta alcanzar 5 registros.  
        #/Start an infinite loop that will repeat the reading until 5 records are reached.
        nombre()  #Llama a la función 'nombre' para leer y validar un nombre.
        #/Call the 'nombre' function to read and validate a name.
        edad()  #Llama a la función 'edad' para leer y validar una edad. 
        #/ Call the 'edad' function to read and validate an age.
        sexo()  #Llama a la función 'sexo' para leer y validar el sexo (M/F). 
        #/ Call the 'sexo' function to read and validate sex (M/F).
        c+=1  #Incrementa el contador 'c' después de leer un registro completo.
        #/ Increment the counter 'c' after reading a complete record.
        if c >= 5:  # Comprueba si se han leído 5 o más registros.
            #/ Check if 5 or more records have been read.
            break  # Si el contador llega a 5, rompe el bucle y termina la función. 
        #/ If the counter reaches 5, break the loop and end the function.
    


def nombre():  #Define la función 'nombre' para pedir y validar un nombre. 
    #/Define the 'nombre' function to request and validate a name.
    while(True):  #Bucle que se repetirá hasta recibir un nombre válido. 
        #/Loop that repeats until a valid name is received.
        n=input('Escribe un nombre ')  #Pide al usuario que escriba un nombre y lo guarda en 'n'.
        #/Ask the user to write a name and store it in 'n'.
        if n.isalpha():  #Verifica que 'n' solo contenga letras (sin espacios ni dígitos).
            #/Verify that 'n' contains only letters (no spaces or digits).
            lis.append(n)  #Si es válido, añade el nombre a la lista 'lis'.
            #/If valid, append the name to the list 'lis'.
            break  #Sale del bucle una vez añadido el nombre. 
        #/Exit the loop once the name has been appended.
        else:
            print('Nombre no valido')  #Mensaje si el nombre no es válido. 
            #/Message shown if the name is not valid.


def edad():  #Define la función 'edad' para pedir y validar la edad. 
    #/ Define the 'edad' function to request and validate age.
    while(True):  #Bucle que se repetirá hasta recibir una edad válida. 
        #/ Loop that repeats until a valid age is received.
        e=input('Escribe una edad ')  # Pide al usuario que escriba una edad y la guarda en 'e'.
        #/Ask the user to write an age and store it in 'e'.
        if e.isdigit():  #Verifica que 'e' esté compuesta solo por dígitos.
            #/Verify that 'e' is composed only of digits.
            lis.append(e)  # Si es válido, añade la edad a la lista 'lis'. 
            #/ If valid, append the age to the list 'lis'.
            break  # Sale del bucle una vez añadida la edad. 
        #/Exit the loop once the age has been appended.
        else:
            print('Edad no valida')  # Mensaje si la edad no es válida. 
            #/Message shown if the age is not valid.
    
def sexo():  # Define la función 'sexo' para pedir y validar el sexo (M/F).
    #/Define the 'sexo' function to request and validate sex (M/F).
    while(True):  # Bucle que se repetirá hasta recibir un sexo válido. 
        #/Loop that repeats until a valid sex is received.
        s=input('Escribe un sexo (M/F) ')  #Pide al usuario que indique el sexo y lo guarda en 's'.
        #/Ask the user to indicate sex and store it in 's'.
        if s=='M' or s=='F':  #Verifica que la entrada sea exactamente 'M' o 'F'.
            #/Verify that the input is exactly 'M' or 'F'.
            lis.append(s)  # Si es válido, añade el sexo a la lista 'lis'.
            #/If valid, append the sex to the list 'lis'.
            break  #Sale del bucle una vez añadido el sexo.
        # /Exit the loop once the sex has been appended.
        else:
            print('Sexo no valido')  # Mensaje si la entrada no es 'M' ni 'F'.
            #/ Message shown if the input is not 'M' or 'F'.


def resultados():  #Define la función 'resultados' (en el código actual imprime desde la lista).
    #/Define the 'resultados' function (currently prints from the list).
    i = 0  #Inicializa el índice 'i' en 0.
    #/Initialize the index 'i' to 0.
    while(True):  #Bucle infinito que imprimirá elementos de 'lis' (tal como está, no incrementa 'i')
        #/ Infinite loop that will print elements of 'lis' (as written, it does not increment 'i').
        print(lis[i])  #Imprime el elemento de la lista en la posición 'i'. 
        #/Print the element of the list at position 'i'.


    


lis = []  #Inicializa la lista vacía 'lis' donde se almacenarán nombres, edades y sexos.
#/Initialize the empty list 'lis' where names, ages and sexes will be stored.
inicio()  #Llama a la función 'inicio' para comenzar el proceso de ingreso.
#/Call the 'inicio' function to start the input process.