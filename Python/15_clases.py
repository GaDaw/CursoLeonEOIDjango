#CLASES Y POO

class Thing:
    pass
thing = Thing()

#constructor sin parametros o argumentos

class Fruit:
    def __init__(self):
        print('objeto fruta')



fruit = Fruit()

#Argumentos del constructor

class CustomFruit:
    #Variable estática para cada nueva clase creada a partir de esta
    COUNTER = 0
    def __init__(self, name,color):
        self.name = name
        self.color = color
        self.juices = 0
        CustomFruit.COUNTER +=1
    """Representar mediante string"""
    def __str__(self):
        return 'soy fruta, me llamo {} y mi color es {}.\nHay {} frutas en total'.format(self.name, self.color, CustomFruit.COUNTER)
    def make_juice(self, count):
        for n in range(count):
            print('Haciendo zumo de ', self.name )
            self.juices +=1

custom = CustomFruit('Pera','verde')
custom.make_juice(2)
custom2 = CustomFruit('Sandia','verde oscuro')
custom2.make_juice(4)


print(custom)
print(custom2)
print('Zumos hechos', custom.juices)
print('Zumos hechos', custom2.juices)

