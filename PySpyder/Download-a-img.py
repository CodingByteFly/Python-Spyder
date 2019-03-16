import urllib.request

url = "https://www.baidu.com/img/bd_logo1.png"
response = urllib.request.urlopen(url)
img = response.read()
with open("img.jpg", "wb") as f:
    f.write(img)
