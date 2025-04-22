
# TODO Animal

import random
import time
import os
from player import Player
from lands_weather import Lands, LANDS, Weather, WEATHERS
from vegetables import Vegetable, VEGETABLES

is_running = True
player = Player()

# BOUCLE TEMPORELLE DU JEU
while is_running:
    for day in range(100):
        if not is_running:
            break

        os.system('cls')
        print()
        print(f" ------- Jour {day} -------")
        print()
        # time.sleep(1)

        today_weather = random.choice(WEATHERS)
        print("Aujourd'hui,")
        # time.sleep(1) 
        print(f"{today_weather.description}")
        print()
        # time.sleep(1.5)

        for vegetable in VEGETABLES:
            vegetable.growth(today_weather)
            # time.sleep(0.5)
        print()

        # Affichage des actions possibles par le joueur 
        def show_actions():
            print()
            print(" ----- ACTIONS -----")
            print("1. Recolter les plantations mûres")
            print("2. Vendre un objet")
            print("3. Ouvrir l'inventaire")
            print("4. Se déplacer")
            print("5. Passer au jour suivant")
            print("6. Quitter la partie")
            print()
            # time.sleep(1)

            player_action = int(input("Que voulez-vous faire ? "))
            return player_action

        # GAMEPLAY DU JOUEUR, GESTION DE SES ACTIONS
        while True:
            action = show_actions()

            try: # Gestion d'erreur si l'entrée est invalide
                action = int(action)
                if action < 1 or action > 6:
                    print("Entrée invalide.")
                    continue
            except ValueError:
                print("Entrée invalide.")
                continue

            if action == 1:
                print()
                for vegetable in VEGETABLES: # Récolte les végétaux mûrs
                    if vegetable.is_harvestable():
                        vegetable.harvest(player)
                        player.add_to_inventory(vegetable)
                    else:
                        print(f"{vegetable.name} n'est pas encore assez mûre.")
                    
            elif action == 2: # Vendre un ou des objets
                player.show_inventory()
                print()
                player.sell_item()
                    
            elif action == 3: # Montrer l'inventaire
                player.show_inventory()
                return_to_actions = input("M pour retourner au menu ").lower()
                print()
                if return_to_actions == "m":
                    continue
                else:
                    print("Entrée invalide.")
                    continue
                                
            elif action == 4: # Se déplacer
                pass

            elif action == 5: # Passer au jour suivant
                break

            elif action == 6: # Quitter la partie
                print()
                print("Fin de partie...")
                # time.sleep(2)
                print("Merci d'avoir joué à Farming !")
                is_running = False
                break
                

            else:
                print("Entrée invalide.")
                continue
