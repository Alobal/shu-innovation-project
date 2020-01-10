# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts.charts import Scatter
from pyecharts import options as opts

def Str2value(oristr):#将oristr中的数字提取成float返回
    # try:
        pattern=re.compile("\\d+")
        result=pattern.findall(oristr)
        return np.float64(result[0])
    # except:
    #     print(oristr,result,sep=' ')

def Colum2value(oricolum):#将oricolum列中所有string转为包含的数字
    try:
        for i in range(0,oricolum.values.size):
            if(oricolum.values[i] is np.nan):
                #空数据近似为上一个
                oricolum.values[i]=oricolum.values[i-1]
                continue
            oricolum.values[i]=Str2value(oricolum.values[i])
        return oricolum
    except:
        print(i,sep=' ')

def Fang_Scatter(filepath,searchType):#在当前路径生成一个散点分布图render.html,散点图纵坐标为price/unitPrice,横坐标为想要查询的字段searchType,需要传入数据路径和查询字段
    oridata=pd.read_csv(filepath)
    if(searchType not in oridata.columns):
        print('不存在该字段! No Such attribution!')
        return
    
    #字段的单位
    unit={}
    #非数值数据列表
    x_1=[]
    x_1.append('direction')
    x_1.append('rentType')
    x_1.append('houseType')
    unit['direction']='方向'
    unit['rentType']='整租'
    unit['houseType']='户型'

    
    #不干净的数值型数据
    x_2=[]
    #租房和二手房有不同的价格字段
    if('price' in oridata.columns):
        x_2.append('price')
    else:
        x_2.append('unitPrice')

    x_2.append('area')
    x_2.append('viewNum')
    x_2.append('floor')
    x_2.append('buildTime')
    unit['area']='平米'
    unit['viewNum']='人'
    unit['floor']='层'
    unit['price']='元/月'
    unit['unitPrice']='元/m2'
    unit['buildTime']='年'

    for i in x_2:
        if(i in oridata.columns):
            oridata[i]=Colum2value(oridata[i])

    #xflag标记是否找到查询字段,=1说明在x_1里,为非数值字段,=2在x_2里
    xflag=0
    #查找searchType
    for i in x_1:
        if i==searchType:
            xflag=1
            break

    if xflag==0:
        for i in x_2:
            if i==searchType:
                xflag=2
                break
    
    if xflag==0:
        print('没有找到该字段! No Such attribution!')
        return
            
    x=oridata[searchType]
    y=oridata[x_2[0]]

# %%
    # pyecharts绘图

    c = (
        Scatter()
        .add_xaxis(x)
        .add_yaxis("price",y,symbol_size=10,label_opts=opts.LabelOpts(is_show=False))
        )
    if xflag==1: #横坐标是类目数据时,改变X轴类型
        c.set_global_opts(
            title_opts=opts.TitleOpts(title=searchType+" with Price"),
            xaxis_opts=opts.AxisOpts(name=searchType+'/'+unit[searchType],type_="category"),
            yaxis_opts=opts.AxisOpts(name=x_2[0]+'/'+unit[x_2[0]]),
            visualmap_opts=opts.VisualMapOpts(max_=60000),
            datazoom_opts=opts.DataZoomOpts(range_start=0),
        )
    else:
        c.set_global_opts(
                title_opts=opts.TitleOpts(title=searchType+" with Price"),
                xaxis_opts=opts.AxisOpts(name=searchType+'/'+unit[searchType]),
                yaxis_opts=opts.AxisOpts(name=x_2[0]+'/'+unit[x_2[0]]),
                visualmap_opts=opts.VisualMapOpts(max_=100000,min_=10000),
                datazoom_opts=opts.DataZoomOpts(range_start=0),

            )
    
    c.render()
# %%示例
# path="C:/Users/邹世奇/Downloads/shu-innovation-project-master/data/fang/上海 二手房.csv"
# Fang_Scatter(path,'viewNum')

# %%
