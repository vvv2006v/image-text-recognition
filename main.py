import pytesseract
from PIL import Image

img = Image.open('')  # relative path to image
pytesseract.pytesseract.tesseract_cmd = r''

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config)

with open('', 'w') as text_file:  # text file for text from picture
    text_file.write(text)
