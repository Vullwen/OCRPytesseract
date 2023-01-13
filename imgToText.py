import pytesseract
from PIL import Image
import os


pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\cpinquier\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'



def main():
    imagePath = 'Programmes/imgToText/image/'
    imagePathAbs = os.path.abspath(imagePath)
    
    #si le dossier image est vide:
    images = get_image_paths(imagePathAbs)
    
    allImages = os.listdir(imagePathAbs)
    
    for el in images:
        print("~"*50)
        print("texte numéro: ", images.index(el)+1,"\n(", allImages[images.index(el)], ")\n" )
        imageAct = Image.open(el).convert('L')

        # Recognize the text in the image
        text = pytesseract.image_to_string(imageAct)

        # Print the recognized text
        print(text)


def get_image_paths(folder):
    # Check if the folder exists
    if not os.path.exists(folder):
        print("folder does not exist")
        return False

    # Get the list of all files in the folder
    files = os.listdir(folder)
    
    # If the folder is empty, return False
    if not files:
        print("folder is empty")
        return False
    
    # Otherwise, return the paths of all the files in the folder
    paths = []
    for file in files:
        path = os.path.join(folder, file)
        paths.append(path)
    return paths

if __name__ == '__main__':
    main()
    
