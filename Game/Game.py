import random
from random import Random
from faker import Faker
from rich import print



fake = Faker()

#création personnage:
# --utilisation de l'objet
# props:
# -Nom_personnage. == random si non choix
# -Prenom_personnage. == random si non choix
# -Couleur_Cheveux == affichage Couleur_Cheveux en couleur. == random si non choix
# -List_Equipements == doit être ranger en Desc. == random si non choix
# -Hp_personnage. == random si non choix

class Personnage:
    def __init__(self, Nom_personnage, Prenom_personnage, Hp_personnage, Couleur_Cheveux, List_Equipements):
        self.Nom_personnage = Nom_personnage
        self.Prenom_personnage = Prenom_personnage
        self.Hp_personnage = Hp_personnage
        self.Couleur_Cheveux = Couleur_Cheveux
        self.List_Equipements = List_Equipements

    def echoHero(self):
        print("ededzd")
        print(f"Présentation personnage {self.Nom_personnage} || {self.Prenom_personnage} || {self.Hp_personnage} || [{self.Couleur_Cheveux}]{self.Couleur_Cheveux}[/{self.Couleur_Cheveux}]  || {self.List_Equipements}")




