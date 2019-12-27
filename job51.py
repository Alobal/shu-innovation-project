#前程无忧
from includes import *
import settings
def getAreadId():
    url='https://www.51job.com/'
    response=requests.get(url)
    response.encoding='gbk'
    html=pq(response.text)
    dict={}
    idDict={}
    allItems=html('#area_channel_layer_all>div').items()
    for item in allItems:
        citys=item('span').items()
        for city in citys:
           dict[city('a').text()]='https:'+city('a').attr('href')
    print(dict)
    for k in dict:
        print('正在爬取'+str(k))
        response=requests.get(dict[k])
        response.encoding='gbk'
        html = response.text
        areaid = re.compile('areaid=(.*?)&').findall(html)[0]
        idDict[k]=areaid
    return idDict
def get_details(html,page):
    allItems=html('#resultList>div.el').items()
    count=0
    totalList=[]
    for item in allItems:
        if count==0:
            count+=1
            continue
        dict ={
            'link':item('p > span > a').attr('href'),
            'jobName':item('p > span > a').text(),
            'companyName':item('span.t2 > a').text(),
            'position':item('span.t3').text(),
            'salary':item('span.t4').text(),
            'time':item('span.t5').text()
        }
        totalList.append(dict)
    return totalList
#得到总共有多少页数
def get_total_page(city,name):
    if city not in settings.qianCityId:
       raise Exception("未找到该城市")
    cityid=settings.qianCityId[city]
    url = 'https://search.51job.com/list/' + cityid + ',000000,0000,00,9,99,' + quote(name) + ',2,' + str(
        1) + '.html?' + settings.jobUnchange
    response = requests.get(url)
    response.encoding = 'gbk'
    html = pq(response.text)
    totalPage=html('#resultList > div.dw_page > div > div > div > span:nth-child(3)').text()
    pageNum=re.compile('共(.*?)页，到第').findall(totalPage)[0]
    pageNum=eval(pageNum)
    return pageNum
def get_page(page,cityid,name):
    url = 'https://search.51job.com/list/' + cityid + ',000000,0000,00,9,99,' + quote(name) + ',2,' + str(
        page) + '.html?'+settings.jobUnchange
    response=requests.get(url)
    response.encoding='gbk'
    html=pq(response.text)
    return get_details(html,page)
def get_all(city,job):
    if city not in settings.qianCityId:
        raise Exception("未找到该城市")
    cityid = settings.qianCityId[city]
    pageNum = get_total_page(city=city, name=job)
    if pageNum == 0:
        raise Exception('未找到有关职业的相关信息')
    totalDict = {}
    totalDict['name']='job51'
    totalDict['city']=city
    totalDict['job'] =job
    totalDict['pages']=pageNum
    totalList=[]
    for i in range(1,pageNum+1):
        print('正在爬取第'+str(i)+'页')
        lists=get_page(page=i,cityid=cityid,name=job)
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    jsonText = json.dumps(totalDict, ensure_ascii=False)
    return jsonText
def run(city,job,page):
    if city not in settings.qianCityId:
       raise Exception("未找到该城市")
    cityid=settings.qianCityId[city]
    pageNum=get_total_page(city=city,name=job)
    if pageNum==0:
        raise Exception('未找到有关职业的相关信息')
    if page<1 or page>pageNum:
        raise Exception('页数小于1')
    totalDict={}
    totalDict['name']='job51'
    totalDict['city']=city
    totalDict['job']=job
    totalDict['pages']=pageNum
    totalDict['data']=get_page(page=page,cityid=cityid,name=job)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText