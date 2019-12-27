from includes import *
import settings
def safe_get(i,item):
    if item=="" or len(item)-1<i:
        return ""
    return item[i]
def get_city():
    response=requests.get('https://www.ke.com/city/')
    html=pq(response.text)
    allPro=html('body > div.city_selection_section > div.city_recommend > div.city-item > div.city_list_section > ul > li').items()
    dict={}
    for pro in allPro:
        citys=pro('div.city_list > div > ul > li').items()
        for city in citys:
            dict[city('a').text()]='https:'+city('a').attr('href')
    return dict
#获得二手房信息,使用正则表达式
def get_details1(html):
    titles=html('div.title').items()
    infos=html('div.address').items()
    totalList=[]
    for title,info in zip(titles,infos):
        des=info('div.houseInfo').text().split('|')
        floor=''
        buildTime=''
        roomType=''
        area=''
        direction=''
        if len(des)==5:
            floor=des[0]
            buildTime=des[1]
            roomType=des[2]
            area=des[3]
            direction=des[4]
        elif len(des)==3:
            floor=des[0].split()[0]
            roomType=des[0].split()[1]
            area=des[1]
            direction=des[2]
        view_time=info('div.followInfo').text().split('/')
        viewNum=''
        time=''
        if len(view_time)==2:
            viewNum=view_time[0]
            time=view_time[1]
        dict={
            'link':title('a').attr('href'),
            'title':title.text(),
            'floor':floor,
            'buildTime':buildTime,
            'roomType':roomType,
            'area':area,
            'direction':direction,
            'position':info('div.flood > div > a').text(),
            'viewNum':viewNum,
            'time':time,
            'tags':info('div.tag').text(),
            'totalPrice':info('div.priceInfo > div.totalPrice').text(),
            'unitPrice':info('div.priceInfo > div.unitPrice').text()
        }
        totalList.append(dict)
    return totalList
#新房的信息
def get_details2(html,url):
    urlList = url.split('/')
    url = urlList[0] + '//' + urlList[2]
    allItems=html('body > div.resblock-list-container.clearfix > ul.resblock-list-wrapper > li').items()
    totalList=[]
    for item in allItems:
        t_s_t=item('div > div.resblock-name').text().split()
        title=safe_get(0,t_s_t)
        state=safe_get(1,t_s_t)
        type=safe_get(2,t_s_t)
        dict={
            'link':url+item('div > div.resblock-name > a').attr('href'),
            'title':title,
            'state':state,
            'type':type,
            'position':item('div > a.resblock-location').text(),
            'tags':item('div > div.resblock-tag').text(),
            'totalPrice':item('div > div.resblock-price > div.second').text(),
            'unitPrice':item('div > div.resblock-price > div.main-price').text()
        }
        totalList.append(dict)
    return totalList
def get_details3(html,url):
    urlList = url.split('/')
    url = urlList[0] + '//' + urlList[2]
    allItems=html('#content > div.content__article > div.content__list > div').items()
    totalList=[]
    for item in allItems:
        t_t=item('div > p.content__list--item--title.twoline > a').text().split()[0]
        title=safe_get(1,t_t.split('·'))
        rentType=safe_get(0,t_t.split('·'))
        des=item('div > p.content__list--item--des').text().split('/')
        position=''
        area=''
        direction=''
        roomType=''
        floor=''
        if len(des)==3:
            area=des[0]
            roomType=des[2]
        elif len(des)==4:
            area=des[0]
            roomType=des[3]
        elif len(des)==5:
            position=des[0]
            area=des[1]
            direction=des[2]
            roomType=des[3]
            floor=des[4]
        dict={
            'link':url + item('div > p.content__list--item--title.twoline > a').attr('href'),
            'title':title,
            'rentType':rentType,
            'position':position,
            'area':area,
            'direction':direction,
            'roomType':roomType,
            'floor':floor,
            'tags':item('div > p.content__list--item--bottom.oneline').text(),
            'brand':item('div > p.content__list--item--brand.oneline>span.brand').text(),
            'time':item('div > p.content__list--item--brand.oneline > span.content__list--item--time.oneline').text(),
            'price':item('div > span').text()
        }
        totalList.append(dict)
    return totalList
def get_page(page,base_url,typeh):
    url=''
    if typeh=='二手房':
        url=base_url+'/ershoufang/pg'+str(page)+'/'
    elif typeh=='新房':
        urlList = base_url.split('.')
        url = urlList[0] + '.fang' + '.' + urlList[1] + '.' + urlList[2]
        url=url+'/loupan/pg'+str(page)+'/'
    else:
        urlList = base_url.split('.')
        url = urlList[0] + '.zu' + '.' + urlList[1] + '.' + urlList[2]
        url = url + '/zufang/pg' + str(page) + '/#contentList'
    response=requests.get(url)
    html=pq(response.text)
    if typeh=='二手房':
        return get_details1(html)
    elif typeh=='新房':
        return get_details2(html,url)
    else:
        return get_details3(html,url)
def get_all(city,typeh):
    if city not in settings.beikecityDict:
        raise Exception('没有找到该城市')
    url=settings.beikecityDict[city]
    totalDict = {}
    if typeh not in ['二手房','新房','租房']:
        raise Exception('没有找到类型')
    totalDict['name']='beike'
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
    if city not in settings.beikecityDict:
        raise Exception('没有找到该城市')
    url=settings.beikecityDict[city]
    if page < 1 or page > 100:
        raise Exception('输入错误或越界，请重新输入！')
    totalDict = {}
    if typeh not in ['二手房','新房','租房']:
        raise Exception('没有找到类型')
    totalDict['name']='beike'
    totalDict['city']=city
    totalDict['type'] = typeh
    totalDict['pages']=100
    totalDict['data']=get_page(page=page,base_url=url,typeh=typeh)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText