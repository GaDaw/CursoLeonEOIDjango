PREGUNTA = '¿Cómo te llamas?'
RESPUESTA = input(PREGUNTA)
print ("Hola, ", RESPUESTA , "¿Cómo estás")

resuesta_formateada = 'Hola {}, ¿Cómo estás?'.format(RESPUESTA)
print (resuesta_formateada)