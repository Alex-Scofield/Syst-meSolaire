import math
class Systeme:
    # Je change. C'est mieux d'avoir les objets dans la classe système. Comme ça on peut
    # Faire plusieurs systèmes au même temps.

    def __init__(self) -> None:
        self.objets = []

        # Constante G
        self.G = -6.61*10**(-11)

        # Variation de temps
        self.DELTA = 0.01

    def actualiser_forces(self):
        # Ce qu'on va faire ici est actualiser les forces ressenties pour chaque objet.
        for objet in self.objets:
            objet.f = [0,0,0]
            for objet2 in self.objets:
                if objet2 != objet:

                    # distance entre les objets
                    delta_x = objet2.pos[0] - objet.pos[0]
                    delta_y = objet2.pos[1] - objet.pos[1]
                    delta_z = objet2.pos[2] - objet.pos[2]
                    distance = math.sqrt((delta_x)**2+(delta_y)**2+(delta_z)**2)
                    
                    # Force ressentie en objet
                    module_f = -self.G*objet.m*objet2.m/((distance)**2)
                    
                    distance_unitaire = [(delta_x)/distance, (delta_y)/distance, (delta_z)/distance]
                    objet.f += [distance_unitaire[0]*module_f, distance_unitaire[1]*module_f, distance_unitaire[2]*module_f]
    

    def actualiser_vitesses(self):
        for objet in self.objets:
            objet.v += [f/objet.m * self.DELTA for f in objet.f]

    
    def actualiser_positions(self):
        for objet in self.objets:
            objet.pos += [v*self.DELTA for v in objet.v]
    
    def actualise(self):
        self.actualiser_forces()
        self.actualiser_vitesses()
        self.actualiser_positions()


# On définit une class pour les objets qui vont intervenir dans la simulation.
# C'est comme une espèce de variable pour tous les objets.
class ObjetCeleste:
    # C'est un méthode qui s'execute chaque fois qu'on initialise un ObjetCeleste
    def __init__(self, m:float, pos, v, systeme) -> None:
        '''@param m float, masse de l'objet en kg.
        @param pos liste (de floats), position en 3D
        @param v liste (de floats), vitesse en 3D
        @param systeme (systeme où se trouve)'''
        self.m = m
        self.pos = pos
        self.v = v
        self.systeme = systeme
        
        # Ici la force ressenti par l'objet.
        self.f = [0,0,0]
        
        #Si tu comprends cette ligne tu comprends l'OOP.
        #est ce que le append fait que ça se rajoute dans la liste objets ?
        # Oui, mais la liste d'objets de qui?
        #de systeme du coup mais ça me parait bizarre
        # Mais du systeme specifique associé à l'obet. Tu vois, on peut avoir plusieurs systemes au meme temps
        self.systeme.objets.append(self)
    
    

