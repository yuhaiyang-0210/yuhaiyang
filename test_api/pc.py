#"https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1719748809728&mid=fd90709f4cf9764d63c687e10504f06c&uuid=fd90709f4cf9764d63c687e10504f06c&dfid=4FHtky3ayPMQ2d9fE700Aae2&appid=1014&platid=4&encode_album_audio_id=6n58iraf&token=&userid=0&signature=9cf0f1457573d5484d2aa195d3a97664 "
import requests
import time
#user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
url = 'https://wwwapi.kugou.com/play/songinfo'
data = {
'srcappid': '2919',
'clientver': '20000',
'clienttime': '1719748809728',
'mid': 'fd90709f4cf9764d63c687e10504f06c',
'uuid': 'fd90709f4cf9764d63c687e10504f06c',
'dfid': '4FHtky3ayPMQ2d9fE700Aae2',
'appid': '1014',
'platid': '4',
'encode_album_audio_id': '6n58iraf',
'token':'',
'userid': '0',
'signature': '9cf0f1457573d5484d2aa195d3a97664'
}
reaponse = requests.get(url=url,params=data,headers=headers)
json_date = reaponse.json()
print(json_date)
audio_name = json_date['data']['audio_name']
play_url = json_date['data']['play_url']
print(play_url)
print(audio_name)
#转化成二进制
music_content = requests.get(url=play_url,headers=headers).content
with open('D:\文件下载\music\\' + audio_name + '.mp3' , mode='wb') as f:
    f.write(music_content)

'''
使用歌曲id列表全局搜索查找到榜单链接来为凄凉获取做做准备
'''
#获取列表链接“https://www.kugou.com/yy/html/rank.html。



