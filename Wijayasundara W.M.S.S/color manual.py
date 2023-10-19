import cv2
import numpy as np

def color_balance(image, red, green, blue):
    # Apply the scaling factors to each channel
    balanced_image = np.copy(image)
    balanced_image[:, :, 2] = np.uint8(np.clip(balanced_image[:, :, 2] * red, 0, 255))
    balanced_image[:, :, 1] = np.uint8(np.clip(balanced_image[:, :, 1] * green, 0, 255))
    balanced_image[:, :, 0] = np.uint8(np.clip(balanced_image[:, :, 0] * blue, 0, 255))

    return balanced_image

def update_balance(*args):
    red = cv2.getTrackbarPos('Red', 'Color Balancing Bar') / 100.0
    green = cv2.getTrackbarPos('Green', 'Color Balancing Bar') / 100.0
    blue = cv2.getTrackbarPos('Blue', 'Color Balancing Bar') / 100.0

    balanced_image = color_balance(image, red, green, blue)
    color_bar = np.hstack((image, balanced_image))
    cv2.imshow('Color Balancing Bar', color_bar)

# Load your image
image = cv2.imread('test2.jpg')

# Create a window and display the color balancing bar
cv2.namedWindow('Color Balancing Bar')

# Create trackbars for adjusting the color balance
cv2.createTrackbar('Red', 'Color Balancing Bar', 100, 200, update_balance)
cv2.createTrackbar('Green', 'Color Balancing Bar', 100, 200, update_balance)
cv2.createTrackbar('Blue', 'Color Balancing Bar', 100, 200, update_balance)

# Initialize the color balance
update_balance()

# Wait for the user to adjust the color balance
cv2.waitKey(0)
cv2.destroyAllWindows()
