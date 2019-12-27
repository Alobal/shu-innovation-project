import settings
from includes import *
#获取到所有的城市以及它的链接
def get_allCity(dict):
    response=requests.get('https://www.lianjia.com/city/')
    html=pq(response.text)
    allCity=html('div.city_province > ul>li').items()
    for item in allCity:
        dict[item.text()]=item('a').attr('href')
def get_details_1(html):
    allText=html('#content > div.leftContent > ul>li').items()
    totalList=[]
    for item in allText:
        houseinfo=item('div.info.clear > div.address > div').text().strip().split('|')
        housetype=houseinfo[0]
        area=houseinfo[1]
        direction=houseinfo[2]
        decoration=houseinfo[3]
        floor=houseinfo[4]
        buildtime=''
        if len(houseinfo)==7:
            buildtime=houseinfo[5]
        floortype=houseinfo[-1]
        tags=item('div.info.clear > div.tag').text()
        dict={
            "link":item('a').attr('href'),
            "title":item('div.info.clear > div.title > a').text(),
            "position":item('div.info.clear > div.flood > div').text().strip(),
            'houseType':housetype,
            'area':area,
            'direction':direction,
            'decoration':decoration,
            'floor':floor,
            'buildTime':buildtime,
            'floorType':floortype,
            "viewNum":item('div.info.clear > div.followInfo').text().split('/')[0].strip(),
            "time":item('div.info.clear > div.followInfo').text().split('/')[1].strip(),
            'tags':tags,
            "totalPrice":item('div.info.clear > div.priceInfo > div.totalPrice').text(),
            "unitPrice":item('div.info.clear > div.priceInfo > div.unitPrice').text()
        }
        totalList.append(dict)
    return totalList
def get_details_2(html):
    allText=html('body > div.resblock-list-container.clearfix > ul.resblock-list-wrapper>li').items()
    totalList=[]
    for item in allText:
        position = item('div > div.resblock-location').text().strip().split('/')
        dict = {
            "link": 'https://sh.fang.lianjia.com'+item('div > div.resblock-name > a').attr('href'),
            "title": item('li > div > div.resblock-name>a').text(),
            'houseType':item('li>div > div.resblock-name > span.resblock-type').text(),
            'state':item('li> div > div.resblock-name > span.sale-status').text(),
            'position':position,
            "houseInfo": item('li> div > a > span').text(),
            "area":item('div > div.resblock-area > span').text(),
            "tags": item('div > div.resblock-tag').text(),
            "totalPrice": item('div > div.resblock-price > div.second').text(),
            "unitPrice": item('div > div.resblock-price > div.main-price').text()
        }
        totalList.append(dict)
    return totalList
def get_details_3(html):
    allText=html('#content > div.content__article > div.content__list > div.content__list--item').items()
    totalList=[]
    for item in allText:
        title=item('div > p.content__list--item--title.twoline > a').text().split()
        rentType=title[0].split('·')[0]
        realTitle=title[0].split('·')[1]
        info=item('div > p.content__list--item--des').text().split('/')
        position=info[0]
        area=info[1]
        direction=info[2]
        roomType=info[3]
        tags=item('div > p.content__list--item--bottom.oneline>i').text()
        dict={
            'link':'https://sh.lianjia.com/'+item('div > p.content__list--item--title.twoline > a').attr('href'),
            'rentType':rentType,
            'title':realTitle,
            'position':position,
            'area':area,
            'direction':direction,
            'roomType':roomType,
            'tags':tags,
            'time':item('div > p.content__list--item--brand.oneline > span.content__list--item--time.oneline').text(),
            'price':item('div > span').text()
        }
        totalList.append(dict)
    return totalList
def get_page(page, base_url,typeh):
    if typeh == '二手房':
        url = base_url + 'ershoufang/pg' + str(page) + '/'
    elif typeh == '新房':
        'https://sh.fang.lianjia.com/loupan/pg3/'
        base_url = base_url.replace('.lianjia.com', '.fang.lianjia.com')
        url = base_url + 'loupan/pg' + str(page) + '/'
    else:
        url = base_url + 'zufang/pg' + str(page) + '/#contentList'
    settings.lianjiaHeader['Referer'] = url
    response = requests.get(url, headers=settings.lianjiaHeader)
    if response.url == url:
        html = pq(response.text)
        if typeh == '二手房':
            return get_details_1(html)
        elif typeh == '新房':
            return get_details_2(html)
        else:
            return get_details_3(html)
    else:
        get_page(page, base_url,typeh)
def get_all(city,typeh):
    if city not in settings.lianjiacityDict:
        raise Exception('没有找到该城市')
    url=settings.lianjiacityDict[city]
    totalDict = {}
    if typeh not in ['二手房','新房','租房']:
        raise Exception('没有找到类型')
    totalDict['name']='lianjia'
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
    return jsonText
def run(city,typeh,page):
    if city not in settings.lianjiacityDict:
        raise Exception('没有找到该城市！')
    if typeh not in ['二手房','新房','租房']:
        raise Exception('没有找到相应类型')
    url = settings.lianjiacityDict[city]
    if page < 1 or page > 100:
        raise Exception('page小于1或越界')
    totalDict={}
    totalDict['name']='lianjia'
    totalDict['city']=city
    totalDict['type']=typeh
    totalDict['pages']=100
    totalDict['data']=get_page(page=page,base_url=url,typeh=typeh)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText