import cv2
from math import *
import numpy as np
import base64
from test import img_to_base64
def rotate_file(img_b64, angle):
    # 角度是按照逆时针旋转
    '''
    img = file.read()
    img = np.fromstring(img, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = np.array(img)'''
    img_data = base64.b64decode(img_b64)
    nparr = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
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
    img_b64 = img_to_base64('data/test9.jpg')
    print(img_b64[:100])
    img = rotate_file(img_b64, 90)
    retval, buffer = cv2.imencode('.jpg', img)
    img_b64 = base64.b64encode(buffer)
    img = rotate_file(img_b64, 90)
    cv2.imshow('image', img)
    cv2.waitKey(0)