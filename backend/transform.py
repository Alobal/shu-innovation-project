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
        position=data['position']
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
def trans_newHouse(jsonText):
    if isinstance(jsonText,str):
        jsonText=json.loads(jsonText)
    fintotal = {}
    fintotal['name'] = jsonText['name']
    fintotal['city'] = jsonText['city']
    fintotal['type'] = jsonText['type']
    fintotal['pages'] = jsonText['pages']
    dataList = []
    for data in jsonText['data']:
        title = data['title']
        houseType=data['houseType']
        state=data['state']
        position =data['position']
        tags=data['tags']
        unitPrice=data['unitPrice']
        totalPrice=data['totalPrice']
        dict={
            'title':title,
            'houseType':houseType,
            'state':state,
            'position':position,
            'tags':tags,
            'unitPrice':unitPrice,
            'totalPrice':totalPrice
        }
        dataList.append(dict)
    fintotal['data']=dataList
    jsonText=json.dumps(fintotal,ensure_ascii=False)
    return jsonText
def trans_seconde_house(jsonText):
    if isinstance(jsonText,str):
        jsonText=json.loads(jsonText)
    fintotal = {}
    fintotal['name'] = jsonText['name']
    fintotal['city'] = jsonText['city']
    fintotal['type'] = jsonText['type']
    fintotal['pages'] = jsonText['pages']
    dataList = []
    for data in jsonText['data']:
        title = data['title']
        houseType=data['houseType']
        floor=data['floor']
        position=data['position']
        area=data['area']
        direction=data['direction']
        buildTime=data['buildTime']
        viewNum=data['viewNum']
        time=data['time']
        tags=data['tags']
        unitPrice=data['unitPrice']
        totalPrice=data['totalPrice']
        dict={
            'title':title,
            'houseType':houseType,
            'floor':floor,
            'position':position,
            'area':area,
            'direction':direction,
            'buildTime':buildTime,
            'viewNum':viewNum,
            'time':time,
            'tags':tags,
            'unitPrice':unitPrice,
            'totalPrice':totalPrice
        }
        dataList.append(dict)
    fintotal['data']=dataList
    jsonText=json.dumps(fintotal,ensure_ascii=False)
    return jsonText
def trans_rent_house(jsonText):
    if isinstance(jsonText,str):
        jsonText=json.loads(jsonText)
    fintotal = {}
    fintotal['name'] = jsonText['name']
    fintotal['city'] = jsonText['city']
    fintotal['type'] = jsonText['type']
    fintotal['pages'] = jsonText['pages']
    dataList = []
    for data in jsonText['data']:
        title = data['title']
        rentType=data['rentType']
        position=data['position']
        direction=data['direction']
        area=data['area']
        tags=data['tags']
        price=data['price']
        dict={
            'title':title,
            'rentType':rentType,
            'position':position,
            'direction':direction,
            'area':area,
            'tags':tags,
            'price':price
        }
        dataList.append(dict)
    fintotal['data']=dataList
    jsonText=json.dumps(fintotal,ensure_ascii=False)
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




