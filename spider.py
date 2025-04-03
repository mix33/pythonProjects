# coding=utf-8
import re
import urllib2
import urllib

url = 'http://www.qiushibaike.com/pic/'
hander = {
        "Referer": "http://www.qiushibaike.com/pic/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
        }

def ppk(url):
    req = urllib2.Request(url,None,hander)
    opens = urllib2.urlopen(req)
    # print opens
    content = opens.read()
    # print content
    img = re.findall(r'<img src="(http.*?://.*?)"', content, re.S)
    # print img
    for imgurl in img:
        i = imgurl.rsplit('?',1)[0]
        try:
            name = i.rsplit('/',1)[1]
        # print name
            urllib.urlretrieve(i, name)
            print name,'is  done'
        except:
            pass
ppk('http://www.qiushibaike.com/pic/')
