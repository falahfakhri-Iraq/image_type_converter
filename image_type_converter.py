# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 17:13:05 2021

@author: FALAH FAKHRI


Module: image_type_converter.py
==================================================================================================================
This is a premilinary image type converter from float32 into to one of many different types,

Convert to floating point (integer types become 64-bit floats). float -1 to 1 or 0 to 1

Convert to 8-bit uint. uint8 0 to 255

Convert to 16-bit uint. uint16 0 to 65535

Convert to 16-bit int. int16 -32768 to 32767

==================================================================================================================
"""


data = "D:/Australia_Project\image_data/flood_18_03_2021_Descending_mode/GRD/resampled_data_F1/sigma0_S1A_IW_GRDH_1SDV_20210324_21DF_VH.tif"

outfn = "D:/Australia_Project/image_data/flood_18_03_2021_Descending_mode/GRD/resampled_data_F1/Image_converted.tif"

from skimage import (img_as_float,
                    img_as_ubyte,
                    img_as_uint,
                    img_as_int,
                    io
                    )
                    
import cv2



def image_type_converter(img:float, target_save:str, target_type:str):
    
    """Image type converter 
   
   parameters
   ----------
   img: source of an image input as tif float type
   target_save: the target of save image destination includes the *.tif format
   target_type: choose one of the desired type unit8, or int16 
   """
    
    img = io.imread(img)
    
    # Convert to floating point (integer types become 64-bit floats) 
    
    if target_type == '64-bitfloats':
        
        img_converted_64 = img_as_float(img)
        cv2.imwrite(target_save, img_converted_64)
        
    # Convert to 8-bit uint.
    
    elif target_type == 'unit8':
        
        img_converted_unit8 = img_as_ubyte(img)
        cv2.imwrite(target_save, img_converted_unit8)
        
    # Convert to 16-bit uint.
    
    elif target_type == '16unit':
        img_converted_16unit = img_as_uint(img)
        cv2.imwrite(target_save, img_converted_16unit)
        
    else:
        
        # Convert to 16-bit int.
        
        target_type == '16int'
        img_converted_16int = img_as_int(img)
        cv2.imwrite(target_save, img_converted_16int)
        
def image_properties(filename):
    filename=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    
    print('dtype:',filename.dtype, 'Min:', filename.min(), 'Max:', filename.max(), 'shape:', filename.shape)  
        
        
if __name__ == "__main__":
    
    image_type_converter(data, outfn, 'unit8')
    image_properties(outfn)

