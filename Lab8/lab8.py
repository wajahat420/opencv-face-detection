import cv2
import os
import numpy as np


def resize_images(path):
    # print(path)
    for file in range(1, 7):
        img = cv2.imread(path + str(file) + '.jpg')
        # print(file,img)
        print('Original Dimensions : ', img.shape) 

        resized = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)

        print('Resized Dimensions : ', resized.shape)

        #cv2.imwrite('resized images/{}'.format(file), resized)
        cv2.imwrite('/home/wajahat/Desktop/AI/Lab8/resized_images/' +
                    str(file) + '.jpg', resized)


# calling the func
resize_images('/home/wajahat/Desktop/AI/Lab8/source1/')


def rotate_images(path):
    for file in range(1, 7):

        img = cv2.imread(path + str(file) + '.jpg')

        img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

        cv2.imwrite('/home/wajahat/Desktop/AI/Lab8/rotated_images/' +
                    str(file) + '.jpg', img_rotate)


# calling the func
rotate_images('/home/wajahat/Desktop/AI/Lab8/resized_images/')


def translate_images(path):
    for file in range(1, 7):

        img = cv2.imread(path + str(file) + '.jpg')

        height, width = img.shape[:2]

        quarter_height, quarter_width = height / 4, width / 4

        T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

        img_translation = cv2.warpAffine(img, T, (width, height))

        cv2.imwrite('/home/wajahat/Desktop/AI/Lab8/translated_images/' +
                    str(file) + '.jpg', img_translation)


# calling the func
translate_images('/home/wajahat/Desktop/AI/Lab8/resized_images/')


# def rename_func(path):
#    i = 0
#    #path="D:/sana"
#    for filename in os.listdir(path):
#       my_dest =str(i+1) + ".jpg"
#       my_source =path + filename
#       my_dest =path + my_dest
#       # rename() function will
#       # rename all the files
#       os.rename(my_source, my_dest)
#       i += 1

# rename_func('C:/Users/Hp/Desktop/lab 8/resized images/')
