import requests
import image_rotation
import cv2
import numpy as np
from io import BufferedReader, BytesIO
def delete_blank(original_data):
    data_later = []
    for item in original_data:
        if item[1] == '':
            continue
        data_later.append(item)
    return data_later
def array2buffer(data_array):
    img_encode = cv2.imencode('.jpg', data_array)[1]
    str_encode = img_encode.tostring()
    data_bytes = BytesIO(str_encode)
    data_bytes.name = '....jpg'
    data_buffer = BufferedReader(data_bytes)
    return data_buffer
def read_trurl():
    path = 'data/tr_url.txt'
    data = ''
    with open(path, "r") as f:
        data = f.readline()
    return data
def getKeyData(text):
    i = 0
    key_data = {}
    department = ''
    for one in text:
        if '当事人姓名' in one[1]:
            key_data['partyName'] = text[i+1][1]
        if '案件编号' in one[1]:
            key_data['caseNo'] = text[i+1][1]
        if '身份证' in one[1] and '代理人' not in one[1]:
            key_data['idNo'] = text[i+1][1]
        if '联系方式' in one[1]:
            key_data['phone'] = text[i+1][1]
        if '金额' in one[1]:
            key_data['amount'] = text[i+1][1]
        if '账号' in one[1]:
            key_data['acctNo'] = text[i+1][1]
        if '户名' in one[1]:
            key_data['acctName'] = text[i+1][1]
        if '开户行' in one[1] and '行号' not in one[1]:
            key_data['bankName'] = text[i+1][1]
        if '开户行行号' in one[1] and '当事人' not in text[i+1][1]:
            key_data['bankCode'] = text[i+1][1]
        if department == '' and ('派出所' in one[1] or '大队' in one[1] or '看守所' in one[1] or '拘留所' in one[1] or '水利' in one[1]):
            key_data['department'] = one[1]
            department = one[1]
        i += 1
    return key_data
def imgFile_recognition(file):
    key_data = {}
    url = read_trurl()
    angle = 0
    text = []
    while (True):
        res = requests.post(url=url, data={'compress': 0}, files={'file': file})
        print(res)
        res = res.json()
        text = res['data']['raw_out']
        text = delete_blank(text)
        if text[0][2] >= 0.8 and '通知书' in text[0][1]:
            break
        angle += 90
        file.seek(0)
        img = image_rotation.rotate_file(file, angle)
        file = array2buffer(np.array(img))
    # for one in text: print(one)
    key_data = getKeyData(text)
    return key_data

if __name__ == '__main__':
    file = open('data/case1.jpg', 'rb')
    key = imgFile_recognition(file)
    for v, k in key.items():
        print('{v}:{k}'.format(v=v, k=k))
    print(key)

    '''
    url = 'http://192.168.10.41:8089/api/tr-run/'
    def img_to_base64(img_path):
        with open(img_path, 'rb')as read:
            b64 = base64.b64encode(read.read())
        return b64
    img_b64 = img_to_base64('data/test7.jpg')
    res = requests.post(url=url, data={'img': img_b64})
    res = res.json()
    text = res['data']['raw_out']
    text_simple = []
    for one in text:
        one_simple = []
        one_simple.append(one[1])
        one_simple.append(one[2])
        print(one)
        text_simple.append(one_simple)
    print(text_simple)
    
    img1_file = {
        'file': open('data/test7.jpg', 'rb')
    }
    res = requests.post(url=url, data={'compress': 0}, files=file)
    res = res.json()
    text = res['data']['raw_out']
    print(text)
    text_simple = []
    for one in text:
        one_simple = []
        one_simple.append(one[1])
        one_simple.append(one[2])
        print(one)
        text_simple.append(one_simple)
    print(text_simple)
    '''