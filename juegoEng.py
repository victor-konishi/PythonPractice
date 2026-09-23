import random


def calc_damage (attack: int, defense: int) -> return.int:
    damage = attack - defense
    if damage < 0:
        damage = 0
    return damage 


player = {"name": "Arturo", "life": 100, "attack": 100, "defense": 5, "max_life": 200, "potions": 5}

enemies = [
    {"name": "Orco", "life": 200, "attack": 15, "defense": 2},
    {"name": "Goblin", "life": 50, "attack": 10, "defense": 0},
    {"name": "Dragon", "life": 300, "attack": 35, "defense": 15}
]
for enemy in enemies:
    if player["life"] <= 0:
        break
    else:
        print("/////////New Level//////////")
    while player["life"] > 0 and enemy["life"] > 0:
        critic = random.randint(1, 5)
        print(f"Current life of {player['name']}: {player['life']}")
        print(f"Current life of {enemy['name']}: {enemy['life']}")
        option = input(' --- Choose an option: (atack / potion) ').lower()
        if option == "break":
            break
        elif option == "atacar" or option == "a":
            enemy_damage = calc_damage(player["attack"], enemy["defense"])
            if critic == 5:
                enemy_damage = enemy_damage*2
                print("*The attack was critical!*")
            
            enemy["life"] -= enemy_damage 
            print(f"The damage dealt to the enemy was: {enemy_damage}")
            print(f"critic: {critic}")
        elif option == "potion" or option == "p":
            if player["potions"] > 0:
                player["potions"] -= 1
                print(f"Avaliable potions: {player['potions']}")
                player["life"] += 40
                if player["life"] > player["max_life"]:
                    player["life"] = player["max_life"]
                    print(f"The player {player['name']} has exceeded the maximum value of life, life was set to: {player['life']}")
                else: print("The player healed: 40")
            else:
                print(f"The player: '{player['name']}' has run out of potions")
        else:
            print("--Invalid option; please enter an available option.--")
            continue

        if enemy["life"] > 0:
            player_damage = calc_damage(enemy["attack"], player["defense"])
            player["life"] -= player_damage
            print(f"The damage dealt to player was: {player_damage}")

    if enemy["life"] <= 0:
        print(f"You have defeated the enemy: {enemy['name']} ")
    elif player["life"] <= 0:
        print(f"You lost :( You was defeated by: {enemy['name']}")

if player["life"] > 0:
    print(f"*******Congratulations {player['name']}, you have defeated ALL the enemies!*******")

    