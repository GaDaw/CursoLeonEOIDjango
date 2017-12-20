ALUMNO = {
        'nombre': 'David',
        'edad': 26,
        'clase': 'python'
        }

print(ALUMNO['nombre'])
print(ALUMNO['edad'])
print(ALUMNO['clase'])

print(ALUMNO)

ALUMNO['edad'] = 30
print(ALUMNO)

ALUMNO['sexo'] = 'masculino'
print(ALUMNO)

del ALUMNO['sexo']
print(ALUMNO)

#Borra contenido pero no objeto
ALUMNO.clear()
print(ALUMNO)


del ALUMNO
print(ALUMNO)

