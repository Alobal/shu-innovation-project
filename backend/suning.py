from includes import *
import saving
def get_details(html):
    allItems = html('div.item-bg>div').items()
    dictList=[]
    for item in allItems:
        link = item('div > div.res-img > div.img-block>a').attr('href')
        if link==None:
            continue
        link = 'https:' + link
        title=item('div.title-selling-point').text()
        Info=item('div.res-info > div.price-box > span')
        datasku=Info.attr('datasku')
        brand_id=Info.attr('brand_id')
        threegroup_id=Info.attr('threegroup_id')
        dataStr=''
        for k in range(len(datasku)):
            if datasku[k]!='|':
                dataStr+=datasku[k]
            else:
                break
        length=18-len(dataStr)
        for i in range(length):
            dataStr='0'+dataStr
        url='https://ds.suning.com/ds/generalForTile/'+dataStr+'____'+threegroup_id+'_'+brand_id+'-010-2-0000000000-1--ds0000000003206.jsonp?callback=ds0000000003206'
        response=requests.get(url)
        text=response.text
        jsonText=text.replace('ds0000000003206(','').replace(');','')
        jsonText=json.loads(jsonText)
        price=jsonText['rs'][0]['price']
        if price!='':
            price+='元'
        tags=jsonText['rs'][0]['promotionLable']
        Info=jsonText['rs'][0]['promotionList']
        for key in Info:
            tags+=' '+key['simple']
        commitNum=item('div.res-info > div.evaluate-old.clearfix > div>a').text()
        shop=item('div.res-info > div.store-stock > a').text()
        dict={
            'link':link,
            'title':title,
            'price':price,
            'commitNum':commitNum,
            'shop':shop,
            'tags':tags
        }
        dictList.append(dict)
    return dictList
def get_page(page,keyword,id):
    # print('正在爬取第'+str(page)+'页')
    totalList=[]
    for paging in range(4):
        url='https://search.suning.com/emall/searchV1Product.do?keyword='+quote(keyword)+'&ci='+id+'&pg=01&cp=0&il='+str(page-1)+'&st=0&iy=0&isDoufu=1&isNoResult=0&n=1&sesab=ACAABAABCAAA&id=IDENTIFYING&cc=010&paging='+str(paging)+'&sub=1&jzq=13460'
        response=requests.get(url)
        html=pq(response.text)
        tempList=get_details(html)
        for item in tempList:
            totalList.append(item)
    return totalList
def get_all(keyword):
    totalDict = {}
    totalDict['name'] = 'suning'
    totalDict['keyword'] = keyword
    totalDict['pages'] = 50
    totalList=[]
    response = requests.get('https://search.suning.com/' + quote(keyword) + '/')
    id = re.compile('\n"categoryId": (.*),').findall(response.text)[0]
    for i in range(1,51):
        lists=get_page(i, keyword,id)
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    return totalDict
def run(keyword,page):
    totalDict={}
    totalDict['name']='suning'
    totalDict['keyword']=keyword
    totalDict['pages']=50
    response = requests.get('https://search.suning.com/'+quote(keyword)+'/')
    id = re.compile('\n"categoryId": (.*),').findall(response.text)[0]
    totalDict['data']=get_page(page,keyword,id)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText

