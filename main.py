"""
Ce fichier contient tout le code "en vrac".
Il doit être organisé dans des modules :
  - taches.py => classes Tache et TODOList
  - afficheurtaches.py => classe Afficheur
  - main.py => le code main du projet
"""
import taches                    # import du module complet
from afficheur import Afficheur  # import d'une partie du module seulement, dans le scope global


# Création de la TODOList principale
todoList = taches.TODOList() # on utilise taches.TODOList car on a importé tout le module "taches", TODOList n'est donc pas dans le scoe global
# Création de l'afficheur console
afficheur = Afficheur(todoList) # on peut utiliser directement Afficheur car on a importé Afficheur dans le scope global

# Boucle principale
while True:
    print("----------")
    afficheur.afficherListe()
    choix = afficheur.demanderChoix()
    afficheur.traiterChoix(choix)


