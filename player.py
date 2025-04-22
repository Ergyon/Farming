
class Player:
    def __init__(self):
        self.inventory = {}
        self.money = 0

    # Ajouter un objet à l'inventaire
    def add_to_inventory(self, item, quantity = 1):
        if item.name in self.inventory:
            self.inventory[item.name]["quantity"] += quantity
        else:
            self.inventory[item.name] = {"quantity": quantity, "item": item}

    # Montrer l'inventaire
    def show_inventory(self):
        print()
        print(" ------- Inventaire ------- ")
        print()
        if not self.inventory:
            print("Votre inventaire est vide.")
        else:
            for index, (name, info) in enumerate(self.inventory.items()):
                print(f"{index}. {name} : {info['quantity']} || Prix unité : {info['item'].price}$ || Total : {info['quantity'] * info['item'].price}$")
        print()        
    
    # Ajouter de l'argent à la banque du joueur 
    def get_money(self, amount):
        self.money += amount
        print(f"Total de votre banque : {self.money}$.")

    # Vendre un ou des objets disponibles dans l'inventaire
    def sell_item(self):
        if not self.inventory: # Verifie si l'inventaire est vide
            print("Vous n'avez rien à vendre.")
            return

        try:
            choice = int(input("Que souhaitez-vous vendre ? : "))

            if choice < 0 or choice > len(self.inventory): # Verifie si le choix est valide
                print("Choix invalide.")
                return
            
            # Chercher l'objet et sa quantité
            item_name = list(self.inventory.keys())[choice]
            item = self.inventory[item_name]["item"]
            quantity_in_inventory = self.inventory[item_name]["quantity"]

            quantity_to_sell = int(input(f"Combien de {item_name} voulez-vous vendre ? "))

            if quantity_to_sell > quantity_in_inventory:
                print(f"Vous n'avez pas assez de {item_name}.")
                print()
                return
            elif quantity_to_sell <= 0:
                print("Vous devez choisir une quantité à vendre.")
                print()
                return
            
            # Gain d'argent du joueur
            total_price = quantity_to_sell * item.price 
            print(f"Vous vendez {quantity_to_sell} {item_name}s")
            print(f"Vous gagnez {total_price}$")
            self.get_money(total_price)

            # Met à jour l'inventaire
            new_quantity = quantity_in_inventory - quantity_to_sell 
            if new_quantity > 0:
                self.inventory[item_name]['quantity'] = new_quantity
            else:
                del self.inventory[item_name] # Supprime la ressource de l'inventaire si tout est vendu
                
        except ValueError:
            print("Entrée invalide.")

                    

        