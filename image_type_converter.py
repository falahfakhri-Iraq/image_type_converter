# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 17:13:05 2021

@author: FALAH FAKHRI


Module: image_type_converter.py
==================================================================================================================
This is a premilinary image type converter from float32 into to one of two types unit8 (0 to 255) or
int16 bit (-32768 to 32767).
==================================================================================================================
"""


data = "Input.tif"

outfn = "Image_converted.tif"

from skimage import img_as_ubyte, img_as_int

import tifffile as tif

import cv2



def image_type_converter(img:float, target_save:str, target_type:str):
    
    """Image type converter
   
   parameters
   ----------
   img: source of an image input as tif float type
   target_save: the target of save image destination includes the *.tif format
   target_type: choose one of the desired type unit8, or int16 
   """
    
    img = tif.imread(img)
    
    if target_type == 'unit8':
        
        img_converted_unit8 = img_as_ubyte(img)
        cv2.imwrite(target_save, img_converted_unit8)
    
    elif target_type == 'int16':
        
        img_converted_int16 = img_as_int(img)
        cv2.imwrite(target_save, img_converted_int16)
        
        
image_type_converter(data, outfn, 'unit8')
