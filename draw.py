import cv2   

class Draw:
    def __init__(self, text):
        self.text = text
        self.position   = (0,0)
        self.x, self.y = self.position
        self.bgColor    = (0,0,0)
        self.font       = cv2.FONT_HERSHEY_COMPLEX_SMALL
        self.fontScale  = 1
        self.fontColor  = (0,0,255)
        self.fontThickness = 2
        
        self.text_size, _ = cv2.getTextSize(self.text, 
                                            self.font, 
                                            self.fontScale, 
                                            self.fontThickness)
        self.text_width, self.text_height = self.text_size
        
        
     
    def DrawRect(self, image):   
        img_height, img_width = image.shape[0], image.shape[1]     
        
        cv2.rectangle(image, self.position,
            (
            self.x + self.text_width + 30, 
            self.y + self.text_height + 30),
            self.bgColor, -1)
    
        
        cv2.rectangle(image, (int(img_width/4), int(img_height/1.1)), 
                                 (int(img_width/1.2), int(img_height)), 
                                 (0,0,0), -1)
        
    def DrawText(self, image):
        img_height, img_width = image.shape[0], image.shape[1] 
        cv2.putText(image,
                    self.text,
                    (self.x, self.y + self.text_height + self.fontScale +10),
                    self.font,
                    self.fontScale,
                    self.fontColor,
                    self.fontThickness,
                    cv2.LINE_AA)
        
        cv2.putText(image,
                    "Order Now",
                    (int(img_width/4),  int(img_height-15)),
                    self.font,
                    5,               # Font Scale
                    self.fontColor,
                    10,              # Font Thickness
                    cv2.LINE_AA)
