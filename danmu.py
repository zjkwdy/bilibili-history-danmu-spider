import json
import random
import time
import xml.etree.ElementTree as ET

import requests

import bilidm_pb2


# 返回开始到结束年中的所有月数组，例如['2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12', '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09', '2012-10', '2012-11', '2012-12']
def list_months(start, end):
    result = []
    for year in range(start, end+1):
        for month in range(1, 13):
            result.append(str(year)
                          + '-' +
                          str(month).rjust(2, '0')
                          )
    return result


# 获取某年某月有弹幕的天，返回天数组。
def get_danmu_months(cid, month, SESSDATA, proxy):
    api_url = f'http://api.bilibili.com/x/v2/dm/history/index?type=1&oid={str(cid)}&month={month}'
    req_headers = {
        'User-Agent': random_user_agent(),
        'Cookie': 'SESSDATA='+random_SESSDATA(SESSDATA)+';'
    }
    # 如果有代理就随机一个用
    if len(proxy) >= 1:
        req = requests.get(url=api_url, headers=req_headers,
                           proxy={'https': random_proxy(proxy)})
    else:
        req = requests.get(url=api_url, headers=req_headers)
    return req.json()


# 获取所有有弹幕的天
def get_danmu_dates(cid, months, SESSDATA, daily, proxy):
    result = []
    for month in months:
        dates = get_danmu_months(cid, month, SESSDATA, proxy)
        if dates['code'] == 0:
            if dates['data'] != None:
                for date in dates['data']:
                    result.append(date)
                    print(date, dates['message'])
            time.sleep(daily)
        else:
            print(f'ERROR:{dates}')
    return result


# 获取某天的历史弹幕。
def get_day_danmu(cid, date, SESSDATA, proxy):
    api_url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={cid}&date={date}'
    req_headers = {
        'User-Agent': random_user_agent(),
        'Cookie': 'SESSDATA='+random_SESSDATA(SESSDATA)+';',
        'Referer': 'https://www.bilibili.com/',
        'Origin': 'https://www.bilibili.com'
    }

    # 下载protobuf格式弹幕，有代理就整一个！
    if len(proxy) >= 1:
        data = requests.get(url=api_url, headers=req_headers, proxy={
                            'https': random_proxy(proxy)})
    else:
        data = requests.get(api_url, headers=req_headers)

    try:
        target = bilidm_pb2.DmSegMobileReply()
        target.ParseFromString(data.content)
        print(f'{date}处理完成.')
        return target.elems
    except:
        print(f'处理弹幕出错:{date}:{data.json()}')


# 随机UA标
def random_user_agent():

    # 复制的，不知道还有用没
    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; "
        "SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; "
        "SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; "
        "Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; "
        "Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; "
        ".NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; "
        "Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; "
        ".NET CLR 3.5.30729; .NET CLR 3.0.30729; "
        ".NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; "
        "Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; "
        "InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) "
        "AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) "
        "Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ "
        "(KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; "
        "rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) "
        "Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) "
        "Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) "
        "Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 "
        "(KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
        "AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) "
        "Presto/2.9.168 Version/11.52",
    ]

    return random.choice(USER_AGENTS)


# 随机SESSDATA，多个SESSDATA时很有用
def random_SESSDATA(SESSDATA):
    return random.choice(SESSDATA)

# 随机使用代理


def random_proxy(proxy):
    return random.choice(proxy)


if __name__ == '__main__':
    # av114514 1P的cid 190524
    cid = 190524
    # 历史弹幕开始年
    start_year = 2018
    # 历史弹幕结束年
    end_year = 2021
    # Cookie中的SESSDATA,可为多个
    SESSDATA = ['']
    # 延迟，防屏蔽,单位：秒
    daily = 1
    # http代理列表。可以为空。
    https_proxy = []

    months = list_months(start_year, end_year)
    print('开始获取历史弹幕日期...时间较长耐心等待')
    all_danmu_dates = get_danmu_dates(
        cid, months, SESSDATA, daily, https_proxy)
    print('获取所有历史弹幕日期完成，开始扒取历史弹幕')

    # 初始化弹幕列表
    danmu_list = []

    # 下载所有历史弹幕
    for date in all_danmu_dates:
        history_danmu = get_day_danmu(cid, date, SESSDATA, https_proxy)
        time.sleep(daily)
        danmu_list.append(history_danmu)

    '''    
        
        #弹幕操作id列表初始化
        danmu_id_list=[]
        #弹幕文字列表初始化
        danmu_content_list=[]
        #弹幕出现时间列表初始化
        danmu_progress_list=[]
        #弹幕模式列表初始化
        danmu_mode_list=[]
        #字号列表初始化
        danmu_font_size_list=[]
        #弹幕颜色列表初始化
        danmu_color_list=[]
        #弹幕发送者列表初始化
        danmu_author_list=[]
        #弹幕发送时间列表初始化
        danmu_create_time_list=[]
        #弹幕权重列表初始化，拿来智能屏蔽的
        danmu_weight_list=[]
        #action初始化，母鸡干啥用的,但还是存起来好
        danmu_action_list=[]
        #弹幕池列表初始化
        danmu_pool_list=[]
    '''
    # 把一大堆弹幕数据放进对应列表，输出xml
    # xml根对象i
    print('开始输出xml格式弹幕文件...')
    danmu_xml_root = ET.Element('i')
    ET.SubElement(danmu_xml_root, 'chatserver').text = 'chat.bilibili.com'
    ET.SubElement(danmu_xml_root, 'chatid').text = f'{cid}'
    ET.SubElement(danmu_xml_root, 'mission').text = '0'
    ET.SubElement(danmu_xml_root, 'maxlimit').text = '100000000000'
    ET.SubElement(danmu_xml_root, 'state').text = '0'
    ET.SubElement(danmu_xml_root, 'real_name').text = '0'
    ET.SubElement(danmu_xml_root, 'source').text = 'k-v'
    for day_danmu in danmu_list:
        for danmu in day_danmu:
            # fw作者脑抽写的代码，写完发现没啥用，留着吧
            '''
            danmu_id_list.append(danmu.id)
            danmu_progress_list.append(danmu.progress)
            danmu_mode_list.append(danmu.mode)
            danmu_font_size_list.append(danmu.fontsize)
            danmu_color_list.append(danmu.color)
            danmu_author_list.append(danmu.midhash)
            danmu_content_list.append(danmu.content)
            danmu_create_time_list.append(danmu.ctime)
            danmu_weight_list.append(danmu.weight)
            danmu_action_list.append(danmu.action)
            danmu_pool_list.append(danmu.pool)
            '''
            # 每条弹幕
            content = danmu.content
            ET.SubElement(danmu_xml_root, 'd', {
                          'p': f'{int(danmu.progress)/1000},{danmu.mode},{danmu.fontsize},{danmu.color},{danmu.ctime},{danmu.pool},{danmu.midHash},{danmu.idStr}'}).text = content
            print('输出弹幕', content)

    # 保存弹幕
    try:
        result_danmu_xml = ET.ElementTree(danmu_xml_root)
        result_danmu_xml.write(f'{cid}.xml', 'UTF-8')
    except:
        print('保存xml弹幕失败。')


# else:
    #print('这是Plan B? (雾)')