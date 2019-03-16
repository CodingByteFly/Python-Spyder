import urllib.request

URL = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
USER_AGENT = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
req = urllib.request.Request(URL)
req.add_header(USER_AGENT[0], USER_AGENT[1])
data = urllib.request.urlopen(req).read ()
print(data)
