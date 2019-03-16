import urllib.request

URL = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
USER_AGENT = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [USER_AGENT]
data = opener.open(URL).read()
print(data)