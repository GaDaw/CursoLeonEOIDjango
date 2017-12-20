#arumentos posicionales obligatorios

def hi(name):
    print ('hi', name)

#valores de argumento por defecto
def f(n='uno'):
    print(n)
f()

def f2(one,two,three= 3):
    print('one:' , one, 'two:', two, ',three:', three)
f2(45,10)

#usar argumentos como keywords

f2(two=90, one=25, three=45)


#varios argumentos (convierte argumentos en tupla)
def dime_cosas(*args):
    print(args)
dime_cosas(20,30,90, True, 'Hola')


#args no son obligatorios
def f3(name, *args):
    print ('hola', name)
    print(args)
f3('pepe')

#keywords, trabajar con diccionarios como argumentos
def f4 (**kwars):
    print(kwars)
o= {'c':'uno', 'b':'tres', 'a': 'manolo','f': True}
#f4(c='uno', b='tres', a = 'manolo',f= True)
f4(**o)







