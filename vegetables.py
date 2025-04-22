from lands_weather import LANDS, WEATHERS

# DEFINITION D'UN VEGETAL ET DE SES BESOINS
class Vegetable:

    def __init__(self, name, water_needed, sun_exposure_needed, growth_needed, land, price):
        self.name = name
        self.water = 0
        self.water_needed = water_needed
        self.sun_exposure = 0
        self.sun_exposure_needed = sun_exposure_needed
        self.current_growth = 0
        self.growth_needed = growth_needed
        self.land = land
        self.price = price

    def growth(self, weather):
        self.water += weather.water_rain + self.land.water
        self.sun_exposure += weather.sun_exposure + self.land.sun

        if self.water >= self.water_needed and self.sun_exposure >= self.sun_exposure_needed:
            self.water = 0 # Consomme l'eau
            self.sun_exposure = 0 # Consome l'énergie
            self.current_growth += 1 # Augmente la croissance
            print(f"{self.name} est en train de pousser. Croissance actuelle : {self.current_growth}/{self.growth_needed}")
        else:
            print(f"{self.name} manque encore de ressource pour pousser.")

    def is_harvestable(self):
        return self.current_growth >= self.growth_needed
    
    # TODO refactor into player class
    def harvest(self, player):
        if self.is_harvestable():
            quantity_to_harvest = self.current_growth # Combien de légumes sont récoltés
            self.current_growth = 0 # Remet la croissance à 0
            player.add_to_inventory(self, quantity_to_harvest)
            print(f"Vous récoltez {quantity_to_harvest} {self.name}(s).")
        else:
            print(f"{self.name} ne peut pas encore être récolté.")


# LES DIFFERENTS VEGETEAUX
VEGETABLES = [
    Vegetable("Blé", 1, 2, 2, LANDS[0], 2),
    Vegetable("Salade", 1, 1, 2, LANDS[0], 3),
    Vegetable("Tournesol", 4, 3, 4, LANDS[3], 6),
    Vegetable("Tomate", 2, 1, 2, LANDS[1], 3),
    Vegetable("Maïs", 2, 2, 2, LANDS[0], 3),
    Vegetable("Pomme", 2, 3, 2, LANDS[0], 4),
    Vegetable("Olive", 2, 3, 3, LANDS[2], 5),
    Vegetable("Kiwi", 3, 4, 5, LANDS[2], 7)
]