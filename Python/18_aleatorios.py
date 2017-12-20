import random

for n in range(10):
    print('entero aleatorio:', random.randint(0,100))

#Random puro (0-1)

for n in range(10):
    print('aleatorio entre 0-1', random.random())

#Aleatorio array
L = ["Juan", "Luis", "María", "Juana", "Roberto"]

for n in range(10):
    print(random.choice(L))

#aleatorio de una lista(puede haber repetidos) k ->numero de elementos que queremos

for n in range(10):
    print(random.choices(L, k=2))

#cambiar orden elementos lista
print(L)
random.shuffle(L)
print(L)

#a partir de una lista, crear otra con k elementos de L que no esten repetidos

print(random.sample(L, k=2))

