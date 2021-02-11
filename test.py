import bilidm_pb2
import requests

CID = 190524
#SEG = 1
DATE = '2020-12-01'
SESSDATA=input()
url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={CID}&date={DATE}'
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
    'Cookie': f'SESSDATA={SESSDATA};'
}
data = requests.get(url,headers=req_headers)
target = bilidm_pb2.DmSegMobileReply()
target.ParseFromString(data.content)

print(target.elems[0])
print(target.elems[0].content)
