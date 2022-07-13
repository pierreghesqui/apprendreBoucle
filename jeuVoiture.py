from voiture import Voiture

# ===================================================
maVoiture = Voiture()
while not maVoiture.estSurParking():
    if maVoiture.verifierSiRouteADroite():
        maVoiture.tournerADroite()
    elif maVoiture.verifierSiRouteAGauche():
        maVoiture.tournerAGauche()
    maVoiture.avancer()

#===================================================
maVoiture.verifierMission()

