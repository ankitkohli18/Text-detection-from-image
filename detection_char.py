#In this we are going to extract text from image word by word
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('images\im4.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Detecting Characters
h_img =  img.shape[0]
w_img = img.shape[1]
boxes = (pytesseract.image_to_boxes(img))
for character in boxes.splitlines():
  character = character.split(' ')
  x,y,w,h = int(character[1]), int(character[2]), int(character[3]), int(character[4])
  cv2.rectangle(img, (x,h_img-y), (w, h_img-h), (0,255,0), 1)
  cv2.putText(img, character[0], (x, h_img-y+20), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255, 2))

#printing Result
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
