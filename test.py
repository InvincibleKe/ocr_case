# coding=UTF-8
import requests

if __name__ == '__main__':
    data = {'model': 'ZKKTZS'}
    file = open('data/case1.jpg', 'rb')
    r = requests.post("http://192.168.10.41:5000/api/v1/AI_detect", data=data, files = {'image': file})
    print(r.json())
'''
if __name__ == '__main__':
    url = 'http://192.168.10.41:8080/api/v1/AI_detect'
    file = open('data/case1.jpg', 'rb')
    res = requests.post(url=url, data={'model': 'ZKKTZS'}, files = {'image': file})
    res = res.json()
    print(res)'''