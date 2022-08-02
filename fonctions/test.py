# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:59:47 2022

@author: pierr
"""

import time
import matplotlib.pyplot as plt
import IPython.display as display
import numpy as np
import os
def testImage():
    d=display.display('test', display_id='essai')
    time.sleep(0.5)
    for i in range(10):
        if i%2==0:
            text = "ap_niveau0.png"
            img = np.zeros((200,200))
        else: 
            text = "ap_niveau1.png"
            img =  np.ones((200,200))
        dispImg = display.Image(filename=os.path.join('fonctions','arrierePlans',text),width = 400, height = 400)
        display.update_display(dispImg,display_id='essai')

        time.sleep(0.1)

    print('done')
    
def testImage2():
    for i in range(10):
        if i%2==0:
            text = "ap_niveau2.png"
            img = np.zeros((200,200))
        else: 
            text = "ap_niveau3.png"
            img =  np.ones((200,200))
        dispImg = display.Image(filename=os.path.join('fonctions','arrierePlans',text),width = 400, height = 400)
        display.update_display(dispImg,display_id='essai')

        time.sleep(0.1)