import picamera
import PIL
from PIL import Image
import io
import time
import logger

Samples = 5
pauseBetweenPic = 1;
deviation = 5
camera = picamera.PiCamera()

def avg(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def getBrithnessFromStream(stream):
    stream.seek(0)
    image = Image.open(stream)
    image = image.convert ('RGB')
    #coordinates of the pixel
    X,Y = 0,0
    #Get RGB
    pixelRGB = image.getpixel((X,Y))
    R,G,B = pixelRGB 
    brightness = sum([R,G,B])/3 ##0 is dark (black) and 255 is bright (white)
    return brightness
    
    
def getThreshold():
    SamplesResults = ([])    
    for x in range(0, Samples):
        stream = io.BytesIO()
        camera.start_preview()
        time.sleep(pauseBetweenPic)
        camera.capture(stream, format='jpeg')
        brightness = getBrithnessFromStream(stream)
        SamplesResults.append(brightness)
        logger.log("camera brightness: "+ str(brightness))
    return avg(SamplesResults)
    
def isThereBaby(threshold):
    return getThreshold() - deviation <= threshold