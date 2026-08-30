import mss

sct = mss.mss()

class PixelRead():
    """Position and hex color code of the pixel"""
    def __init__(self,left,top,color_hex):
        self.monitor = {
            "left": left,
            "top" : top,
            "width" : 1,
            "height" : 1
        }
        self.r = (color_hex >> 16) & 0xff
        self.g = (color_hex >> 8) & 0xff
        self.b = color_hex & 0xff
        
    def read_pixel(self):
        """Reads the pixel value and returns a boolean"""
        shot = sct.grab(self.monitor)
        sb,sg,sr,_ = shot.raw
        if sr == self.r and sg == self.g and sb == self.b:
            return True
        else:
            return False