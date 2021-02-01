import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Loading the image to be tested
for file in range(1, 4):
    test_image = cv2.imread('/home/wajahat/Desktop/AI/Lab9/pics/' + str(file) + '.jpg')

# Converting to grayscale
    test_image_gray = cv2.cvtColor(test_image , cv2.COLOR_BGR2RGB)

# Displaying the grayscale image
    plt.figure()
    plt.imshow(test_image_gray, cmap='gray')


def convertToRGB(image):

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


for file in range(1, 4):
    test_image = cv2.imread(
        '/home/wajahat/Desktop/AI/Lab9/pics/' + str(file) + '.jpg')
    haar_cascade_face = cv2.CascadeClassifier(
        '/home/wajahat/Desktop/AI/Lab9/haarcascade_frontalface_default.xml')
# convert image to RGB and show image
    plt.figure() 
    plt.imshow(convertToRGB(test_image))


def detect_faces(cascade, test_image, scaleFactor=1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()

    # convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(
        gray_image, scaleFactor=scaleFactor, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (100, 255, 0), 10)

    return image_copy


for file in range(1, 4):
    test_image = cv2.imread(
        '/home/wajahat/Desktop/AI/Lab9/pics/' + str(file) + '.jpg')
    img = detect_faces(haar_cascade_face, test_image)
    plt.figure()
    plt.imshow(convertToRGB(img))
    plt.show()
    
    
