def print_evertthing(*args):
    for n in args:
        print(n)
print_evertthing(1,2,3,4,5,'hola')



def print_all_with_position(*args):
    for count, thing in enumerate(args):
        print ('{}.{}'.format(count,thing))
    
print_all_with_position(1,2,3,4,5,'hola')

def count_until(n):
    counter = 0
    while counter<n:
        counter+=1
        print(counter)
count_until(50)

def show_keyword_arguments(**kwargs):
    for name, value in kwargs.items():
        print('{}: {}'.format(name,value))

show_keyword_arguments(uno=1, dos=2, tres=3)




