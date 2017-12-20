LIST = [14,3,5 ,6, 'PEPE', True]
print(LIST)
print(LIST[0])
print(LIST[2:5])
print(LIST[4][1:3])

print(len(LIST))
del LIST[2]
print(LIST)

LIST[2] = 'tres'
print(LIST)


#Concatenar dos Listas

LIST += ["luis", 7, False]
print(LIST)


#añadir elemento lista al final

LIST.append('elemento nuevo')
print(LIST)

#eliminar por valor
LIST.remove('tres')
print(LIST)

LIST.reverse()
print(LIST)

#Insertar elemento en posicion 1
LIST.insert(1, 'PC')
print(LIST)



