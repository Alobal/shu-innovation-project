from PIL import Image
import numpy as np

def alphabg2white_PIL(img):
    img = img.convert('RGBA')
    sp = img.size
    width = sp[0]
    height = sp[1]
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img.getpixel(dot)
            if (color_d[3] == 0):
                color_d = (255, 255, 255, 255)
                img.putpixel(dot, color_d)
    return img


def read_image(imageName):
    img = Image.open(imageName)
    img=alphabg2white_PIL(img)
    data = np.array(img)
    return data


def get_num(n):
    l_num = []
    m = 0
    x = n
    while True:
        if m < 9:
            x0,x1, = np.split(x, [30],axis = 1)
            l_num.append(x0)
            x = x1
            m+=1
            continue
        else:
            l_num.append(x)
            break
    return l_num

def get_0_9():
    l_num = get_num(read_image('./test.png'))
    x9,x3,x1,x0,x8,x6,x7,x5,x4,x2 = l_num
    list_num = [x0,x1,x2,x3,x4,x5,x6,x7,x8,x9]
    return list_num

def scanNum():
    l = []
    list_num = get_0_9()
    l_num_test = get_num(read_image('./temp.png'))
    for i in range(0,10):
        for w in range(0,10):
            if (l_num_test[i] == list_num[w]).all():
                l.append(w)
                break
    return l