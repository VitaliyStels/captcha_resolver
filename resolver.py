import os
import pytesseract
import cv2

dir = 'static/uploads'
files = os.listdir(dir)

async def check_image():
    if len(files) > 0:
        for i in files:
            text = recognize_text(f'{dir}/{i}')
            os.remove(f'{dir}/{i}')
            print(f'{dir}/{i} was checked and removed')
            return text


def recognize_text(image_path):

  img = cv2.imread(image_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
  config = '--psm 6'  # Page segmentation mode (adjust based on image content)
  text = pytesseract.image_to_string(thresh, config=config)

  return text    