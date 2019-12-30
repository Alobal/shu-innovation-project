from includes import *
import settings
import saving
def get_city_link():
    cityUrl='https://www.liepin.com/citylist/'
    response=requests.get(cityUrl,headers=settings.liepinHeadHeaders,cookies=settings.liepinHeadCookie)
    response.encoding='utf-8'
    html=pq(response.text)
    allItems=html('#bd > div > div.citieslist > ol > li').items()
    cityLinkDict={}
    for item in allItems:
        citys=item('p > span:nth-child(2) > a').items()
        for city in citys:
            link=city.attr('href')
            if link!=None:
                url='https://www.liepin.com'+link
                cityLinkDict[city.text()]=url
    return cityLinkDict
def get_city_code():
    codeDict={}
    for k in settings.liepinCityLinkDict:
        url=settings.liepinCityLinkDict[k]
        city_site=re.compile('https://www.liepin.com/city-(.*?)/').findall(url)[0]
        settings.liepinHeadCookie['city_site']=city_site
        response=requests.get(url,headers=settings.liepinHeadHeaders,cookies=settings.liepinHeadCookie)
        html=pq(response.text)
        code=html('#search_form > input[type=hidden]:nth-child(2)').attr('value')
        if code==None:
            break
        else:
            codeDict[k]=code
    return codeDict
def get_details(html):
    allItems=html('ul.sojob-list>li').items()
    totalList=[]
    for item in allItems:
        jobName=item('div > div.job-info > h3 > a').text()
        company=item('div > div.company-info.nohover > p.company-name > a').text()
        salary=item('div > div.job-info > p.condition.clearfix > span.text-warning').text()
        position=item('div > div.job-info > p.condition.clearfix > a').text()
        dict={
            'jobName':jobName,
            'company':company,
            'position':position,
            'salary':salary
        }
        totalList.append(dict)
    return totalList
def get_total_page(city,job):
    tempurl = settings.liepinCityLinkDict[city]
    city_site = re.compile('https://www.liepin.com/city-(.*?)/').findall(tempurl)[0]
    settings.liepinHeaders['city_site'] = city_site
    code = settings.liepinCityCodeDict[city]
    firstUrl = 'https://www.liepin.cn/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&dqs=' + str(code) + '&key=' + quote(job)
    response = requests.get(firstUrl, headers=settings.liepinHeaders, cookies=settings.liepinCookie)
    html=pq(response.text)
    lastLink=html('a.last').attr('href')
    if lastLink!=None:
        pages=re.compile('&curPage=(.*)').findall(lastLink)[0]
        pages=int(pages)
        return pages+1
    else:
        return 1
def get_page(page,city,job):
    print('正在爬取第'+str(page)+'页')
    tempurl = settings.liepinCityLinkDict[city]
    city_site = re.compile('https://www.liepin.com/city-(.*?)/').findall(tempurl)[0]
    settings.liepinHeaders['city_site']=city_site
    code=settings.liepinCityCodeDict[city]
    firstUrl = 'https://www.liepin.cn/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&dqs='+str(code)+'&key='+quote(job)
    if page==1:
        url=firstUrl
        response=requests.get(url,headers=settings.liepinHeaders,cookies=settings.liepinCookie)
        html=pq(response.text)
        return get_details(html)
    else:
        response=requests.get(firstUrl,headers=settings.liepinHeaders,cookies=settings.liepinCookie)
        html=pq(response.text)
        link=html('#sojob > div:nth-child(6) > div > div.job-content > div:nth-child(1) > div > div > a:nth-child(4)').attr('href')
        if link!=None:
            settings.liepinUrlParams['dqs']=code
            settings.liepinUrlParams['key']=quote(job)
            settings.liepinUrlParams['d_curPage']=str(page-2)
            settings.liepinUrlParams['curPage']=str(page-1)
            headckid=re.compile('&headckid=(.*?)&').findall(link)[0]
            ckid=re.compile('&ckid=(.*?)&').findall(link)[0]
            siTag=re.compile('&siTag=(.*?)&').findall(link)[0]
            d_ckId=re.compile('&d_ckId=(.*?)&').findall(link)[0]
            d_headId=re.compile('&d_headId=(.*?)&').findall(link)[0]
            settings.liepinUrlParams['headckid']=headckid
            settings.liepinUrlParams['ckid']=ckid
            settings.liepinUrlParams['siTag']=siTag
            settings.liepinUrlParams['d_ckId']=d_ckId
            settings.liepinUrlParams['d_headId']=d_headId
            url = 'https://www.liepin.com/zhaopin/?'
            for k in settings.liepinUrlParams:
                url += k + '='
                if settings.liepinUrlParams[k] == 'none':
                    url += '&'
                else:
                    url += settings.liepinUrlParams[k]
                    if k != 'curPage':
                        url += '&'
            response=requests.get(url)
            html = pq(response.text)
            return get_details(html)
def get_all(city,job):
    if city  not in settings.liepinCityCodeDict:
        raise Exception("未找到该城市")
    pageNum = get_total_page(city, job)
    totalDict = {}
    totalDict['name'] = 'liepin'
    totalDict['city'] = city
    totalDict['job'] = job
    totalDict['pages'] = pageNum
    totalList=[]
    for i in range(1,pageNum+1):
        lists=get_page(page=i,city=city,job=job)
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText
def run(city,job,page):
    if city  not in settings.liepinCityCodeDict:
        raise Exception("未找到该城市")
    pageNum=get_total_page(city,job)
    if page<1 or page>pageNum:
        raise Exception('页数小于1')
    totalDict={}
    totalDict['name']='liepin'
    totalDict['city']=city
    totalDict['job']=job
    totalDict['pages']=pageNum
    totalDict['data']=get_page(page=page,city=city,job=job)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText