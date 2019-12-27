import cv2
import numpy as np


def alpha2white_opencv2(img):
    sp=img.shape
    width=sp[0]
    height=sp[1]
    for yh in range(height):
        for xw in range(width):
            color_d=img[xw,yh]
            if(color_d[3]==0):
                img[xw,yh]=[255,255,255,255]
    return img

# 垂直投影
def vProject(binary):
    h, w= binary.shape
    # 垂直投影
    SumWidth=[]

    # 创建 w 长度都为0的数组
    for i in range(w):
        tempsum=0
        for j in range(h):
            if binary[j,i] != 255:
                tempsum+= 1
        SumWidth.append(tempsum)


    return SumWidth

def scanNum():
    img = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
    alpha2white_opencv2(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cutsimg = []
    for i in range(10):
        cutsimg.append(img[0:28, i * 30:(i + 1) * 30])
    charlist = {9: vProject(cutsimg[0]), 3: vProject(cutsimg[1]), 1: vProject(cutsimg[2]), 0: vProject(cutsimg[3]),
                8: vProject(cutsimg[4]), 6: vProject(cutsimg[5]), 7: vProject(cutsimg[6]), 5: vProject(cutsimg[7]),
                4: vProject(cutsimg[8]), 2: vProject(cutsimg[9])}

    trainimg = cv2.imread('temp.png', cv2.IMREAD_UNCHANGED)
    alpha2white_opencv2(trainimg)
    trainimg = cv2.cvtColor(trainimg, cv2.COLOR_BGR2GRAY)
    cutstrain = []
    for i in range(10):
        cutstrain.append(trainimg[0:28, i * 30:(i + 1) * 30])
    resultList = []
    for i in range(10):
        for j in range(10):
            if (vProject(cutstrain[i]) == charlist[j]):
                resultList.append(j)
    return resultList
