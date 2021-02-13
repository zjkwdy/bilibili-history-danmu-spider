
# bilibili-history-danmu-spider

* * * 

用来爬历史弹幕用的，可以整全弹幕什么的。目前支持爬取所有历史弹幕，输出标准xml格式弹幕 
使用的是B站protobuf历史弹幕接口，原因就是b站xml格式历史弹幕接口爆炸了，可以用但是返回弹幕已被关闭的信息。

## 爬av114514(默认) 

食用教程：先把浏览器Cookie中的SESSDATA，例如
`b7723dd1%1C45141919810%2C6b33f*21`
在代码找到`SESSDATA=['']`
把SESSDATA填进去保存，多个SESSDATA直接塞进列表里，会随机使用。
其他设置：
HTTP代理（如果有）：
在代码找到`https_proxy = []`
在`if __name__ == '__main:'`下找到： 

```
# 历史弹幕开始年
start_year = 2018
# 历史弹幕结束年
end_year = 2021
# Cookie中的SESSDATA,可为多个
SESSDATA = ['d0ae0de7%2C1628585724%2Ccc213*21']
# 延迟，防屏蔽,单位：秒
daily = 1
``` 

以下爬取是2021-01-01到2021-01-10 av114514全弹幕效果
![效果](https://s3.ax1x.com/2021/02/11/yBLTn1.png)  


## 想要爬别的视频弹幕？ 

***把代码中cid改成对应视频的cid即可。***

