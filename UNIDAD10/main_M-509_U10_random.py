

#! REDONDEAR VALORES NUMERICOS

def p(*args):
    print()
    print(*args)

#! ROUNND
# 3.141592653589793
# pi = 3.141592653589793
# p(pi)

# p(round(pi))

# p(round(pi, 2))

# x = 314159
# p(round(x, -1))
# p(round(x, -2))
# p(round(x, -3))

#! FUNCIONES PISO - FLOOR, TECHO - CEIL

# import math

# x = 3.10
# p(math.ceil(x))
# p(math.floor(x))

#! NUMEROS ALEATORIOS

#! RANDINT
import random

# x = 3.10
# for i in range(10):
#     p(random.randint(1,100))

#! RANDRANGE

# for i in range(1,5):
#     p(random.randrange(0,100, i), i)

#! RANDOM

# for i in range(1,5):
#     p(random.random())

#! UNIFORM
# for i in range(1,5):
#     p(random.uniform(1, 100))

#! CHOICE

# lista = ['uvas', 'peras', 'naranjas', 'ciruela', 'piña', 'nispero', 'maki']
# for i in range(1,5):
#     p(random.choice(lista))

#! SHUFFLE

# lista = ['uvas', 'peras', 'naranjas', 'ciruela', 'piña', 'nispero', 'maki']
# for i in range(1,5):
#     random.shuffle(lista)
#     p(lista)


#! SAMPLE

# lista = ['uvas', 'peras', 'naranjas', 'ciruela', 'piña', 'nispero', 'maki']
# for i in range(1,5):
#     p(i,'--',random.sample(lista, i))