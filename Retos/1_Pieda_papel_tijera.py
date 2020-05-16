from random import randint

def comparador(opcion,maquina):
    if opcion==1 and maquina ==3:
        return 1
    if opcion==2 and maquina ==1:
        return 1
    if opcion==3 and maquina ==2:
        return 1
    else:
        return 0

def eleccion(jugada):
    if jugada == 1:
        return "Piedra"
    if jugada == 2:
        return "Papel"
    if jugada ==3:
        return "Tijera"

print("Piedra, Papel, Tijera")


print("selecciona una opción:")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("0. Salir")


marcador_maquina = 0
marcador_persona = 0


opcion=int(input("selecciona una opción:"))

if opcion==0:
       print ("Gracias por jugar") 
       exit()


while (opcion !=0):
    
    maquina= randint(1,4)
    contador = 0
    comp=comparador(opcion,maquina)
    
    
    if opcion == maquina:
        marcador_maquina= marcador_maquina + 0
        
    else:
        if comp == 0:
            marcador_maquina= marcador_maquina + 1
        
        else:
            marcador_persona= marcador_persona + 1
    

    contador=contador + 1
    if contador == 3 or marcador_maquina ==3 or marcador_persona==3:
        if marcador_maquina>marcador_persona:
            print("El ganador es: Maquina")
            print("Marcador: " + str(marcador_maquina))
        if marcador_maquina==marcador_persona:
            print("Empate")
            print("Marcador: " + str(marcador_maquina) + str(marcador_persona))
        if marcador_maquina<marcador_persona:
            print("El ganador es: Persona")
            print("Marcador: " + str(marcador_persona))
    
        print("Marcador: " "Persona "+ str(marcador_persona) + "Maquina" + str(marcador_maquina))        
        exit()    
    else:
        print("Marcador: " "Persona "+ str(marcador_persona) + "Maquina" + str(marcador_maquina))    
        opcion=int(input("selecciona una opción:"))
