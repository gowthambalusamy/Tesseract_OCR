from PIL import Image
import pytesseract
import sys
#print sys.argv[1]
im = Image.open(sys.argv[1])
text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
