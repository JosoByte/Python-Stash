from random import randint

pila=[]

def añadirRandomPila(nombrePila):
    nombrePila.append(randint(0,10))
    nombrePila.append(randint(0,10))
    nombrePila.append(randint(0,10))

def añadirPila(objeto, nombrePila):
    nombrePila.append(objeto)
    
def sacarPila(nombrePila):
    return nombrePila.pop()

def sacarEnPila(nombrePila, pos):
    if pos <= len(pila) and pos >= 0:
        return nombrePila.pop(pos)
    
def printPila(nombrePila):
    print(pila)

        
