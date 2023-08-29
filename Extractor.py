import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def remove_garbage(text, garbage_list):
    for char in garbage_list:
        text = text.replace(char, '')
    return text.replace('. ', ' ')

def Extract_Table(path):
    img = Image.open(path)
    data = tess.image_to_string(img)

    data = remove_garbage(data, '=#«»|')
    data = data.split('\n')
    data = list(filter(lambda x: x!='', data))

    for i in range(len(data)):
        data[i] = data[i].split(' ')
        data[i] = list(filter(lambda x: x!='', data[i]))

    return data