def validar(a):#Define la función 'validar' que recibe el parámetro 'a'.
    #Define the function 'validar' that receives the parameter 'a'.
    c = 0#Inicializa la variable entera 'c' con 0.
    #Initialize the integer variable 'c' to 0.
    d = 0.0#Inicializa la variable decimal 'd' con 0.0.
    #Initialize the float variable 'd' to 0.0.
    try:#Intenta ejecutar el bloque que sigue (intentar conversión a entero).
        #Try to execute the following block (attempt conversion to int).
        c = int(a)#Convierte 'a' a entero y lo asigna a 'c'.
        #Convert 'a' to an integer and assign it to 'c'.
        print('Es un valor numerico sin decimales')#Muestra mensaje indicando que es un número sin decimales.
        #Print message indicating it is a number without decimals.
    except ValueError:#Si ocurre un ValueError (no se puede convertir a int), entra aquí.
        #If a ValueError occurs (cannot convert to int), enter here.
        print('No es un valor numerico sin decimales')#Muestra mensaje indicando que no es un número entero.
        #Print message indicating it is not an integer number.

    try:#Intenta ejecutar el bloque que sigue (intentar conversión a float).
        #Try to execute the following block (attempt conversion to float).
        d = float(a)#Convierte 'a' a float y lo asigna a 'd'.
        #Convert 'a' to a float and assign it to 'd'.
        print('Es un valor numerico con decimales')#Muestra mensaje indicando que es un número con decimales.
        #Print message indicating it is a number with decimals.
    except ValueError:#Si ocurre un ValueError (no se puede convertir a float), entra aquí.
        #If a ValueError occurs (cannot convert to float), enter here.
        print('No es un valor numerico con decimales')#Muestra mensaje indicando que no es un número con decimales.
        #Print message indicating it is not a number with decimals.

def listas(d):#Define la función 'listas' que intenta reconocer el tipo de dato y devolverlo en su tipo.
    #Define the function 'listas' that tries to recognize the data type and return it in its type.
    en = 0#Inicializa la variable entera 'en' con 0.
    #Initialize the integer variable 'en' to 0.
    dec = 0.0#Inicializa la variable decimal 'dec' con 0.0.
    #Initialize the float variable 'dec' to 0.0.

    try:#Intenta convertir 'd' a entero.
        #Try to convert 'd' to an integer.
        en = int(d)#Asigna el entero convertido a 'en'.
    #Assign the converted integer to 'en'.
        return en#Devuelve el entero si la conversión fue exitosa.
        #Return the integer if conversion succeeded.
    except ValueError:#Si falla la conversión a entero, se captura aquí.
        #If integer conversion fails, it is caught here.
        print('No es un entero')#Informa que no es un entero.
        #Inform that it is not an integer.

    try:#Intenta convertir 'd' a float.
        #Try to convert 'd' to a float.
        dec = float(d)#Asigna el float convertido a 'dec'.
        #Assign the converted float to 'dec'.
        return dec#Devuelve el float si la conversión fue exitosa.
        #Return the float if conversion succeeded.
    except ValueError:#Si falla la conversión a float, se captura aquí.
#If float conversion fails, it is caught here.
        print('No es un numero con decimales')#Informa que no es un número con decimales.
        #Inform that it is not a number with decimals.

    return d#Si no es ni entero ni float, devuelve el valor original (como string).
    #If it's neither int nor float, return the original value (as string).

def leer():#Define la función 'leer' que solicita un dato al usuario y lo procesa.
    #Define the function 'leer' that requests data from the user and processes it.
    d = input('Escribe un dato: ')#Lee una entrada del usuario y la guarda en 'd'.
    #Read user input and store it in 'd'.
    dato = listas(d)
    #Llama a 'listas' para convertir 'd' a su tipo si es posible; guarda el resultado en 'dato'.
    #Call 'listas' to convert 'd' to its type if possible; store the result in 'dato'.
    lista.append(dato)
    #Añade el dato (convertido o no) a la lista global 'lista'.
    #Append the data (converted or not) to the global list 'lista'.

#Inicializa la lista vacía global donde se almacenarán los datos.
#Initialize the empty global list where data will be stored.
lista = []

if __name__ == '__main__':#Comprueba si el script está siendo ejecutado directamente (no importado).
    #Check if the script is being run directly (not imported).
    while True:#Bucle infinito que permite leer repetidamente datos del usuario.
        #Infinite loop that allows repeatedly reading user data.
        leer()#Llama a la función 'leer' para solicitar y almacenar un dato.
        #Call the 'leer' function to request and store one datum.

        res = input('Deseas otro dato (S/N): ')#Pregunta al usuario si desea ingresar otro dato y guarda la respuesta en 'res'.
        #Ask the user if they want to enter another datum and save the response in 'res'.
        if res == 'n' or res == 'N':#Si la respuesta es 'n' o 'N', termina el bucle.
            #If the response is 'n' or 'N', break the loop.
            print(lista)#Imprime la lista con todos los datos almacenados.
            #Print the list with all stored data.
            break#Rompe el bucle 'while' terminando la ejecución principal.
            #Break the 'while' loop ending main execution.