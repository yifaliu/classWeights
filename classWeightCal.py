# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:28:17 2017

@author: Faliu Yi

"""

import numpy as np
import os
import h5py
import glob

def classWeight(path,row,col):
    fileName = glob.glob('*.h5')
    zerosNum = 0         # num of zeros for class 0
    onesNum = 0
    zerosNumImg = 0      # the number of image including class o times the total number of pixel of one image
    onesNumImg = 0
    for name in fileName:
        print(name)
        f = h5py.File(name,'r')
        lab_=list(f['label'])
        print(len(lab_))
        for iter in range(len(lab_)):
            label = lab_[iter][0,:,:]
            zeroTmp = (label == 0).sum()
            oneTmp = (label == 1).sum()
            
            if zeroTmp != 0:
                zerosNumImg += row * col
                zerosNum +=zeroTmp
                #print('zeros')
            if oneTmp != 0:
                onesNumImg += row * col
                onesNum += oneTmp
                #print('ones')

    
    fclass = np.array([zerosNum, onesNum])
    fimg = np.array([zerosNumImg, onesNumImg])    
    freClass = fclass/(fimg*1.0)
    med = np.median(freClass)  
    
    cw = med/freClass
    return cw
        
 

if __name__ == "__main__":
    path='/disk2/Faliu/segNet/data'
    row = 360
    col = 480
    cw = classWeight(path,row,col)
    print(cw)

