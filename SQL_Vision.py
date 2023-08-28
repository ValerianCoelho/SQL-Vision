# import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image, ImageTk
from customtkinter import *
from tkinter import filedialog

def browse():
    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif")])
    if filePath:
        fileInput.insert(0, filePath)
        image = Image.open(filePath)
        new_width = 500
        aspect_ratio = image.width / image.height
        new_height = int(new_width / aspect_ratio)
        resized_image = image.resize((new_width, new_height))
        tk_image = ImageTk.PhotoImage(resized_image)
        imageLabel.configure(image=tk_image)
        imageLabel.image = tk_image
        imageLabel.grid(padx=10, pady=10, row=3, column=0, columnspan=5)

def page2():
    homeFrame.pack_forget()

    constraintFrame = CTkFrame(window)
    constraintFrame.pack(padx=20, pady=20)

    detailsLabel = CTkLabel(constraintFrame, text='Enter Table Details', font=CTkFont(size=15, weight="bold"))
    detailsLabel.grid(padx=20, pady=20, row=0, column=0)

    tableNameLabel = CTkLabel(constraintFrame, text='Enter Table Name : ')
    tableNameLabel.grid(padx=10, pady=10, row=1, column=0)

    tableNameinput = CTkEntry(constraintFrame, placeholder_text = 'STUDENT')
    tableNameinput.grid(padx=10, pady=10, row=1, column=3)

    constraintsLabel = CTkLabel(constraintFrame, text='Enter Table Constraints :', font=CTkFont(size=15, weight="bold"))
    constraintsLabel.grid(padx=20, pady=20, row=2, column=0) 

# def remove_garbage(text, garbage_list):
#     for char in garbage_list:
#         text = text.replace(char, '')
#     return text.replace('. ', ' ')

# img = Image.open('./Image_Test_1.png')
# data = tess.image_to_string(img)

# data = remove_garbage(data, '=#«»|')
# data = data.split('\n')
# data = list(filter(lambda x: x!='', data))

# for i in range(len(data)):
#     data[i] = data[i].split(' ')
#     data[i] = list(filter(lambda x: x!='', data[i]))

# print(data)

window = CTk()

window.title('SQL Vision')

homeFrame = CTkFrame(window)
homeFrame.pack(padx=20, pady=20)

titleField = CTkLabel(homeFrame, text='SQL Vision', font=CTkFont(size=25, weight='bold'))
titleField.grid(padx=10, pady=10, row=0, column=0, columnspan=5, sticky='nsew')

selectFileField = CTkLabel(homeFrame, text='Select Image: ', font=CTkFont(size=20))
selectFileField.grid(padx=10, pady=10, row=1, column=0, columnspan=1)

fileInput = CTkEntry(homeFrame, placeholder_text = "Path to Image", width=300)
fileInput.grid(padx=(20, 0), pady=10, row=2, column=0, columnspan=3, sticky='nsew')

browseBtn = CTkButton(homeFrame, command = browse , text = "Browse")
browseBtn.grid(padx=10, pady=10, row=2, column=3)

imageLabel = CTkLabel(homeFrame, text='') # It is packed in the Browser Function

proceedBtn = CTkButton(homeFrame, command = page2 , text = "Proceed")
proceedBtn.grid(padx=10, pady=10, row=4, column=0, columnspan=5)

window.mainloop()