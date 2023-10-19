import cv2
import numpy as np

image = cv2.imread('test3.jpg')
image = cv2.resize(image, (450, 250))
if image is None:
    print("Image not found.")
    exit()

cv2.namedWindow('Tonal Transformation')
contrast = 1.0
brightness = 0

def update_tonal_transformation(x):
    global contrast, brightness
    contrast = x / 10.0
    alpha = contrast
    beta = brightness
    tonal_transformed = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imshow('Tonal Transformation', tonal_transformed)

cv2.createTrackbar('Contrast', 'Tonal Transformation', 10, 20, update_tonal_transformation)
cv2.createTrackbar('Brightness', 'Tonal Transformation', 0, 100, update_tonal_transformation)
update_tonal_transformation(10) 
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  
        break
    
cv2.destroyAllWindows()
