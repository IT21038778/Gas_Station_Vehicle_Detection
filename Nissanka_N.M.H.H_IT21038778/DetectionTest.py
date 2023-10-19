import cv2

#Reading an image, resizing it and converting it to greyscale
image = cv2.imread("test6.jpg")
if image is None:
    print("Image not found.")
    exit()
image = cv2.resize(image, (450, 250))#width and height 
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Greyscale conversion

blur = cv2.GaussianBlur(grey, (5, 5), 0)

car_cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + car_cascade_src)
if car_cascade.empty():
    print("Error: Cascade Classifier not loaded.")
    exit()

cars = car_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Cars", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(len(cars), "cars found")
