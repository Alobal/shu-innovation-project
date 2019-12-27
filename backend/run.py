import transform
import zhaopin
import lianjia
import saving
import beike
import job51
import lagou
import ziru

#beike
#获取特定页的信息(json格式),页数范围(第三个参数)1-100
#print(beike.run('上海','二手房',1))
#print(beike.run('上海','新房',1))
#print(beike.run('上海','租房',1))
#获取所有页的信息(json格式)
#print(beike.get_all('上海','二手房'))   #第一个参数即为城市名，第二个参数有三种选择
#对获得的json格式统一化
#print(transform.trans_house(beike.run('上海','二手房',1)))
#print(transform.trans_house(beike.get_all('上海','二手房')))
#保存文件-保存特定页
#saving.saveFile('C://Users/23560/Desktop/file',beike.run('上海','新房',1))
#保存文件-保存所有信息
#saving.saveFile('C://Users/23560/Desktop/file',beike.get_all('上海','二手房'))

'''
print(transform.trans_rent_house(beike.run('上海','租房',1)))
print(transform.trans_rent_house(lianjia.run('上海','租房',1)))
print(transform.trans_rent_house(ziru.run('上海',1)))
'''
'''
print(transform.trans_newHouse(beike.run('上海','新房',1)))
print(transform.trans_newHouse(lianjia.run('上海','新房',1)))
'''
'''
print(transform.trans_seconde_house(beike.run('上海','二手房',1)))
print(transform.trans_seconde_house(lianjia.run('上海','二手房',1)))
'''
print(ziru.run('上海',1))
#lianjia
#获取特定页的信息(json格式),页数范围(第三个参数)1-100
#print(lianjia.run('上海','二手房',1))
#print(lianjia.run('上海','新房',1))
#print(lianjia.run('上海','租房',1))
#获取所有页的信息(json格式)
#print(lianjia.get_all('上海','二手房'))   #第一个参数即为城市名，第二个参数有三种选择
#对获得的json格式统一化
#print(transform.trans_house(lianjia.run('上海','二手房',1)))
#print(transform.trans_house(lianjia.get_all('上海','二手房')))
#保存文件-保存特定页
#saving.saveFile('C://Users/23560/Desktop/file',lianjia.run('上海','新房',1))
#保存文件-保存所有信息
#saving.saveFile('C://Users/23560/Desktop/file',lianjia.get_all('上海','二手房'))


#ziru
#获取特定页的信息(json格式),页数范围1-100     ziru只有租房一种类型
#print(ziru.run('上海',1))
#获取所有页的信息(json格式)   
#print(ziru.get_all('上海'))
#对获得的json格式统一化
#print(transform.trans_house(ziru.run('上海',1)))
#print(transform.trans_house(ziru.get_all('上海')))
#保存文件-保存特定页
#saving.saveFile('C://Users/23560/Desktop/file',ziru.run('上海',1))
#保存文件-保存所有页
#saving.saveFile('C://Users/23560/Desktop/file',ziru.get_all('上海'))
#saving.saveFile('C://Users/23560/Desktop/file',beike.run('上海','租房',1))
#saving.saveFile('C://Users/23560/Desktop/file',lianjia.run('上海','租房',1))


'''
#job51
#得到总页数
print(get_total_page('上海','数据分析'))
#获取特定页的信息(json格式),页数范围(第三个参数)1-get_total_page('上海','数据分析')
print(job51.run('上海','数据分析',1))
#获取所有页的信息(json格式)
print(job51.get_all('上海','数据分析'))   #第一个参数即为城市名，第二个参数为职位名
#对获得的json格式统一化
print(transform.trans_house(job51.run('上海','数据分析',1)))
print(transform.trans_house(job51.get_all('上海','数据分析')))
#保存文件-保存特定页
saving.saveFile('C://Users/23560/Desktop/file',job51.run('上海','数据分析',1))
#保存文件-保存所有信息
saving.saveFile('C://Users/23560/Desktop/file',lianjia.run('上海','数据分析'))
'''

'''
#lagou
#获取特定页的信息(json格式),页数范围(第三个参数)1-30
print(lagou.run('上海','数据分析',1))
#获取所有页的信息(json格式)
print(lagou.get_all('上海','数据分析'))   #第一个参数即为城市名，第二个参数为职位名
#对获得的json格式统一化
print(transform.trans_house(lagou.run('上海','数据分析',1)))
print(transform.trans_house(lagou.get_all('上海','数据分析')))
#保存文件-保存特定页
saving.saveFile('C://Users/23560/Desktop/file',lagou.run('上海','数据分析',1))
#保存文件-保存所有信息
saving.saveFile('C://Users/23560/Desktop/file',lagou.run('上海','数据分析'))
'''

'''
#zhaopin
#获取特定页的信息(json格式),页数范围(第三个参数)1-50
print(zhaopin.run('上海','数据分析',1))
#获取所有页的信息(json格式)
print(zhaopin.get_all('上海','数据分析'))   #第一个参数即为城市名，第二个参数为职位名
#对获得的json格式统一化
print(transform.trans_house(zhaopin.run('上海','数据分析',1)))
print(transform.trans_house(zhaopin.get_all('上海','数据分析')))
#保存文件-保存特定页
saving.saveFile('C://Users/23560/Desktop/file',zhaopin.run('上海','数据分析',1))
#保存文件-保存所有信息
saving.saveFile('C://Users/23560/Desktop/file',zhaopin.run('上海','数据分析'))
'''