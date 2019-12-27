#保存文件相应模块
import json
import csv
import os
def saveFile(path,jsonText):
    if not os.path.exists(path):
        # 创建文件
        os.mkdir(path)
    if isinstance(jsonText, str):
       jsonText=json.loads(jsonText)
    name=jsonText['name']
    city=jsonText['city']
    last=''
    if 'type' in jsonText:
        last=jsonText['type']
    elif 'job' in jsonText:
        last=jsonText['job']
    data=jsonText['data']
    fieldnames=[]
    for k in data[0]:
        fieldnames.append(k)
    os.chdir(path)
    if not os.path.exists(name):
        # 创建文件
        os.mkdir(name)
    os.chdir(name)
    file = open(city+'-'+last+'.csv', 'w', encoding='utf-8', newline='')
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for dict in data:
        writer.writerow(dict)