import requests
import json


def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    Form_Data = {
        'i': '我爱中国',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1539566557666',
        'sign': '540ff8114214197c197ad80949b144e1',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }

    # 请求表单数据
    respose = requests.post(url, data=Form_Data)
    # 将JSON格式字符串转字典
    content = json.loads(response.text)
    # 打印翻译后的数据
    print(contant['translateResult'][0][0]['tgt'])

    # if __name__== '__main__':
    get_translate_date('我爱数据')

# 这段代码有问题
