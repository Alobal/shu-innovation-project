from includes import *
import settings
def safe_get(k,dict):
    if k in dict:
        return dict[k]
    return ""
def get_token(job,city):
    response=requests.get('https://zhaopin.baidu.com/quanzhi?query='+quote(job)+'&city='+quote(city),headers=settings.baiduHeaders)
    html=pq(response.text)
    body=html('body')
    body=str(body)
    nekotStr=''
    count=0
    for c in body:
        if c=='\n':
            if count==7:
                break
            count+=1
        else:
            if count==6:
                nekotStr+=c
    token=nekotStr.replace('data["nekot"]','').replace(';','').replace(' ','')[::-1]
    token=token[:-1].replace('"','')
    return token
def get_list(job,city):
    response = requests.get('https://zhaopin.baidu.com/quanzhi?query=' + quote(job) + '&city=' + quote(city),headers=settings.baiduHeaders)
    text=response.text
    html = pq(text)
    body = html('body')
    body = str(body)
    nekotStr = ''
    count = 0
    for c in body:
        if c == '\n':
            if count == 19:
                break
            count += 1
        else:
            if count == 18:
                nekotStr += c

    jsonText=nekotStr.replace('data["list"]','').replace('=','').replace(' ','')
    jsonList=eval(jsonText.replace(';',''))
    return jsonList
def get_details(jobLists):
    totalList=[]
    for job in jobLists:
        #link=job['url'].replace('\\','')
        dict={
            'jobName':job['title'],
            'company':job['officialname'],
            'positon':job['province'],
            'salary':job['ori_salary']
        }
        totalList.append(dict)
    return totalList
def get_page(page,city,job):
    url='https://zhaopin.baidu.com/quanzhi?query='+quote(job)+'&city='+quote(city)
    if page==1:
        jsonList=get_list(job,city)
        return get_details(jsonList)
    else:
        token=get_token(job,city)
        params={
            'query': quote(job),
            'city': quote(city),
            'is_adq': '1',
            'pcmod': '1',
            'token': quote(token),
            'pn': str(page*20),
            'rn': '20'
        }
        url='https://zhaopin.baidu.com/api/qzasync?'
        for k in params:
            url+=k+'='+params[k]
            if k!='rn':
                url+='&'
        response=requests.get(url,headers=settings.baiduHeaders)
        jsonText=json.loads(response.text)
        dataList=safe_get('disp_data',jsonText['data'])
        return get_details(dataList)
def get_all(city,job):
    if city not in settings.baiduCitys:
        raise Exception("未找到该城市")
    totalDict={}
    totalDict['name'] = 'baiduZhaopin'
    totalDict['city'] = city
    totalDict['job'] = job
    totalDict['pages'] = 35
    totalList=[]
    for i in range(1,36):
        print('正在爬取第'+str(i)+'页')
        lists=get_page(page=i,city=city,job=job)
        for item in lists:
            totalList.append(item)
        totalDict['data'] = totalList
    jsonText = json.dumps(totalDict, ensure_ascii=False)
    return jsonText
def run(city,job,page):
    if city not in settings.baiduCitys:
        raise Exception("未找到该城市")
    if page < 1 or page > 35:
        raise Exception('页数小于1')
    totalDict={}
    totalDict['name']='baiduZhaopin'
    totalDict['city']=city
    totalDict['job']=job
    totalDict['pages']=35
    totalDict['data']=get_page(page=page,city=city,job=job)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText

