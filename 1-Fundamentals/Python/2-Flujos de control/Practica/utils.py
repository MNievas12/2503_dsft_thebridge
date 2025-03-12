import random

def jugar(vidas_ini=2):
    print()
    print("Empezando nueva partida..")
    n_oculto = random.randint(1,5)
    vidas = vidas_ini
    while vidas > 0:
        n_usuario = int(input("Introduzca numero del 1 al 5"))
        if n_oculto == n_usuario:
            print("Has acertado, el número era", n_oculto)
            break
        else:
            print("Has fallado")
            vidas = vidas - 1
            print("Te quedan", vidas, "vidas")
    else:
        print("Fin del juego, el número era", n_oculto )

    mensaje = input("Jugar de nuevo? S/N")
    if mensaje == "S":
        jugar(vidas_ini)