def hi():
    print("Hola")
hi()

def hi_to(name):
    print('Hi', name)
hi_to('Gaspar')

def add_name(name_list, name):
    name_list.append(name)
    print(name_list)

l = ['Patricia', 'María']
add_name(l, 'Carlota')

def talk(word):
    word = 'cambio'
    print(word)
talk('hola')


