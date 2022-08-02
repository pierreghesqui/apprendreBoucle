import numpy as np
import cv2
import os
import IPython.display as display
class Fenetre :
    def __init__(self,hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.image = np.zeros((hauteur,largeur))
        self.arrierePlan = []
        self.imageNb = 0
        self.ecranLargeur = 200
        self.ecranHauteur = 200
        d=display.display('test', display_id='essai')

    def mettreArrierePlan(self, path):
        bg = cv2.imread(path)/255
        bg = cv2.resize(bg,(self.largeur,self.hauteur))
        self.arrierePlan =bg
        
        self.image = np.copy(self.arrierePlan)
        
        
    def afficher(self):
        dir = os.path.join('fonctions', 'tentative','im'+'.png')
        cv2.imwrite(dir, self.image*255)
        self.imageNb=self.imageNb+1
        #afficher l'image avec Ipython.display
        dispImg = display.Image(dir,width = 400, height = 400)
        display.update_display(dispImg,display_id='essai')
        cv2.waitKey(1)
