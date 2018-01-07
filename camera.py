import picamera
import PIL
from PIL import Image
import io
import time

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# "Rewind" the stream to the beginning so we can read its content

stream.seek(0)
image = Image.open(stream)
print "Opening ..."
#camera = picamera.PiCamera()

#camera.capture('image.jpg')

#imag = Image.open("image.jpg")

image = image.convert ('RGB')
#coordinates of the pixel
X,Y = 0,0
#Get RGB
pixelRGB = image.getpixel((X,Y))
R,G,B = pixelRGB 

brightness = sum([R,G,B])/3 ##0 is dark (black) and 255 is bright (white)

print brightness