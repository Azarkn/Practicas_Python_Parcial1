#hacer un progrma que lea 10 numeros y los almacene en un arreglo

a =[0,0,0,0,0,0,0,0,0,0]#variable llamada "a" que almacena 10 elementos/variable called "a" that stores 10 elements

for i in range(0,10):# ciclo for que tiene un rango del 0 al 9/for loop that has a range from 0 to 9
    a[i]= int(input(f'Ingresa un numero \n'))
    #ingresa un numero con "input()"
    #"int()" convierte el texto que ingresa en entero
    #"a[]" guarda el dato en cada posicion del arreglo
    #enter a number with "input()"
#"int()" converts the text you enter to an integer
#"a[]" stores the data in each position of the array

for i in a:#recorre todos los elementos de la lista a /traverses all elements of list a
    print (i)#imprime cada numero en pantalla/prints each number on the screen
