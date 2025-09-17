a = 1#Asigna el valor entero 1 a la variable 'a' (coeficiente cuadrático).
#Assign the integer 1 to variable 'a' (quadratic coefficient).
b = 2# Asigna el valor entero 2 a la variable 'b' (coeficiente lineal).
#Assign the integer 2 to variable 'b' (linear coefficient).
c = -15#Asigna el valor entero -15 a la variable 'c' (término independiente).
#Assign the integer -15 to variable 'c' (constant term).
p = 0#Inicializa la variable 'p' con 0; aquí se usará para b**2.
#Initialize variable 'p' to 0; here it will be used for b**2.
m = 0#Inicializa la variable 'm' con 0; aquí se usará para 4*a*c.
#Initialize variable 'm' to 0; here it will be used for 4*a*c.
r = 0#Inicializa la variable 'r' con 0; representará el discriminante (b^2 - 4ac).
#Initialize variable 'r' to 0; it will represent the discriminant (b^2 - 4ac).
ra = 0.0#Inicializa 'ra' como float; se usará para la raíz cuadrada del discriminante.
#Initialize 'ra' as float; it will be used for the square root of the discriminant.
d = 0.0#Inicializa 'd' como float; se usará para el denominador 2*a.
#Initialize 'd' as float; it will be used for the denominator 2*a.
x1 = 0.0#Inicializa 'x1' como float; contendrá la primera raíz.
#Initialize 'x1' as float; it will hold the first root.
x2 = 0.0#Inicializa 'x2' como float; contendrá la segunda raíz.
#Initialize 'x2' as float; it will hold the second root.
p = b**2#Calcula b al cuadrado y lo asigna a 'p'.
#Compute b squared and assign it to 'p'.
m = 4*a*c#Calcula 4*a*c y lo asigna a 'm'.
#Compute 4*a*c and assign it to 'm'.
r = p - m#Calcula el discriminante r = b^2 - 4ac.
#Compute the discriminant r = b^2 - 4ac.
if r > 0:#Si el discriminante es mayor que 0 hay dos raíces reales distintas.
#If the discriminant is greater than 0 there are two distinct real roots.
    print('Si se puede')#Imprime mensaje indicando que sí es posible calcular raíces reales.
#print a message indicating it's possible to compute real roots.
    ra = r ** (1/2)#Calcula la raíz cuadrada del discriminante y la guarda en 'ra'.
#Calculate the square root of the discriminant and store it in 'ra'.
    d = 2*a#Calcula el denominador 2*a y lo guarda en 'd'.
#Compute the denominator 2*a and store it in 'd'.
    x1 = (-b + ra) / d#Calcula la primera raíz usando la fórmula (-b + sqrt(r)) / (2a).
#Calculate the first root using the formula (-b + sqrt(r)) / (2a).
    x2 = (-b - ra) / d#Calcula la segunda raíz usando la fórmula (-b - sqrt(r)) / (2a).
#Calculate the second root using the formula (-b - sqrt(r)) / (2a).
    print(f'El valor de x1 es {x1:.2f} y de x2 es {x2:.2f}')
    #Imprime los valores de x1 y x2 formateados con 2 decimales.
#Print the values of x1 and x2 formatted with 2 decimal places.
else:#Si r no es mayor que 0 (es 0 o negativo) entra aquí.
#If r is not greater than 0 (it is 0 or negative) enter here.
    print('No se puede')#Imprime mensaje indicando que no es posible calcular dos raíces reales distintas.
    #Print a message indicating it's not possible to compute two distinct real roots.