""" Ejemplos para trabajar con cadenas de texto"""

TEXTO = 'hola mundo'
print(TEXTO[0])
print(TEXTO[1])
print(TEXTO[2])
print(TEXTO[3])

print(TEXTO[5:8])
print(TEXTO[5:])
print(TEXTO[:4])

#CONCATENACIÓN
print (TEXTO + ' ' + TEXTO)

#Mayusculas, Capital
print(TEXTO.upper())
print(TEXTO.capitalize())
#Longitud
print (len(TEXTO))

#Delimitar por espacio o letra
print(TEXTO.split())
print(TEXTO.split('u'))

