import os


def copy(path1, path2):  # 将path1复制到path2
    fp1 = open(path1, 'rb')
    fp2 = open(path2, 'wb')
    for j in fp1:
        fp2.write(j)
    fp1.close()
    fp2.close()


def copy_enhance(path1, path2):
    fp1 = open(path1, 'rb')
    img = fp1.read()
    with open(path2, 'wb') as f:
        f.write(img)


source = r"C:\Users\LOVEL\AppData\Local\Packages" \
         r"\Microsoft.Windows.ContentDeliveryMana" \
         r"ger_cw5n1h2txyewy\LocalState\Assets" 
result = r"D:\LOVEL\Pictures\Win10-pictures-extracted-by-Python"
sy = os.listdir(source)  # listdir(source)以列表形式返回source文件目录下的所有文件名
for each in enumerate(sy):  # enumerate(sy)生成由二元组构成的一个迭代对象，每个二元组由可迭代参数的索引号及其对应的元素组成的
    print(each)
print(type(enumerate(sy)))
c = 0.0
for i in sy:
    d = str(c)
    copy_enhance(source + '\\' + i, result + '\\' + d + '.jpg')
    c += 1
os.system("pause")



