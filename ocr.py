import pytesseract
import keyboard
import time
import os
#import win10toast
import pyperclip

from PIL import ImageGrab
from PIL import Image

def fooeng():
    foo('eng')

def foorus():
    foo('rus')

def foo(_lang='eng'):
    print(" OSR - "+_lang)
        
    im = ImageGrab.grabclipboard()
    image_path = "C:/Windows/Temp"
    
    try:
        im.save(f"{image_path}/TEXT.png")
        
        # time.sleep (1)

        img = Image.open(f"{image_path}/TEXT.png")
        pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"

        # custom_config = r'--oem 3 --psm 13'
        # text = pytesseract.image_to_string(img, lang="rus")
        text = pytesseract.image_to_string(img, lang=_lang)
        print(text)

        pyperclip.copy(text)
        
        os.remove(f"{image_path}/TEXT.png")
        
        print(_lang+ " [INFO] The text was successfully saved to the clipboard.")
        with open('out-text.txt', 'a') as f:
            f.write(text+"\n")
    except Exception as err:
        print("---error---",err)

    
keyboard.add_hotkey('Alt + q', fooeng)
keyboard.add_hotkey('Alt + r', foorus)

print(" [INFO] Save a picture with text to the clipboard and recognize it with a hotkey:\n     For Russian text <Alt + r> \n     For English text <Alt + q>")
print(" [INFO] Exit the program <Alt + z>")

#keyboard.wait('Ctrl + Alt + q')
keyboard.wait('Alt + z')
