# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 00:38:04 2017

@author: SpectralMD
"""

import numpy as np
import re
from PIL import Image
#a=[1,2,3,4,5,6,7,8,9,10,11,12]
#b=list(np.reshape(a,(-1,2,2)))
#print(type(b))
#print(b)
#
#
#c=np.reshape(a,(-1,2,3))
#print(c)
##d=c.transpose((1,2,0))
##print(d)
#
#e=c[:,:,::-1]
#print(e)

#def atoi(text):
#    return int(text) if text.isdigit() else text
#
#def natural_keys(text):
#    '''
#    alist.sort(key=natural_keys) sorts in human order
#    http://nedbatchelder.com/blog/200712/human_sorting.html
#    (See Toothy's implementation in the comments)
#    '''
#    return [ atoi(c) for c in re.split('_', text) ]
#
#a=['abc_1_0.h5','abc_1_3.h5','abc_1_10.h5','abc_1_2.h5','abc_1_12.h5']
#
#b = [e.split('.h5')[0] for e in a]
#
#b.sort(key=natural_keys)


im_=np.array(range(12))
im_=im_.reshape((3,4))
a=im_[:,1:-2]
#print(im_)
#xoffset = 4
#yoffset = 4
#im_pad=np.pad(im_,((0,0),(xoffset,xoffset-1),(yoffset,yoffset-1)),'reflect')
#
#print(im_pad)
#
#print(np.array(range(0,10,1)))




#img1 = Image.open('E:/disk2/Faliu/cnn/v1/script/infer.png')
#img2 = Image.open('E:/disk2/Faliu/cnn/v1/script/true.png')
#img1.show()
#img2.show()
#
#img1Tmp = np.array(img1,dtype=np.float32)
#img2Tmp = np.array(img2,dtype=np.float32)
#
#img11 =  img1Tmp[17:-16,17:-16]
#img22 =  img2Tmp[17:-16,17:-16]
#
#img11 = Image.fromarray(np.uint8(img11))
#img22 = Image.fromarray(np.uint8(img22))
#
#img11.show()
#img22.show()

#a = np.array(range(12))
#b = np.reshape(a,(-1,2,2))
#
#print(b)
#
#c = b[:,1,1]
#print(c)
#
#
#e = np.zeros((3,2,2))
#
#for iter in range(4):
#    row = iter // 2
#    col = iter % 2
#    e[:,row,col] = c
#    
#print(e)
#
#print(10%3)
#print(10//3)

fclass=np.array([10682767,14750079,623349,20076880,2845085,6166762,743859,714595,3719877,405385,184967,2503995])
fimg=np.array([366,365,366,367,349,319,351,173,360,317,201,367])

fclass=fclass/(fimg*480*360)
print(fclass)

med = np.median(fclass)
print(med)

wclass = med / fclass
print(wclass)



















