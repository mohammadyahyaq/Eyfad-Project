# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 06:25:33 2020

@author: LENOVO
"""

from PIL import Image


#تعديل دقة الصوره
im = Image.open("IMG-5848.jpg")
im.save("IMG-5848-300dpi.png", dpi=(300,300))#save image




mm