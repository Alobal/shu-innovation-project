from includes import *
import settings
import transform
import ScanNum
def safe_get(i,item):
    if item=="" or len(item)-1<i:
        return ""
    return item[i]
def get_zufang_detail(html):
    allText=html('body > section > div.Z_list > div.Z_list-box > div').items()
    totalList=[]
    tempItem = html('body > section > div.Z_list > div.Z_list-box > div:nth-child(1) > div.info-box > div.price > span:nth-child(3)').attr('style')
    urlStyle = tempItem.replace('background-image: url(', '').replace(')', '').replace('background-position: ', '')
    url = urlStyle.split(';')[0]
    url = 'http:' + url
    response = requests.get(url)
    file = open('temp.png', 'wb')
    file.write(response.content)
    file.close()
    numList=ScanNum.scanNum()
    numDicct={}
    count=0
    for k in numList:
        numDicct[k]=settings.ziruValueList[count]
        count+=1
    for item in allText:
        link=item('div.info-box > h5 > a').attr('href')
        if link!=None:
            link='http:'+item('div.info-box > h5 > a').attr('href')
            info=item('div.info-box > h5 > a').text().split('·')
            rentType=safe_get(0,info)
            title=safe_get(0,safe_get(1,info).split('-'))
            roomDirection=safe_get(1,safe_get(1,info).split('-'))
            des=item('div.info-box > div.desc > div:nth-child(1)').text().split('|')
            area=safe_get(0,des)
            floor=safe_get(1,des)
            detectionAndTime=item('div.info-box > div.tips.has-more.air-low').text()
            detection='0'
            emptyTime='0天'
            if detectionAndTime!='':
                detection=detectionAndTime.split(',')[0].replace('空气质量已检测','1')
                emptyTime=detectionAndTime.split(',')[1].replace('已空置','')
            priceItems=item('div.info-box > div.price > span').items()
            price=''
            for it in priceItems:
                style=it.attr('style')
                if style!=None:
                    pos=re.compile('background-position: (.*?)px').findall(style)[0]
                    pos+='px'
                    for k in numDicct:
                        if pos==numDicct[k]:
                            price+=str(k)
                            break
            price+='元/月'
            dict={
                'link':link,
                'title':title,
                'rentType':rentType,
                'direction':roomDirection,
                'area':area,
                'floor':floor,
                'position':item('div.info-box > div.desc > div.location').text(),
                'tags':item('div.info-box > div.tag').text(),
                'detection':detection,
                'emptyTime':emptyTime,
                'price':price
            }
            totalList.append(dict)
    return totalList
def get_zufang(page,base_url):
    url=base_url+'z/p'+str(page)+'/'
    response=requests.get(url,headers=settings.ziruHeader)
    if response.url==url:
        html = pq(response.text)
        return get_zufang_detail(html)
    else:
        get_zufang(page,base_url)
def get_all(city):
    if city not in settings.zirucityDict:
        raise Exception('没有找到该城市')
    url=settings.zirucityDict[city]
    totalDict = {}
    totalDict['name']='ziru'
    totalDict['city']=city
    totalDict['type'] = '租房'
    totalDict['pages']=100
    totalList=[]
    for i in range(1,101):
        lists=get_zufang(page=i,base_url=url)
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    jsonText = json.dumps(totalDict, ensure_ascii=False)
    return jsonText
def run(city,page):
    if city not in settings.zirucityDict:
        raise Exception('没有找到该城市！')
    if page < 1 or page > 100:
        raise Exception('page小于1或越界')
    url = settings.zirucityDict[city]
    settings.ziruHeader['Host'] = url.replace('http://', '').replace('/', '')
    settings.ziruHeader['Referer'] = url + 'z/'
    totalDict={}
    totalDict['name']='ziru'
    totalDict['city']=city
    totalDict['type']='租房'
    totalDict['pages']=100
    totalDict['data']=get_zufang(page=page, base_url=url)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    jsonText = transform.trans_rent_house(jsonText)
    return jsonText
