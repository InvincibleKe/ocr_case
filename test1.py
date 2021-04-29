import cv2
if __name__ == '__main__':
    img = cv2.imread('data/text_background.png', cv2.IMREAD_UNCHANGED)
    cv2.imshow('hhh', img)
    cv2.waitKey(0)