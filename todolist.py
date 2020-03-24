"""
Ce fichier contient tout le code "en vrac".
Il doit être organisé dans des modules :
  - taches.py => classes Tache et TODOList
  - afficheurtaches.py => classe Afficheur
  - main.py => le code main du projet
"""

class Tache:

    def __init__(self, f, c):
        self.fait = f
        self.contenu = c

    def terminer(self):
        """ Marque la tache comme terminée """
        self.fait = True

    def afficher(self):
        """ Afficher la tache :
        [ ] blablabalbl -> si elle n'est pas faite
        [X] blablabalbalb -> si elle est faite
        """
        if self.fait: return "[X] "+self.contenu
        else: return "[ ] "+self.contenu

    def estFaite(self):
        return self.fait



class TODOList:

    def __init__(self):
        self.taches = []

    def ajouter(self, contenu):
        tache = Tache(False,contenu)
        self.taches.append(tache)

    def supprimer(self, index):
        self.taches.pop(index)
        # Idem que :
        # self.taches = self.taches[:index]+self.taches[index+1:]

    def getTache(self, index):
        return self.taches[index]

    def getToutesLesTaches(self):
        return self.taches

    def getTachesAFaire(self):
        tachesAFaire = []
        for tache in self.taches:
            if not tache.estFaite(): tachesAFaire.append(tache)
        return tachesAFaire

    def getTachesFaites(self):
        tachesAFaire = []
        for tache in self.taches:
            if tache.estFaite(): tachesAFaire.append(tache)
        return tachesAFaire


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



todoList = TODOList()
afficheur = Afficheur(todoList)
while True:
    print("----------")
    afficheur.afficherListe()
    choix = afficheur.demanderChoix()
    afficheur.traiterChoix(choix)


