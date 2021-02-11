import requests

#avid='170001'
#不用我说了吧
bvid='BV17x411w7KC'

#浏览器Cookie SESSDATA，一般不用写，但是比如av2(BV1xx411c7mD)没登陆看不了就得写。
SESSDATA = ''

url=f'http://api.bilibili.com/x/web-interface/view?bvid={bvid}'
req_headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
    'Cookie': f'SESSDATA={SESSDATA};'
}

req=requests.get(url,headers=req_headers)


for video in req.json()['data']['pages']:
    print('======================================================================')
    print('cid for P'+str(video['page'])+' '+video['part']+' is '+str(video['cid']))