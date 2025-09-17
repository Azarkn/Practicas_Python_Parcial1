def vocales(cad):
    ba = False
    ba =False
    bi = False
    bo = False
    bu = False
  
    if 'a' in cad or 'A' in cad:
        ba = True
    if 'e' in cad or 'E' in cad:
        be = True
    if 'i' in cad or 'I' in cad:
        bi = True
    if 'o' in cad or 'O' in cad:
        bo = True
    if 'u' in cad or 'U' in cad:
        bu = True
    if ba == True and be == True and bi == True:
        pass



def minusculas(c1):
   cm = 0
   print(c1)
   for i in c1[1:]:
      #con ese lee la cadena y hace que la primera letra sea o no mayuscula
        if ord(i) >=97 and ord(i)<122:
         cm += 1
        if cm == len(c1)-1:
         print(f'la cadena son minusculas excepto la primera{cm}')
         vocales (cm)
        else:
         print('error la cadena no cumple')


def leer():
    ce = 0
    nc = ""
    c = input('escribe una cadena')
    for i in c:
       if ord(i) == 32:
          ce += 1
    if ce == len(c):
#todo lo de arriba es para ver si tiene espacios y la longitud, la cuenta 
     if ce == len(c):
        if c.isalpha():
#revisa que sean minusculas
           pass
        else:
           for i in c:
            if ord(i)>=48 and ord(i)<=57:
#esos en ascii son los numeros 
              pass
           else:
              nc += i
              print(nc)
              minusculas(nc)
     else:
      print('error la cadena no cumple')






    lista = []
if __name__=='__main__':
  while(True):
    
    leer()
    if len(lista) >=5:
     break