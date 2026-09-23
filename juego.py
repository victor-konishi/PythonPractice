import random


def calcular_dano(ataque, defensa):
    dano = ataque - defensa
    if dano < 0:
        dano = 0
    return dano 


jugador = {"nombre": "Arturo", "vida": 100, "ataque": 100, "defensa": 5, "vida_maxima": 200, "pociones": 5}

enemigos = [
    {"nombre": "Orco", "vida": 200, "ataque": 15, "defensa": 2},
    {"nombre": "Goblin", "vida": 50, "ataque": 10, "defensa": 0},
    {"nombre": "Dragon", "vida": 300, "ataque": 35, "defensa": 15}
]
for enemigo in enemigos:
    if jugador["vida"] <= 0:
        break
    else:
        print("/////////Nuevo Nivel//////////")
    while jugador["vida"] > 0 and enemigo["vida"] > 0:
        critico = random.randint(1, 5)
        print(f"Vida actual de {jugador['nombre']}: {jugador['vida']}")
        print(f"Vida actual de {enemigo['nombre']}: {enemigo['vida']}")
        opcion = input(' --- Que opcion eliges: (Atacar / Usar pocion) ').lower()
        if opcion == "break":
            break
        elif opcion == "atacar" or opcion == "a":
            dano_a_enemigo = calcular_dano(jugador["ataque"], enemigo["defensa"])
            if critico == 5:
                dano_a_enemigo = dano_a_enemigo*2
                print("*El ataque fue critico!*")
            
            enemigo["vida"] -= dano_a_enemigo 
            print(f"El dano realizado al enemigo fue: {dano_a_enemigo}")
            print(f"critico: {critico}")
        elif opcion == "usar pocion" or opcion == "p":
            if jugador["pociones"] > 0:
                jugador["pociones"] -= 1
                print(f"Pociones disponibles: {jugador['pociones']}")
                jugador["vida"] += 40
                if jugador["vida"] > jugador["vida_maxima"]:
                    jugador["vida"] = jugador["vida_maxima"]
                    print(f"El jugador {jugador['nombre']} ha exedido el valor maximo de vida, se establecio la vida en: {jugador['vida']}")
                else: print("El jugador se curo: 20")
            else:
                print(f"El jugador: '{jugador['nombre']}' se quedo sin pociones")
        else:
            print("--Opcion no valida, por favor introduzca una opcion disponible--")
            continue

        if enemigo["vida"] > 0:
            dano_a_jugador = calcular_dano(enemigo["ataque"], jugador["defensa"])
            jugador["vida"] -= dano_a_jugador
            print(f"El dano realizado al jugador fue: {dano_a_jugador}")

    if enemigo["vida"] <= 0:
        print(f"Has derrotado el monstruo: {enemigo['nombre']} ")
    elif jugador["vida"] <= 0:
        print(f"Has perdido :( Has sido derrotado por: {enemigo['nombre']}")

if jugador["vida"] > 0:
    print(f"*******Felicidades {jugador['nombre']}, has derrotado a todos los enemigos!*******")

    