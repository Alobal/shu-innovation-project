from includes import *
def trans_house(jsonText):
    if isinstance(jsonText,str):
        jsonText=json.loads(jsonText)
    fintotal={}
    fintotal['name']=jsonText['name']
    fintotal['city']=jsonText['city']
    fintotal['type']=jsonText['type']
    fintotal['pages']=jsonText['pages']
    dataList=[]
    for data in jsonText['data']:
        title=data['title']
        position=''
        if 'position' in data:
            position=data['position']
        elif 'region' in data:
            position=data['region']+'/'+data['town']+'/'+data['detailAddress']
        else:
            position=data['regionOrCircum']+'/'+data['townOrPos']+'/'+data['detailAddress']
        price=''
        if 'price' in data:
            price=data['price']
        elif 'unitPrice' in data:
            price=data['unitPrice']
        dict={
            'title':title,
            'position':position,
            'price':price
        }
        dataList.append(dict)
    fintotal['data']=dataList
    jsonText = json.dumps(fintotal, ensure_ascii=False)
    return jsonText
def trans_job(jsonText):
    if isinstance(jsonText,str):
        jsonText=json.loads(jsonText)
    fintotal={}
    fintotal['name']=jsonText['name']
    fintotal['city']=jsonText['city']
    fintotal['job']=jsonText['job']
    fintotal['pages']=jsonText['pages']
    dataList=[]
    for data in jsonText['data']:
        dict={
            'jobName':data['jobName'],
            'company':data['companyName'],
            'position':data['position'],
            'salary':data['salary']
        }
        dataList.append(dict)
    fintotal['data']=dataList
    jsonText = json.dumps(fintotal, ensure_ascii=False)
    return jsonText




