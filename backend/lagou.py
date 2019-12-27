from includes import *
import transform
import settings
def get_details(results,sid,page):
    totalList=[]
    for result in results:
        positionId=result['positionId']
        link=''
        if positionId!=None:
            link='https://www.lagou.com/jobs/'+str(positionId)+'.html?show='+sid
        position = ''
        if result['city'] != None:
            position += result['city'] + ' '
        if result['district'] != None:
            position += result['district']
        comLabList = result['companyLabelList']
        companyLabelList = ''
        if comLabList != None:
            for com in comLabList:
                companyLabelList += com
                if com != comLabList[-1]:
                    companyLabelList += '-'
        posLab = result['positionLables']
        positionLaels = ''
        if posLab != None:
            for pos in posLab:
                positionLaels += pos
                if pos != posLab[-1]:
                     positionLaels+='-'
        busZone=result['businessZones']
        businessZones=''
        if busZone!=None:
            for zone in busZone:
                businessZones+=zone
                if zone!=busZone[-1]:
                    businessZones+=','
        dict={
            'link':link,
            'jobName':result['positionName'],
            'position':position,
            'salary':result['salary'],
            'companyName': result['companyShortName'],
            'companySize':result['companySize'],
            'financeStage':result['financeStage'],
            'companyLabels':companyLabelList,
            'jobLabels':positionLaels,
            'workYear':result['workYear'],
            'jobNature':result['jobNature'],
            'education':result['education'],
            'jobAdvantage':result['positionAdvantage'],
            'businessZones':businessZones,
            'createTime':result['createTime']
        }
        totalList.append(dict)
    return totalList
def set_sid(city,name):
    s = requests.Session()
    cookieUrl = 'https://www.lagou.com/jobs/list_' + quote(name) + '?labelWords=&fromSearch=true&suginput='
    s.get(cookieUrl, headers=settings.lagouHeaders1)
    cookie = s.cookies
    post_data = {
        'first': 'true',
        'pn': 1,
        'kd': name
    }
    postUrl = 'https://www.lagou.com/jobs/positionAjax.json?city=' + quote(city) + '&needAddtionalResult=false'
    settings.lagouHeaders['Referer'] = cookieUrl
    response = requests.post(postUrl, data=post_data, headers=settings.lagouHeaders, cookies=cookie)
    jsonText = json.loads(response.text)['content']
    sid = jsonText['showId']
    file = open('sid.txt', 'w')
    file.write(str(sid))
def get_page(page,name,city):
    s=requests.Session()
    cookieUrl='https://www.lagou.com/jobs/list_'+quote(name)+'?labelWords=&fromSearch=true&suginput='
    s.get(cookieUrl,headers=settings.lagouHeaders1)
    cookie=s.cookies
    post_data={
        'first': 'true',
        'pn': page,
        'kd': name
    }
    postUrl = 'https://www.lagou.com/jobs/positionAjax.json?city=' + quote(city) + '&needAddtionalResult=false'
    if page!=1:
        set_sid(city,name)
        file=open('sid.txt','r')
        sid=file.read()
        post_data['sid']=str(sid)
        post_data['first']='false'
        settings.lagouHeaders['Referer']=cookieUrl
        response = requests.post(postUrl, data=post_data, headers=settings.lagouHeaders, cookies=cookie)
        results=json.loads(response.text)['content']['positionResult']['result']
        return get_details(results,sid,page)
    else:
        settings.lagouHeaders['Referer']=cookieUrl
        response = requests.post(postUrl, data=post_data, headers=settings.lagouHeaders, cookies=cookie)
        jsonText=json.loads(response.text)['content']
        sid=jsonText['showId']
        file=open('sid.txt','w')
        file.write(str(sid))
        results=jsonText['positionResult']['result']
        return get_details(results,sid,page)
def get_all(city,job):
    if city not in settings.lagoucityDict:
        raise Exception('没有找到该城市')
    totalDict = {}
    totalDict['name']='lagou'
    totalDict['city']=city
    totalDict['job'] = job
    totalDict['pages']=30
    totalList=[]
    for i in range(1,31):
        lists=get_page(page=i,name=job,city=city)
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    jsonText = json.dumps(totalDict, ensure_ascii=False)
    return jsonText
def run(city,job,page):
    if city not in settings.lagoucityDict:
        raise Exception('没有找到该城市！')
    totalDict={}
    totalDict['name']='lagou'
    totalDict['city']=city
    totalDict['job']=job
    totalDict['pages']=30
    dictList=[]
    if page<1 or page>30:
        raise Exception('page小于1或越界')
    totalDict['data']=get_page(page=page,name=job,city=city)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    jsonText = transform.trans_job(jsonText)
    return jsonText
