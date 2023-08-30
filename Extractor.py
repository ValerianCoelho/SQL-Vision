import os
import Color
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
from PIL import Image

garbage = '=#«»|'

def remove_garbage(text, garbage_list):
    for char in garbage_list:
        text = text.replace(char, '')
    return text.replace('. ', ' ')

def Extract_Table(path):
    try:
        img = Image.open(path)
    except:
        print(Color.red, 'Unable to Load File', Color.reset, sep='')
        input()
        os.system('pause')
        
    data = tess.image_to_string(img)

    data = remove_garbage(data, garbage)
    data = data.split('\n')
    data = list(filter(lambda x: x!='', data))

    for i in range(len(data)):
        data[i] = data[i].split(' ')
        data[i] = list(filter(lambda x: x!='', data[i]))

    return data