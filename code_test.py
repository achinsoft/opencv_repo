import numpy as np
import cv2
import pandas as pd

img = cv2.imread("img/grey.PNG", 0)
print(img.shape)
img2 = cv2.imread("img/grey.PNG", 1)
cv2.imshow('image', img)
cv2.imshow('imag1e', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
#cv2.imwrite('img/modfile.png', img)
img = cv2.imread("img/modfile.png", 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#face_cascade = cv2.CascadeClassifier('img/haarcascade_frontalface_default.xml')
#print(face_cascade)
#face = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)


