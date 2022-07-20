import cv2
from PIL import Image
from matplotlib.pyplot import text
from pytesseract import pytesseract

# Set to webcam, but could be RTSP
camera=cv2.VideoCapture(0)

# POC press the 'd' to capture 
while True:
    _,image=camera.read()
    cv2.imshow('Detection',image)
    if cv2.waitKey(1)& 0xFF==ord('d'):
        cv2.imwrite('detect.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()

# Once you press 'd' then Tesseract tries to read test
def tesseract():
    tesseract_bin = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    imgPath = "detect.jpg"
    pytesseract.tesseract_cmd=tesseract_bin
    text = pytesseract.image_to_string(Image.open(imgPath))
    print(text[:-1])
tesseract()
    