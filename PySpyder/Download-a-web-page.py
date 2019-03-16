import urllib.request

# 将爬取的内容写入文件的方法一：
URL = "https://wapbaike.baidu.com/item/scanf/10773316?fr=aladdin&ms=1&rid=11622657884936857739"
file = urllib.request.urlopen(URL)
print(type(file))
file.info()
file.getcode()
print(file.getcode())
file.geturl()
print(file.geturl())
file = urllib.request.urlopen(URL)
dataline = file.readline()
file = urllib.request.urlopen(URL)
datalines = file.readlines()
file = urllib.request.urlopen(URL)
data = file.read()
print(data)
print(dataline)
print(datalines)
with open('web.html', 'wb') as f:
    f.write(data)

# 将爬取的内容写入文件的方法二：
filename = urllib.request.urlretrieve(URL, 'web2.html')
urllib.request.urlcleanup()
print(filename)
print(type(filename))
