def resultados():
    c2 = 0  # Inicializa el contador c2 en 0. /Initialize the counter c2 to 0.
    print(f'La lista tiene {len(lis)}')  #Imprime la longitud de la lista 'lis'. 
    #/Print the length of the list 'lis'.
    for i in ar:  #Recorre cada elemento del arreglo 'ar'. 
        #/Iterate over each element of array 'ar'.
        if i !=-1:  # Comprueba si el elemento no es -1 (valor marcador).
            #/Check if the element is not -1 (marker value).
            c2 += 1  # Si no es -1, incrementa el contador c2.
            #/If it's not -1, increment counter c2.
    print(f'El arreglo tiene {c2}')  # Imprime cuántos elementos distintos de -1 hay en 'ar'.
    #/English: Print how many elements different from -1 are in 'ar'.
    print(ar)  #Imprime el contenido completo del arreglo 'ar'. /Print the full contents of the array 'ar'.
    print(lis)  # Imprime el contenido de la lista 'lis'. /Print the contents of the list 'lis'.

def hola(): # definicion de metodo o funcion
    #Define la función 'hola' que leerá hasta 10 entradas y las catalogará en 'ar' o 'lis'.
    #Define the 'hola' function that will read up to 10 inputs and categorize them into 'ar' or 'lis'.
    c = 0  #Inicializa el índice/contador 'c' en 0 para usar como posición en 'ar'. 
    #/Initialize index/counter 'c' to 0 to use as position in 'ar'.
    while(True):  #Bucle que leerá datos repetidamente hasta alcanzar 10 entradas. 
        #/Loop that will read data repeatedly until reaching 10 entries.
        a = input('Escribe un dato o valor ')  #Pide al usuario un dato y lo guarda en 'a' como cadena
        #/Ask the user for a datum and store it in 'a' as a string.
        if a.isdigit():  #Si la entrada contiene solo dígitos (número positivo sin signo).
            #/If the input contains only digits (positive number without sign).
            ar[c] = int(a)  # Convierte a entero y lo almacena en la posición c del arreglo 'ar'.
            #/Convert to int and store it at position c of array 'ar'.
        elif a.isalpha():  #Si la entrada contiene solo letras. /If the input contains only letters.
            lis.append(a)  #Añade la cadena a la lista 'lis'.  /Append the string to the list 'lis'.
        c += 1  #Incrementa el índice/contador para la siguiente posición del arreglo.  
        #/Increment the index/counter for the next array position.
        if c >=10: #Si se han leído 10 entradas, sale del bucle. /If 10 entries have been read, exit the loop.
            break  #Rompe el while. /Break the while loop.
    resultados()  #Llama a la función 'resultados' para mostrar salidas. 
    #/Call the 'resultados' function to display outputs.

ar  = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  #Arreglo con 10 posiciones inicializadas a -1 como marcador. 
#/Array with 10 positions initialized to -1 as marker.
lis = []  #Lista vacía donde se almacenarán entradas alfabéticas. 
#/Empty list where alphabetic entries will be stored.

if __name__ == "__main__":  # Comprueba si el archivo se ejecuta directamente. 
    #/Check if the file is executed directly.
    hola()  #Si la condición anterior se cumple, llama a 'hola()'.  
    #/If the above condition holds, call 'hola()'.