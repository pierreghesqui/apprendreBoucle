import numpy as np
import cv2
import os
import tkinter  
class Fenetre :
    def __init__(self,hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.image = np.zeros((hauteur,largeur))
        self.arrierePlan = []
        root = tkinter.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        self.ecranLargeur = width
        self.ecranHauteur = height
        
    def mettreArrierePlan(self, path):
        print(path)
        bg = cv2.imread(path)/255
        #print(bg[1,1313])
        #cv2.imshow('fenetre', bg )
        #cv2.waitKey()
        bg = cv2.resize(bg,(self.largeur,self.hauteur))
        self.arrierePlan =bg
        #print(np.shape(bg))
        self.image = np.copy(self.arrierePlan)
        
        
    def afficher(self):
        cv2.namedWindow('mon image', cv2.WINDOW_NORMAL)
        cv2.moveWindow('mon image', int(self.ecranLargeur/2),10)
        cv2.resizeWindow('mon image', int(self.ecranHauteur*0.75), int(self.ecranHauteur*0.75))
        cv2.imshow('mon image', self.image)
        cv2.waitKey(1)
        
    def close(self):
        cv2.destroyAllWindows()
