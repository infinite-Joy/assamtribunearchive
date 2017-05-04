import pytesseract
from PIL import Image
from sys import argv

print(pytesseract.image_to_string(Image.open(argv[1])))