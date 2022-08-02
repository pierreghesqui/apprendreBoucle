import cv2
import os
import numpy as np
#import pygame.mixer
from fonctions.fenetre import Fenetre
import sys
import imageio

class Voiture :
    
    def __init__(self,niveau, ligne=0,colonne=0, hauteur = 100, largeur = 100):
        '''
        #Remove all images in tentative folder
        dir = os.path.join('fonctions', 'tentative')
        for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
        #===
        '''
        fenetre = Fenetre(1000,1000)
        '''
        f = open(os.path.join( 'fonctions', 'arrierePlans','config.txt'),'r')
        lines = f.readlines()
        f.close()
        niveau = lines[-1]
        '''
        self.niveau = niveau
        test = 'ap_niveau'+ niveau
        test= test+'.png'
        pathAP = os.path.join('fonctions', 'arrierePlans',test)
        fenetre.mettreArrierePlan(pathAP)
        voiture1 = cv2.resize(cv2.imread(\
            os.path.join('fonctions','voiture','voiture1.png'))/255,(largeur,hauteur))
        voiture2 = cv2.resize(cv2.imread(\
            os.path.join('fonctions','voiture','voiture2.png'))/255,(largeur,hauteur))
        voiture3 = cv2.resize(cv2.imread(\
            os.path.join('fonctions','voiture','voiture3.png'))/255,(largeur,hauteur))
        voiture4 = cv2.resize(cv2.imread(\
            os.path.join('fonctions','voiture','voiture4.png'))/255,(largeur,hauteur))
        listeVoiture = [voiture1, voiture2, voiture3, voiture4]
        #self.son =0
        self.surRoute = True
        self.listeImage = listeVoiture
        self.compteurImage = 1
        self.hauteur = hauteur
        self.largeur = largeur
        self.ligne = ligne
        self.colonne = colonne
        self.vitesse = 100  #doit être un diviseur de 100
        self.fenetre = fenetre
        self.position(ligne,colonne)
        
        cv2.putText(self.fenetre.image,"Niveau "+self.niveau, (325,920),\
                        cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 0, 255), 2, cv2.LINE_AA)
    def getCoord(self):
        coord = np.where( self.listeImage[self.compteurImage] != [0,0,0] )
        return coord
    
    def avancer(self):
        if self.compteurImage == 0:
            for i in range(0,self.hauteur//self.vitesse):
                self.bougerVersLeHaut()   
        elif self.compteurImage == 1:
            for i in range(0,self.hauteur//self.vitesse):
                self.bougerVersLaDroite()     
        elif self.compteurImage == 2:
            for i in range(0,self.hauteur//self.vitesse):
                self.bougerVersLeBas()     
        elif self.compteurImage==3:
            for i in range(0,self.hauteur//self.vitesse):
                self.bougerVersLaGauche()
        self.verifierSiOnEstSurRoute()    
    
    
            
        
    def tournerAGauche (self):
        self.effacer()
        self.compteurImage = (self.compteurImage-1)%4
        self.position(self.ligne,self.colonne)
        self.hauteur,self.largeur=self.largeur,self.hauteur
    def tournerADroite(self):
        self.effacer()
        self.compteurImage = (self.compteurImage+1)%4
        self.position(self.ligne,self.colonne)
        self.hauteur,self.largeur=self.largeur,self.hauteur

    def bougerVersLeHaut(self,vitesse=0):
        if vitesse ==0:
            vitesse =self.vitesse
        if self.ligne>0:
            self.effacer()
            self.ligne = self.ligne-vitesse
            self.position( self.ligne, self.colonne)
            
        else:
            self.effacer()
            #while not keyboard.is_pressed('esc'):
            cv2.putText(self.fenetre.image,"Tu es sorti de la page !", (125,550),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(self.fenetre.image,"Modifie le code et retente ta chance", (200,650),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            self.fenetre.afficher()
            sys.exit()
           
            
    
    def bougerVersLeBas(self,vitesse=0):
        if vitesse ==0:
            vitesse =self.vitesse
        try:
            self.effacer()
            self.ligne = self.ligne+vitesse
            self.position( self.ligne, self.colonne)
        except IndexError:
            self.effacer()
            #while not keyboard.is_pressed('esc'):
            cv2.putText(self.fenetre.image,"Tu es sorti de la page !", (125,550),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(self.fenetre.image,"Modifie le code et retente ta chance", (200,650),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            self.fenetre.afficher()
            sys.exit()
            
    def bougerVersLaGauche(self,vitesse=0):
        if vitesse ==0:
            vitesse =self.vitesse
        if self.colonne>0:
            self.effacer()
            self.colonne = self.colonne-self.vitesse
            self.position( self.ligne, self.colonne)
        else:
            self.effacer()
            #while not keyboard.is_pressed('esc'):
            cv2.putText(self.fenetre.image,"Tu es sorti de la page !", (125,550),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(self.fenetre.image,"Modifie le code et retente ta chance", (200,650),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            self.fenetre.afficher()
            sys.exit()
            
    def bougerVersLaDroite(self,vitesse=0):
        if vitesse ==0:
            vitesse =self.vitesse
        #if self.colonne+self.vitesse+self.largeur<=self.fenetre.image.shape[1]:
        try : 
            self.effacer()
            self.colonne = self.colonne+self.vitesse
            self.position(self.ligne, self.colonne)
        except IndexError:
            self.effacer()
            #while not keyboard.is_pressed('esc'):
            cv2.putText(self.fenetre.image,"Tu es sorti de la page !", (125,550),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(self.fenetre.image,"Modifie le code et retente ta chance", (200,650),\
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            self.fenetre.afficher()
            sys.exit()
            
    def position(self,ligne,colonne):
        coord = self.getCoord()
        lignePerso = coord[0]+ligne
        colonnePerso = coord[1] + colonne
        self.fenetre.image[lignePerso,colonnePerso,coord[2]] = self.listeImage[self.compteurImage][coord]
        self.fenetre.afficher()
        
    def effacer(self):
        bg2 = self.fenetre.arrierePlan[self.ligne:self.ligne+self.hauteur,self.colonne:self.colonne+self.largeur]
        self.fenetre.image[self.ligne:self.ligne+self.hauteur,self.colonne:self.colonne+self.largeur]=bg2

    def touche(self,perso2):
        sortie =False
        if perso2.ligne-self.hauteur+10<self.ligne<perso2.ligne+perso2.hauteur-10 :
            if perso2.colonne-self.largeur+10<self.colonne<perso2.colonne+perso2.largeur-10:
                sortie = True
        return sortie
    
    def verifierMission(self):
        '''
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1)
        '''
        if self.surRoute ==False:
            cv2.putText(self.fenetre.image,"Tu es sorti de la route !", (125,450),\
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2,cv2.LINE_AA)
            cv2.putText(self.fenetre.image,"Modifie le code et retente ta chance", (200,650),\
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            
            
            #self.son= pygame.mixer.Sound(os.path.join('fonctions','son','perdu.mp3'))
            
        elif (self.fenetre.arrierePlan[self.ligne+10,self.colonne+10,0]>0.9 and
              self.fenetre.arrierePlan[self.ligne+10,self.colonne+10,1]>0.9 and
              self.fenetre.arrierePlan[self.ligne+10,self.colonne+10,2]>0.9):
            cv2.putText(self.fenetre.image,"Bravo !", (300,450),\
                        cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (0, 128, 0), 2, cv2.LINE_AA)
            
               
            niveauSuivant = str(int(self.niveau)+1)
            cv2.putText(self.fenetre.image,"Tu passes au niveau "+ niveauSuivant +" !!",\
                        (40,550), cv2.FONT_HERSHEY_COMPLEX_SMALL,3, (0, 255, 255), 2, cv2.LINE_AA)
            
            #self.son= pygame.mixer.Sound(os.path.join('fonctions', 'son','victory.mp3'))
            '''
            #==============NIVEAU SUIVANT================      
            fichier = open(os.path.join( 'fonctions','arrierePlans','config.txt'),'a')
            self.niveau = str(int(self.niveau)+1)
            fichier.write("\n"+self.niveau)
            fichier.close()
            '''
            
        else :
            pygame.mixer.init()
            pygame.mixer.music.set_volume(1)
            #self.son= pygame.mixer.Sound(os.path.join( 'fonctions','son','perdu.mp3'))
            cv2.putText(self.fenetre.image,"Appuie sur Echap pour fermer", (275,650),\
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
        self.fenetre.afficher()
        '''
        for i in range(10):
            self.fenetre.afficher()
        pathList = os.listdir(os.path.join('fonctions','tentative'))
           
        with imageio.get_writer(os.path.join('fonctions','modelisation.gif'), mode='I', fps=2) as writer:
            for i in range(len(pathList)):
                path = os.path.join('fonctions','tentative','im_'+str(i)+'.png')
                image = imageio.imread(path)
                writer.append_data(image)
        
        #self.son.play()
        
        display(Image(filename=os.path.join('fonctions','modelisation.gif'),width = 400, height = 400))
        cv2.waitKey(5000)
        pygame.mixer.quit()
        '''
    def verifierSiRouteADroite(self):
        reponse = True
        if self.compteurImage ==1:
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne+150,self.colonne+50,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+150,self.colonne+50,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+150,self.colonne+50,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne+110,self.colonne+50,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+110,self.colonne+50,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+110,self.colonne+50,2]>0.90)):
                reponse = False
        elif  self.compteurImage ==3:
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne-50,self.colonne+50,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne-50,self.colonne+50,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne-50,self.colonne+50,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne-90,self.colonne+50,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne-90,self.colonne+50,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne-90,self.colonne+50,2]>0.90)):
                reponse = False
        elif  self.compteurImage ==2:
            
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne-50,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne-50,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne-50,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne+10,self.colonne-50,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne-50,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne-50,2]>0.90)):
                reponse = False
                
        elif  self.compteurImage ==0:
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+150,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+150,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+150,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne+10,self.colonne+150,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne+150,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne+150,2]>0.90)):
                reponse = False 
             
        return reponse
    
    def verifierSiRouteAGauche(self):
        reponse = True
        if self.compteurImage ==1:
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne-50,self.colonne+50,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne-50,self.colonne+50,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne-50,self.colonne+50,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne-90,self.colonne+50,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne-90,self.colonne+50,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne-90,self.colonne+50,2]>0.90)):
                reponse = False
        elif  self.compteurImage ==3:
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne+150,self.colonne+50,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+150,self.colonne+50,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+150,self.colonne+50,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne+110,self.colonne+50,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+110,self.colonne+50,1]>0.90 and
                  self.fenetre.arrierePlan[self.lign+110,self.colonne+50,2]>0.90)):
                reponse = False
        elif  self.compteurImage ==2:
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+150,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+150,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+150,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne+10,self.colonne+150,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne+150,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne+150,2]>0.90)):
                reponse = False    
        elif  self.compteurImage ==0:
            if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne-50,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne-50,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne-50,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne+10,self.colonne-50,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne-50,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne-50,2]>0.90)):
                reponse = False 
        return reponse

        
    def verifierSiOnEstSurRoute(self):
        if (not ( 0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+50,0]<0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+50,1] <0.51 and 
              0.49 <self.fenetre.arrierePlan[self.ligne+50,self.colonne+50,2] <0.51) and
             not (self.fenetre.arrierePlan[self.ligne+10,self.colonne+50,0]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne+50,1]>0.90 and
                  self.fenetre.arrierePlan[self.ligne+10,self.colonne+50,2]>0.90)):
            
            self.surRoute = False
            
    
    def estSurParking(self):
        reponse = False
        if (self.fenetre.arrierePlan[self.ligne+10,self.colonne+50,0]>0.90 and
            self.fenetre.arrierePlan[self.ligne+10,self.colonne+50,1]>0.90 and
            self.fenetre.arrierePlan[self.ligne+10,self.colonne+50,2]>0.90):
            reponse = True
        return reponse
