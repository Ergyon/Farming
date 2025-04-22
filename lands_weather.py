# METEO ET DIFFERENTS CLIMATS
class Weather:

    def __init__(self, name, description, sun_exposure, water_rain):
        self.name = name
        self.description = description
        self.sun_exposure = sun_exposure
        self.water_rain = water_rain


WEATHERS = [
    Weather("Bon","Le temps est doux, il y a quelques averses.", 2, 1),
    Weather("Doux", "Le ciel est bleu et une légère brise souffle.", 1, 0),
    Weather("Beau", "Les rayons de soleil font leur apparition !", 3, 0),
    Weather("Canicule", "Il fait très chaud et sec.", 5, -1),
    Weather("Nuageux", "Les nuages gris couvrent le ciel.", 1, 1),
    Weather("Pluvieux", "Il commence à pleuvoir.", 0, 3),
    Weather("Moisson", "Il pleut intensément !", -1, 5)
]

# TERRAINS ET ACTIONS QUE LE JOUEUR PEUT Y FAIRE 
class Lands:
    def __init__(self, name, description, sun, water):
        self.name = name
        self.description = description
        self.vegetables = []
        self.buildings = []
        self.sun = 0
        self.water = 0

    def plant(self, vegetable):
        self.vegetables.append(vegetable)

    def construct(self, building):
        self.buildings.append(building)

# LES DIFFERENTS TERRAINS
LANDS = [
    Lands("Campagne", "Le climat est tempéré.", 1, 1),
    Lands("Marais", "Le climat est très humide." , 3, 1),
    Lands("Campagne méditerranéenne", "Le climat est chaud et agréable", 2, 2),
    Lands("Jungle", "Le climat est chaud et humide", 2, 3)]