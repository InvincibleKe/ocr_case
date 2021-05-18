# coding=UTF-8
import requests
import image_rotation
import cv2
import base64
from test import img_to_base64
import numpy as np
import recognition_zkktzs
def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
def getKeyData(text):
    index = 0
    people_num = 0
    key_data = {'caseNo':'', 'infoList':[]}
    text_del = '案件号:'
    while(len(text) > index):
        people = {'index':'', 'name':'', 'idNo':'', 'accountNumber':'', 'bankName':''}
        if '案件号' in text[index][1] and '序号' in text[index+1][1]:
            key_data['caseNo'] = text[index][1].replace(text_del, '', 1)
        if index > 1 and '开户行' in text[index-1][1] and len(text) > index+4:
            people['index'] = text[index][1]
            people['name'] = text[index+1][1]
            people['idNo'] = text[index+2][1]
            people['accountNumber'] = text[index+3][1]
            if is_contain_chinese(text[index+4][1]) and '签章' not in text[index+4][1]:
                people['bankName'] = text[index+4][1]
                if is_contain_chinese(text[index+5][1]) and '签章' not in text[index+5][1]:
                    people['bankName'] += text[index + 5][1]
                    if is_contain_chinese(text[index+6][1]) and '签章' not in text[index+6][1]:
                        people['bankName'] += text[index + 6][1]
                        index += 6
                    else:
                        index += 5
                else:
                    index += 4
            else:
                index += 3
            key_data['infoList'].append(people)
            people_num += 1
        if people_num > 0 and len(text) > index+4 and is_number(text[index][1]):
            people['index'] = text[index][1]
            people['name'] = text[index + 1][1]
            people['idNo'] = text[index + 2][1]
            people['accountNumber'] = text[index + 3][1]
            if is_contain_chinese(text[index + 4][1]) and '签章' not in text[index + 4][1]:
                people['bankName'] = text[index + 4][1]
                if is_contain_chinese(text[index + 5][1]) and '签章' not in text[index + 5][1]:
                    people['bankName'] += text[index + 5][1]

                    if is_contain_chinese(text[index + 6][1]) and '签章' not in text[index + 6][1]:
                        people['bankName'] += text[index + 6][1]
                        index += 6
                    else:
                        index += 5
                else:
                    index += 4
            else:
                index += 3
            key_data['infoList'].append(people)
            people_num += 1
        index += 1
    return key_data
def imgFile_recognition(img_b64, compress=1200):
    url = recognition_zkktzs.read_trurl()
    angle = 0
    while (True):
        res = requests.post(url=url, data={'img': img_b64, 'compress': compress})
        res = res.json()
        text = res['data']['raw_out']
        text = recognition_zkktzs.delete_blank(text)
        if text[0][2] >= 0.8 and '新增第三方账户信息单' in text[0][1]:
            break
        angle += 90
        # file.seek(0)
        img_b64 = image_rotation.rotate_file(img_b64, angle)
        retval, buffer = cv2.imencode('.jpg', img_b64)
        img_b64 = base64.b64encode(np.array(buffer))
    key_data = getKeyData(text)
    return key_data

if __name__ == '__main__':
    #file = open('data/.jpg', 'rb')
    img_b64 = img_to_base64('data/test4.jpeg')

    key = imgFile_recognition(img_b64)
    print(key)
    for v, k in key.items():
        print('{v}:{k}'.format(v=v, k=k))
