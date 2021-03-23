
try:
    4 / 0
except TypeError:
    print('No se pueden sumar letras')
except NameError:
    print('A no existe')
except ZeroDivisionError:
    print('En serio??')
except Exception:
    print('Algo ha ido mal')