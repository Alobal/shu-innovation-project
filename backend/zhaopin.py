#智联招聘爬取
from includes import *
import transform
import settings
def getCity():
    response=requests.get('https://www.zhaopin.com/citymap')
    html=pq(response.text)
    jsonText=html('body > script:nth-child(5)').text()
    jsonText=jsonText.replace('__INITIAL_STATE__=','')
    jsonText=json.loads(jsonText)
    alCitys=jsonText['cityList']['cityMapList']
    dict={}
    for k in alCitys:
        citys=alCitys[k]
        for city in citys:
            dict[city['name']]=city['code']
    return dict
def getItems(key,dict):
    if key in dict and dict!="":
        return dict[key]
    return ""
def get_details(html,page):
    totalList=[]
    for item in html:
        welfares=getItems('welfare',item)
        welfareStr=''
        for welfare in welfares:
            welfareStr+=welfare
            if welfare!=welfares[-1]:
                welfareStr+='|'
        dict={
            'link':getItems('positionURL',item),
            'jobName':getItems('jobName',item),
            'salary':getItems('salary',item),
            'position':getItems('display',getItems('city',item)),
            'workingExp':getItems('name',getItems('workingExp',item)),
            'education':getItems('name',getItems('eduLevel',item)),
            'welfare':welfareStr,
            'companyName':getItems('name',getItems('company',item)),
            'companyType':getItems('name',getItems('type',getItems('company',item))),
            'companySize':getItems('name',getItems('size',getItems('company',item)))
        }
        totalList.append(dict)
    return totalList
def get_page(page,city,job):
    posturl='https://fe-api.zhaopin.com/c/i/sou?at=581df3c5a3c64cd09177e102970e7168&rt=e4abf7a4023042a89824e25a3216b50e&_v=0.75911311&x-zp-page-request-id=7f12b12ae38f40ae82d289b1936313e9-1577197002202-77518&x-zp-client-id=0f476728-dc1c-40b9-b9e4-58bb6f2786b8&MmEwMD=4Hn.Cu._O.bmydVp16gooDnCtoU1ms5xYjdtvYVDrBS0IMh0mP2jyWC.quCxkW95e_xyW0DWFQTsy2vCdjFn.31GSoVvUmYm9NzZ57ZM9zKxIzJm88rFr8SeSfVG2odcaLDJrxEs5ZShCulhOL1tb8L1ZNfEIK3px.6AARI8hV6srUbjq8j8EVlXg7crAH0BT74gKcgr4xsQZR18K4UOqCF1Ckg0ulSTc6jYOBE_UpNRQIfZytBTOZgegb96br.gj259wktqV21dWe1wGn1EJJ55zBk4dFObuSod3MKIhltqZzB3jg5yv1uJLxl4K2pIDzEXEEON8LtchudBbc0NnfpagdeZyH_517W_Nnz7oXiLGr8BHdcDdLFGVY8dmAIYObt78EhCLk9VCxPUkk87hol.rlq0NUdAO5UZWT9.2B0O8REo8zYQDFk26qoRlcq6flAg'
    time.sleep(random.random())
    postData={
        'start':90*(page-1),
        'pageSize':"90",
        'cityId':settings.zhaopincityList[city],
        'salary': "0,0",
        'workExperience': "-1",
        'education': "-1",
        'companyType': "-1",
        'employmentType': "-1",
        'jobWelfareTag': "-1",
        'kw': job,
        'kt': "3",
        "": "0",
        'at': "581df3c5a3c64cd09177e102970e7168",
        'rt': "e4abf7a4023042a89824e25a3216b50e",
        '_v': "0.61208422",
        'userCode': '1058494946'
    }
    jdata=json.dumps(postData)
    response=requests.post(posturl,data=jdata)
    jsonText=json.loads(response.text)
    results=jsonText['data']['results']
    return get_details(results,page)
def get_all(city,job):
    if city not in settings.zhaopincityList:
        raise Exception('没有找到该城市')
    totalDict = {}
    totalDict['name']='zhaopin'
    totalDict['city']=city
    totalDict['job'] =job
    totalDict['pages']=50
    totalList=[]
    for i in range(1,51):
        lists=get_page(page=i,city=city,job=job)
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    jsonText = json.dumps(totalDict, ensure_ascii=False)
    return jsonText
def run(city,job,page):
    if city not in settings.zhaopincityList:
        raise Exception('没有找到该城市！')
    if page<1 or page>50:
        raise Exception('page小于1或越界')
    totalDict={}
    totalDict['name']='zhaopin'
    totalDict['city']=city
    totalDict['job']=job
    totalDict['pages']=50
    totalDict['data']=get_page(page=page,city=city,job=job)
    jsonText =json.dumps(totalDict,ensure_ascii=False)
    # jsonText = transform.trans_job(jsonText)
    return jsonText