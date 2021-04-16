import requests
if __name__ == '__main__':
    url = 'http://192.168.10.41:8080/api/v1/AI_detect'
    file = open('data/case1.jpg', 'rb')
    res = requests.post(url=url, data={'model': 'ZKKTZS', 'image': file})
    res = res.json()
    print(res)