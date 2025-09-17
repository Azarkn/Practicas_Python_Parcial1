a=[10] #en la variable "a" se agrega con un solo elemento "[10]" 
#/ in the variable "a" is added with a single element "[10]"
a[0] = 10#este es un arreglo con posicion de 0 al 10 / This is an array with position from 0 to 10 
a[1] = 10#arreglo con posicion del 1 al 10 / array with position from 1 to 10


b = []#"lista recomendable" creas la lista / "recommended list" you create the list
b = {'hola', 10,10.05,False,{1,2,3,4}}#guardar los sets en python no permiten que los elementos se repitan 
#y no tienen un orden fijo 
#/Saving sets in Python does not allow elements to be repeated and does not have a fixed order.

if (len(a) > len(b)):#lee ambas listas en donde si "a" es mayor a "b" se imprime un mensaje
    #/read both lists where if "a" is greater than "b" a message is printed
    print('A es mayor')#si "a" es mayor se imprimira/If "a" is greater than it will be printed
else:#aqui sino es mayor entonces se imprime otro mensaje/Here if it is not greater then another message is printed
    print('B es mayor')#si "a" no era mayor entonces se imprime/if "a" was not greater then it is printed

    for i in a:#recorre cada elemento de la lista "a" y lo guarda en la variable "i"
        #/traverses each element of list "a" and stores it in variable "i"
        print (i)#imprime la lista guardada /print the saved list