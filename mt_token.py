import base64
import zlib
import time
import requests
from urllib import parse


def decode_token(s):
    a = base64.b64decode(s)
    print(a)
    result = zlib.decompress(a)
    return result


def encode_sign(sign):
    result = base64.b64encode(zlib.compress(sign))
    return str(result, 'utf-8')


def encode_token():
    d = {}
    d["rId"] = 100900
    d["ver"] = "1.0.6"
    d["ts"] = int(time.time() * 1000)
    # d["ts"] = 1582704455270
    d["cts"] = int(time.time() * 1000 + 75)
    # d["cts"] = 1582704455345
    d["brVD"] = [822, 1151]
    d["brR"] = [[1920, 1080], [1920, 1080], 24, 24]
    d["bI"] = ["https://gz.meituan.com/meishi/", "https://gz.meituan.com/"]
    d["mT"] = []
    d["kT"] = []
    d["aT"] = []
    d["tT"] = []
    d["aM"] = ""
    sign = b'"areaId=0&cateId=0&cityName=\xe5\xb9\xbf\xe5\xb7\x9e&dinnerCountAttrId=&optimusCode=10&originUrl=https://gz.meituan.com/meishi/&page=1&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=27feb019adbd4186a43e.1582704408.1.0.0"'
    d["sign"] = encode_sign(sign)
    return d


def get_token():
    d = encode_token()
    data = str(d).replace("'", '"').replace(' ', '').encode()
    # 进行 url 编码
    token = parse.quote(encode_sign(data))
    return token


if __name__ == '__main__':
    token = get_token()
    url = 'https://gz.meituan.com/meishi/api/poi/getPoiList?cityName=%E5%B9%BF%E5%B7%9E&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=&uuid=27feb019adbd4186a43e.1582704408.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fgz.meituan.com%2Fmeishi%2F&riskLevel=1&optimusCode=10&_token=' + token
    headers = {
        # 'Cookie': '_lxsdk_cuid=17061bdb99fc8-02d1bc12d68259-3c604504-1fa400-17061bdb99fc8; _hc.v=4c9bb6b2-be41-8c38-5b85-55b5e525029d.1582187854; iuuid=F27BCC814DA3D3DE87F8AF31680A50D3481F769B5E586743E973F4D665CA8F1A; cityname=%E5%B9%BF%E5%B7%9E; _lxsdk=F27BCC814DA3D3DE87F8AF31680A50D3481F769B5E586743E973F4D665CA8F1A; webp=1; latlng=23.130873,113.314218,1582596340177; i_extend=C_b1Gimthomepagecategory11H__a; PHPSESSID=glju3e7tram9mm14oi6gl8pdq2; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1582704399; Hm_lpvt_f66b37722f586a240d4621318a5a6ebe=1582704399; __utma=211559370.1822528469.1582704399.1582704399.1582704399.1; __utmc=211559370; __utmz=211559370.1582704399.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; uuid=27feb019adbd4186a43e.1582704408.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ci=20; __mta=209023277.1582187792859.1582187792859.1582704411604.2; client-id=50dea765-bdec-4ac7-b5b4-5f92afa9f54c; _lxsdk_s=17080d79353-d36-553-5%7C%7C4',
        'Host': 'gz.meituan.com',
        'Referer': 'https://gz.meituan.com/meishi/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    print(r.text)
