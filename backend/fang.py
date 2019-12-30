from includes import *
import settings
import saving
import transform
def safeGet(i,list):
    if i <len(list):
        return list[i]
    return ""
def getCityDict():
    response=requests.get('https://bj.5i5j.com/',headers=settings.fangHeader)
    html=pq(response.text)
    items=html('body > div.top-bar-box.new-Menu > div > div.top-city-menu.clear > ul > li').items()
    dict={}
    for item in items:
        citys=item('p').items()
        for city in citys:
            dict[city('a').text()]=city('a').attr('href')
    return dict
def get_details1(html,url):
    allItems=html('body > div.pListBox.mar > div.lfBox.lf > div.list-con-box > ul>li').items()
    totalList=[]
    for item in allItems:
        link=item('div.listCon > h3 > a').attr('href')
        if link!=None:
            link=url[:-1]+item('div.listCon > h3 > a').attr('href')
            title=item('div.listCon > h3 > a').text()
            info=item('div.listCon > div.listX > p:nth-child(1)').text().split('·')
            houseType=safeGet(0,info)
            area=safeGet(1,info)
            direction=safeGet(2,info)
            floor=safeGet(3,info)
            buildTime=safeGet(5,info)
            position=item('div.listCon > div.listX > p:nth-child(2)').text()
            info=item('div.listCon > div.listX > p:nth-child(3)').text().split('·')
            viewNum=safeGet(0,info)
            time=safeGet(2,info)
            tags=item('div.listCon > div.listTag').text()
            totalPrice=item('div.listCon > div.listX > div > p.redC').text()
            unitPrice=item('div.listCon > div.listX > div > p:nth-child(2)').text()
            dict={
                'link':link,
                'title':title,
                'houseType':houseType,
                'area':area,
                'direction':direction,
                'floor':floor,
                'buildTime':buildTime,
                'position':position,
                'viewNum':viewNum,
                'time':time,
                'tags':tags,
                'totalPrice':totalPrice,
                'unitPrice':unitPrice
            }
            totalList.append(dict)
    return totalList
def get_details2(html,url):
    allItems=html('body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li').items()
    totalList=[]
    for item in allItems:
        link=item('div.listCon > h3 > a').attr('href')
        if link!=None:
            link=url[:-1]+link
            title=item('div.listCon > h3 > a').text()
            info=item('div.listCon > div.listX > p:nth-child(1)').text().split('·')
            roomType=safeGet(0,info)
            area=safeGet(1,info)
            direction=safeGet(2,info)
            position=item('div.listCon > div.listX > p:nth-child(2)').text()
            time=item('div.listCon > div.listX > p:nth-child(3)').text().split('·')[2]
            price=item('div.listCon > div.listX > div > p.redC').text().strip()
            tags=item('div.listCon > div.listTag').text()
            rentType=item('div.listCon > div.listX > div > p:nth-child(2)').text().replace('出租方式：','')
            dict={
                'link':link,
                'title':title,
                'roomType':roomType,
                'area':area,
                'direction':direction,
                'position':position,
                'time':time,
                'price':price,
                'tags':tags,
                'rentType':rentType
            }
            totalList.append(dict)
    return totalList
def get_page(page,base_url,typeh):
    url=''
    if typeh=='二手房':
        url=base_url+'ershoufang/n'+str(page)+'/'
    else:
        url=base_url+'zufang/n'+str(page)+'/'
    settings.fangHeader['Host']=base_url.replace('https://','').replace('/','')
    response=requests.get(url,headers=settings.fangHeader)
    html=pq(response.text)
    if typeh == '二手房':
        return get_details1(html,base_url)
    else:
        return get_details2(html,base_url)
def get_all(city,typeh):
    if city not in settings.fangCityDict:
        raise Exception('没有找到该城市')
    url=settings.fangCityDict[city]
    totalDict = {}
    if typeh not in ['二手房','租房']:
        raise Exception('没有找到类型')
    totalDict['name']='fang'
    totalDict['city']=city
    totalDict['type'] = typeh
    totalDict['pages']=100
    totalList=[]
    for i in range(1,101):
        lists=get_page(page=i,base_url=url,typeh=typeh)
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    jsonText = json.dumps(totalDict, ensure_ascii=False)
    if typeh=='二手房':
        jsonText=transform.trans_seconde_house(jsonText)
    else:
        jsonText=transform.trans_rent_house(jsonText)
    return jsonText
def run(city,typeh,page):
    if city not in settings.fangCityDict:
        raise Exception('没有找到该城市')
    url=settings.fangCityDict[city]
    if page < 1 or page > 100:
        raise Exception('输入错误或越界，请重新输入！')
    totalDict = {}
    if typeh not in ['二手房','租房']:
        raise Exception('没有找到类型')
    totalDict['name']='fang'
    totalDict['city']=city
    totalDict['type'] = typeh
    totalDict['pages']=100
    totalDict['data']=get_page(page=page,base_url=url,typeh=typeh)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    if typeh=='二手房':
        jsonText=transform.trans_seconde_house(jsonText)
    else:
        jsonText=transform.trans_rent_house(jsonText)
    return jsonText
