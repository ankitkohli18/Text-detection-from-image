import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('images\im4.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Detecting words
h_img =  img.shape[0]
w_img = img.shape[1]
boxes = (pytesseract.image_to_data(img))
for x,character in enumerate(boxes.splitlines()):
  if x!=0:
    character = character.split()
    print(character)
    if len(character)==12:
      x,y,w,h = int(character[6]), int(character[7]), int(character[8]), int(character[9])
      cv2.rectangle(img, (x,y), (w+x, h+y), (0,255,0), 1)
      cv2.putText(img, character[11], (x,y-5), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255, 2))
    
  

#printing Result  
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()