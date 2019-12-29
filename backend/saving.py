#保存文件相应模块
import json
import csv
import os
def saveFile(path,jsonText):
    if isinstance(jsonText, str):
       jsonText=json.loads(jsonText)
    name=jsonText['name']
    finStr=''
    if 'city' in jsonText:
        finStr+=jsonText['city']
    if 'type' in jsonText:
        finStr+=' '+jsonText['type']
    elif 'job' in jsonText:
        finStr+=' '+jsonText['job']
    elif 'keyword' in jsonText:
        finStr+=jsonText['keyword']
    data=jsonText['data']
    fieldnames=[]
    for k in data[0]:
        fieldnames.append(k)
    #os.chdir(path)
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(path+'/'+name):
        # 创建文件
        os.mkdir(path+'/'+name)
    #os.chdir(name)
    file = open(path+'/'+name+'/'+finStr+'.csv', 'w', encoding='utf-8', newline='')
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for dict in data:
        writer.writerow(dict)
