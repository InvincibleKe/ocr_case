# coding=UTF-8
import requests
import base64
def img_to_base64(img_path):
    with open(img_path, 'rb')as read:
        b64 = base64.b64encode(read.read())
    return b64
if __name__ == '__main__':
    img_b64 = img_to_base64('data/test-90.jpg')
    r = requests.post(" http://em.exceltools.cn:8888/api/v1/AI_detect", data={'model': 'ZKKTZS', 'image': img_b64})
    #r = requests.post("http://0.0.0.0:5000/api/v1/AI_detect", data={'model': 'ZKKTZS', 'image': img_b64})
    #r = requests.post(url=url, data={'img': img_b64})
    print(r.json())