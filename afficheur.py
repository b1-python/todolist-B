"""
module afficheur
"""
class Afficheur:
    def __init__(self, liste):
        self.todoListe = liste


    def afficherListe(self):
        """ Afficher toutes les taches de la liste avec les index :

        1/ [X] Faire du python
        2/ [ ] Termienr le TP
        3/ [ ] Commencer l'héritage

        """
        toutesLesTaches = self.todoListe.getToutesLesTaches()
        for index in range(len(toutesLesTaches)):
            print(str(index+1)+"/ "+toutesLesTaches[index].afficher())

        ## Autre façon de faire la même chose :
        #index = 1
        #for tache in self.todoListe.getToutesLesTaches():
        #    print(str(index)+"/ " + tache.afficher())
        #    index += 1

    def demanderChoix(self):
        """ Affiche un menu et demande à l'utilisateur de choisir une action, en gérant les cas d'entrée incorrecte, et renvoie le choix effectuer """
        print("""
        1) Ajouter une tâche
        2) Terminer une tâche
        3) Afficher toutes les tâches
        4) Afficher les tâches à faire
        5) Afficher les tâches faites
        """)
        choix = 0
        # Boucle tant que le choix est invalide
        while not (1 <= choix <= 5):
            try:
                choix = int(input("> Entrez votre choix:"))
            except ValueError:
                print("Choix incorrect ")
                choix = 0

        return choix

    def traiterChoix(self, choix):
        """ Exécuter l'action relative au choix """
        if choix == 1:
            # Ajouter une tache
            descriptionTache = input("Quelle tache ajouter ? ")
            self.todoListe.ajouter(descriptionTache)

        elif choix == 2:
            # Terminer une tache
            # Boucler tant que l'index est invalide.
            # On utilise le fait qu'en cas d'index incorrect, on aura une IndexError
            invalide = True
            while invalide:
                try:
                    indexTache = int(input("Quelle tâche à supprimer ?"))  # Peut déclencher un ValueError
                    tache = self.todoListe.getTache(indexTache - 1)  # Peut déclencher un IndexError
                    # Si on arrive ici, l'index est valide
                    tache.terminer()
                    invalide = False
                except ValueError:
                    print("L'entrée est incorrecte ")
                    indexTache = 0
                except IndexError:
                    print("L'index n'existe pas")

        elif choix == 3:
            # Afficher toutes les taches
            for tache in self.todoListe.getToutesLesTaches():
                print(tache.afficher())

        elif choix == 4:
            # Afficher les taches à faire
            for tache in self.todoListe.getTachesAFaire():
                print(tache.afficher())




        elif choix == 5:
            # Afficher les taches faites
            for tache in self.todoListe.getTachesFaites():
                print(tache.afficher())