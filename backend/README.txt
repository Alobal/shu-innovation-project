接口使用说明
已经实现了6个可用的接口分别用于爬取beike(贝壳)、ziru(自如)、lianjia(链家)、job51(前程无忧)、zhaopin(智联招聘)以及lagou(拉勾网)


基本用法见run.py

下面是相应的使用说明
数据抓取
beike  
   1.导入模块  import beike
   2.使用run(city,type,page) 返回一段json格式文本
   	参数：city:字符串类型，要找的城市
	           type:字符串类型，在"二手房"、"新房"以及"租房" 三者中选择
	           page:整型，要爬取第几页 
    若要获得所有的信息，可以使用get_all(city,typeh)   返回json格式的数据

ziru
   1.导入模块 import ziru
   2.使用run(city,page) 返回一段json格式文本
   	参数：city:字符串类型，要找的城市
	           page:整型，要爬取第几页  
	注意：ziru无type,其只有"租房"一种类型
    若要获得所有的信息，可以使用get_all(city)   返回json格式的数据      获取所有的信息耗时较长，请耐心等待

lianjia
   1.导入模块  import lianjia
   2.使用run(city,type,page) 返回一段json格式文本
   	参数：city:字符串类型，要找的城市
	           type:字符串类型，在"二手房"、"新房"以及"租房" 三者中选择
	           page:整型，要爬取第几页 
   若要获得所有的信息，可以使用get_all(city,typeh)，返回json格式数据    获取所有的信息耗时较长，请耐心等待

job51
   1.导入模块 import job51
   2.使用def run(city,job,page)返回一段json格式文本
   	参数：city:字符串类型，要找的城市
	           type:字符串类型，职位名字
	           page:整型，要爬取第几页
    若要获得所有的信息，可以使用get_all(city,job)，返回json格式数据    获取所有的信息耗时较长，请耐心等待 

lagou
   1.导入模块 import lagou
   2.使用def run(city,job,page)返回一段json格式文本
   	参数：city:字符串类型，要找的城市
	           type:字符串类型，职位名字
	           page:整型，要爬取第几页 
   若要获得所有的信息，可以使用get_all(city,job)，返回json格式数据    获取所有的信息耗时较长，请耐心等待 

zhilian
   1.导入模块 import zhilian
   2.使用def run(city,job,page)返回一段json格式文本
   	参数：city:字符串类型，要找的城市
	           type:字符串类型，职位名字
	           page:整型，要爬取第几页 
    若要获得所有的信息，可以使用get_all(city,job)，返回json格式数据    获取所有的信息耗时较长，请耐心等待 

数据存储：将数据存储到path路径下，并保存为.csv文件格式
   1.导入模块import saving
   2.使用savingFile(path,jsonText)
	参数：path:字符串类型，文件路径
	           jsonText:run()返回的json格式

格式统一：该模块可以将数据统一为房屋类以及招聘类两大数据集合
   1.导入模块transform
   2.使用trans_house(jsonText)     -->将抓取到的房屋信息转换为统一的格式,返回json格式文件
             trans_job(jsonText)          -->将抓取到的招聘信息转换为统一格式，返回json格式文件


       