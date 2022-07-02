#sepia effect
import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline
from draw import Draw
from qoutes import Qoutes

def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))


class Effect:
    def __init__(self, image):
        self.image = image
        
       
    def Sepia(self):
        img_sepia = np.array(self.image, dtype=np.float64) # converting to float to prevent loss
        img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                        [0.349, 0.686, 0.168],
                                        [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
        img_sepia[np.where(img_sepia > 255)] = 255 # normalizing values greater than 255 to 255
        img_sepia = np.array(img_sepia, dtype=np.uint8)
        
        text = Qoutes()
        rect_text = Draw(text)
        rect_text.DrawRect(img_sepia)
        rect_text.DrawText(img_sepia)        
        return img_sepia


    #HDR effect
    def HDR(self):
        hdr = cv2.detailEnhance(self.image, sigma_s=12, sigma_r=0.15)
        text = Qoutes()
        rect_text = Draw(text)
        rect_text.DrawRect(hdr)
        rect_text.DrawText(hdr)
        return  hdr


    def Summer(self):
        increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel,red_channel  = cv2.split(self.image)
        red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
        sum = cv2.merge((blue_channel, green_channel, red_channel))
        text = Qoutes()
        rect_text = Draw(text)
        rect_text.DrawRect(sum)
        rect_text.DrawText(sum)
        return sum


    #winter effect
    def Winter(self):
        increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel,red_channel = cv2.split(self.image)
        red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
        win = cv2.merge((blue_channel, green_channel, red_channel)) 
        text = Qoutes()
        rect_text = Draw(text)
        rect_text.DrawRect(win)
        rect_text.DrawText(win)
        return win
    
    # brightness adjustment
    def Dark(self):
        img_bright = cv2.convertScaleAbs(self.image, beta = -30)
        text = Qoutes()
        rect_text = Draw(text)
        rect_text.DrawRect(img_bright)
        rect_text.DrawText(img_bright)
        return img_bright
    
    
    def Sharp(self):
        kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
        
        image_sharp = cv2.filter2D(src=self.image, 
                                   ddepth=-1, 
                                   kernel=kernel)
        text = Qoutes()
        rect_text = Draw(text)
        rect_text.DrawRect(image_sharp)
        rect_text.DrawText(image_sharp)
        return image_sharp

