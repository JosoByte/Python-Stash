from random import randint

#set variables

tiradasPosibles=[]
tiradasJ1=[]
tiradasJ2=[]
nCarasDado=6
nRondas=10

for i in range(1, nCarasDado+1, 1):
    for j in range(1, nCarasDado+1, 1):
        if str(j)+"-"+str(i) not in tiradasPosibles:
            tiradasPosibles.append(str(i)+"-"+str(j))

tiradasNoSacadas=tiradasPosibles
#test lista
testLista=[[] for i in range(3)]
print(testLista)

#definitions

def tirarDados():
    dado1=randint(1,6)
    dado2=randint(1,6)
    return str(dado1)+"-"+str(dado2)

def empezarPartida():
    rondaActual=0
    while rondaActual!=nRondas:
        rondaActual+=1
        
        #turno jugador 1
        input("RONDA "+str(rondaActual)+", Turno del jugador 1, presiona enter para lanzar tus dados")
        resultado=tirarDados()
        tiradasJ1.append(resultado)
        if resultado in tiradasNoSacadas:
            tiradasNoSacadas.remove(resultado)
        print("Has sacado "+resultado)
        input("RONDA "+str(rondaActual)+", Turno del jugador 1, presiona enter para lanzar tu segunda ronda de dados")
        resultado=tirarDados()
        tiradasJ1.append(resultado)
        if resultado in tiradasNoSacadas:
            tiradasNoSacadas.remove(resultado)
        print("Has sacado "+resultado)

        #turno jugador 2
        input("RONDA "+str(rondaActual)+", Turno del jugador 2, presiona enter para lanzar tus dados")
        resultado=tirarDados()
        tiradasJ2.append(resultado)
        if resultado in tiradasNoSacadas:
            tiradasNoSacadas.remove(resultado)
        print("Has sacado "+resultado)
        input("RONDA "+str(rondaActual)+", Turno del jugador 2, presiona enter para lanzar tu segunda ronda de dados")
        resultado=tirarDados()
        tiradasJ2.append(resultado)
        if resultado in tiradasNoSacadas:
            tiradasNoSacadas.remove(resultado)
        print("Has sacado "+resultado)

        
        
