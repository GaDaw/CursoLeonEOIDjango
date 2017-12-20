import re

phone = '666666666 # esto es un numero de telefono'

#quedarse solo con el nº de telefono (desde # hasta el final)
number = re.sub(r'#.*$', '', phone)
print(number)


#quedarse solo con numeros
number1 = re.sub(r'\D', '', phone)
print(number1)

