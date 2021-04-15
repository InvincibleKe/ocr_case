import cv2
from math import *
import numpy as np
from PIL import Image
def rotate_file(file, angle):
    # 角度是按照逆时针旋转
    img = file.read()
    img = np.fromstring(img, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = np.array(img)
    height, width = img.shape[:2]

    degree = angle
    # 旋转后的尺寸
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))

    matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)

    matRotation[0, 2] += (widthNew - width) / 2
    matRotation[1, 2] += (heightNew - height) / 2

    imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
    return imgRotation

if __name__ == '__main__':
    file_path = 'data/test-90.jpg'
    img = open(file_path, 'rb')
    img = rotate_file(img, 270)
    cv2.imshow('image', img)
    cv2.waitKey(0)