import numpy as np
import cv2
import pandas as pd


img=cv2.imread("img/traffic1.jpeg", 0)
print(img.shape)
img=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

print(int(img.shape[0]/4))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
