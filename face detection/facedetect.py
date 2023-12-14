import cv2
#search this xml file at google, find it and download it
facecascade = cv2.CascadeClassifier('face detection/haarcascade_frontalface_default.xml')

image = cv2.imread("face detection/avengers.png")

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
faces = facecascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y),(x+w, y+h), (225,0,0), 2)

cv2.imshow("image", image)
cv2.waitKey()
cv2.imwrite("detectedface.jpg")