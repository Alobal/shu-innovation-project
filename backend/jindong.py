from includes import *
import settings
import saving
def safe_get(index,lists):
    try:
        result=lists[index]['CommentCountStr']
        return result
    except:
        return ''
def get_details(html,numStr):
    items=html('li.gl-item').items()
    url='https://club.jd.com/comment/productCommentSummaries.action?referenceIds='+numStr+'&callback=jQuery302474&_='+str(int((time.time()*1000)))
    response=requests.get(url)
    text=response.text.replace('jQuery302474(','').replace(');','')
    jsonText=json.loads(text)
    lists=jsonText['CommentsCount']
    count=0
    dictList=[]
    for item in items:
        link=item('div > div.p-name.p-name-type-2 > a').attr('href')
        if 'https' not in link:
            link='https:'+link
        title=item('div > div.p-name.p-name-type-2 > a > em').text().replace('\n','')
        price=item('div > div.p-price > strong').text()
        tags=item('div>div.p-icons').text()
        shop=item('div > div.p-shop > span > a').text()
        price=price.replace('￥', '')
        if price!='':
            price+='元'
        dict={
            'link':link,
            'title':title,
            'price':price,
            'commitNum': safe_get(count,lists),
            'shop':shop,
            'tags':tags
        }
        count+=1
        dictList.append(dict)
    return dictList
def get_page(keyword,page):
    url='https://search.jd.com/Search?'
    url=url+'keyword='+quote(keyword)+settings.jindongUnchange
    url=url+'&page='+str(1+2*(page-1))+'&s='+str(1+60*(page-1))+'&click=0'
    response=requests.get(url,headers=settings.jindongHeadear)
    response.encoding='utf-8'
    html1=pq(response.text)
    items = html1('#J_goodsList > ul > li').items()
    numStr1=''
    for item in items:
        numStr1+=item.attr('data-sku')+','
    numStr1=numStr1[:-1]
    settings.jindongHeadear2['Referer']=url
    url='https://search.jd.com/s_new.php?keyword='+quote(keyword)+settings.jindongUnchange
    url=url+'&page='+str(2*page)+'&s='+str(60*page-29)+'&scrolling=y&log_id='+str(time.time())[:-2]+'&tpl=3_M&show_items='+numStr1
    response=requests.get(url,headers=settings.jindongHeadear2)
    response.encoding = 'utf-8'
    html2=pq(response.text)
    numStr2=''
    items=html2('li.gl-item').items()
    for item in items:
        numStr2+=item.attr('data-sku')+','
    numStr2=numStr2[:-1]
    totalList=[]
    for item in get_details(html1,numStr1):
        totalList.append(item)
    for item in get_details(html2,numStr2):
        totalList.append(item)
    return totalList
def get_all(keyword):
    totalDict = {}
    totalDict['name'] = 'jindong'
    totalDict['keyword'] = keyword
    totalDict['pages'] = 100
    totalList=[]
    for i in range(1,101):
        print('正在爬取第'+str(i)+'页')
        lists=get_page(page=i,keyword=keyword)
        print(len(lists))
        for item in lists:
            totalList.append(item)
    totalDict['data']=totalList
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText
def run(keyword,page):
    totalDict={}
    if page<1 or page>100:
        raise Exception('页数小于1或越界')
    totalDict['name']='jindong'
    totalDict['keyword']=keyword
    totalDict['pages']=100
    totalDict['data']=get_page(keyword,page)
    jsonText=json.dumps(totalDict,ensure_ascii=False)
    return jsonText
saving.saveFile('C://Users/23560/Desktop/file',run('手机',2))
