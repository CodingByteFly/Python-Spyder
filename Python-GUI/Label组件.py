from tkinter import *
import os

root = Tk()
# 创建一个文本Lable对象
root.title("Label组件")
textLable = Label(root, text='hello world!')
textLable.pack(side=LEFT)
# 用PhotoImage实例化一个图片对象（支持gif对象）
photo = PhotoImage(file='../PySpyder/img.jpg')
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()

