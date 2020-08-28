from PIL import Image
import os
import PIL

def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    #print(imgwidth,imgheight)
    height = imgheight/yPieces - 7
    #print(height)
    width = imgwidth/xPieces
    
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
           # a.show() 
            try:
                a.save("output_11\\" + filename + "-" + str(i) + "-" + str(j) + file_extension)
            except:
                pass
            
            
            

imgcrop("CamScanner 08-10-2020 01.17.45_4 - layla 64.jpg",3, 10)



#def Size_of_the_Image(Image_name):
#    
#    image = PIL.Image.open(Image_name)
#    
#    
#    width, height = image.size
#    
#    
#    #print(width, height)
#    
#    return  width, height







