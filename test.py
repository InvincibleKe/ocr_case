# coding=UTF-8
import requests

if __name__ == '__main__':
    user_info = {'model': 'ZKKTZS'}
    file = open('data/case1.jpg', 'rb')
    r = requests.post("http://127.0.0.1:5000/api/v1/AI_detect", data=user_info, files = {'image': file})
    print(r.json())
'''
if __name__ == '__main__':
    url = 'http://192.168.10.41:8080/api/v1/AI_detect'
    file = open('data/case1.jpg', 'rb')
    res = requests.post(url=url, data={'model': 'ZKKTZS'}, files = {'image': file})
    res = res.json()
    print(res)'''