import urllib.request
import urllib
import binascii
import hmac
import hashlib
from collections import OrderedDict
import time
import base64
#基本配置
base_url='https://cvm.api.qcloud.com/v2/index.php'
Secretid=''
SecretKey=''



#腾讯云字符串排序加工
def _url_(params):
    params_data=''
    items = OrderedDict(sorted(params.items(), key=lambda t: t[0]))
    for key,value in items.items():
        params_data=params_data+str(key)+'='+str(value)+'&'
    print("字符串排序完成")
    return params_data[:-1]
#签名算法1
def _verfy_ac(SecretKey, params):
    items=OrderedDict(sorted(params.items(), key=lambda t: t[0]))
    params_data = "GETcvm.api.qcloud.com/v2/index.php?"+"";
    for key,value in items.items():
        params_data = params_data + str(key)+"=" + str(value)+'&'
    params_data = params_data[:-1]
    print(params_data.encode())
    hashed = hmac.new(SecretKey.encode(), params_data.encode(), hashlib.sha256)#sha256加密
    aa=binascii.b2a_base64(hashed.digest())[:-1].decode()#进行base64转换
    bb=urllib.request.quote(aa)#转换为url编码
    return bb
def _url_(params):
    params_data=''
    items = OrderedDict(sorted(params.items(), key=lambda t: t[0]))
    for key,value in items.items():
        params_data=params_data+str(key)+'='+str(value)+'&'
    print("字符串排序完成")
    return params_data
def _request_(param):
    url = base_url + '?' + _url_(param) + 'Signature=' + _verfy_ac(SecretKey, param)
    print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print(data)
    print("接口调用完成")
    return data
#查看服务组字符串
#公共请求参数
param={
    'Action' : 'DescribeInstances',
    'Nonce' : 11886,
    'Region' : 'gz',
    'SecretId' : Secretid,
    'SignatureMethod' : 'HmacSHA256',
    'Timestamp' : time.time(),
    # 'instanceIds.0' : 'ins-09dx96dg',
    'limit' : 20,
    'offset' : 0,
}

print(_url_(param))
print(_verfy_ac(SecretKey,param))
print(_request_(param))
