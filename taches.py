"""
module tache
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
