#coding:utf-8
from PIL import Image
import argparse
import os

def f():

    ls= os.listdir("testDigits1")
    for i in ls:
        c_path = os.path.join("testDigits1", i)
        os.remove(c_path)

    # files = os.listdir("testDigits1")  # 列出目录下的文件
    # for file in files:
    #     if(file!= '.idea'):
    #         os.remove(file)  # 删除文件
    #         print(file + " deleted")

    ascii_char = ['1', '0']

    # 将256灰度映射到2个字符上
    def get_char(r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1) / length
        return ascii_char[int(gray / unit)]


    lis = os.listdir('testpicture')  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lis)):
        WIDTH = 32
        HEIGHT = 32
        path = os.path.join("testpicture", lis[i])
        path = path.split("\\")[1]
        IMG = 'testpicture/' + path
        num=path.split('.')[0]
        OUTPUT = 'testDigits1/1_' + str(num) + '.txt'

        rgb_im = Image.open(IMG)#打开图片
        im = rgb_im.convert('RGB')

        #使用resize()方法重新设置图片大小，其中第一个参数应是一个尺寸元组
        #而第二个参数resample有四个选项，分别是Image.NEAREST、Image.BILINEAR、
        #Image.BICUBIC、Image.LANCZOS，默认是第一个，第四个质量最高
        im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
        txt = ""

        for i in range(HEIGHT):
                for j in range(WIDTH):
                    txt += get_char(*im.getpixel((j,i)))
                txt += '\n'
        #这段代码是使用getpixel()方法获取某坐标像素点的RGBA值，再通过设置好的对应关系使图片被转换成字符画
        #PNG是一种使用RGBA的图像格式，其中A是指alpha即色彩空间
        #然后使用get_char函数将这个值转换成字符，换行时加上换行符
        #其中getpixel()方法会返回四个元素的元组，
        #而get_char(im.getpixel((j, i )))使用了*则会把返回的元组元素依次赋给get_char()函数的四个参数


        #字符画输出到文件
        if OUTPUT:
            with open(OUTPUT,'w') as f:
                f.write(txt)
        else:
            with open("output.txt",'w') as f:
                f.write(txt)


    lis = os.listdir('testpicture2')  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lis)):
        WIDTH = 32
        HEIGHT = 32
        path = os.path.join("testpicture2", lis[i])
        path = path.split("\\")[1]
        IMG = 'testpicture2/' + path
        num=path.split('.')[0]
        OUTPUT = 'testDigits1/10_' + str(num) + '.txt'

        rgb_im = Image.open(IMG)#打开图片
        im = rgb_im.convert('RGB')

        #使用resize()方法重新设置图片大小，其中第一个参数应是一个尺寸元组
        #而第二个参数resample有四个选项，分别是Image.NEAREST、Image.BILINEAR、
        #Image.BICUBIC、Image.LANCZOS，默认是第一个，第四个质量最高
        im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
        txt = ""

        for i in range(HEIGHT):
                for j in range(WIDTH):
                    txt += get_char(*im.getpixel((j,i)))
                txt += '\n'
        #这段代码是使用getpixel()方法获取某坐标像素点的RGBA值，再通过设置好的对应关系使图片被转换成字符画
        #PNG是一种使用RGBA的图像格式，其中A是指alpha即色彩空间
        #然后使用get_char函数将这个值转换成字符，换行时加上换行符
        #其中getpixel()方法会返回四个元素的元组，
        #而get_char(im.getpixel((j, i )))使用了*则会把返回的元组元素依次赋给get_char()函数的四个参数


        #字符画输出到文件
        if OUTPUT:
            with open(OUTPUT,'w') as f:
                f.write(txt)
        else:
            with open("output.txt",'w') as f:
                f.write(txt)

# f()