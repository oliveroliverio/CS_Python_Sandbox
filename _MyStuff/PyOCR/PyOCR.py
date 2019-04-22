# documentation: https://pypi.org/project/pyscreenshot/
# need to install this on all python runners

import pyscreenshot as ImageGrab
import time
import pytesseract as pt

# wait 2 sec for you to pull up the image you want to store
time.sleep(2)

# store screen shot in variable 'im'
im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2

# send 'im' to OCR
text = pt.image_to_string(im)

print(text)


