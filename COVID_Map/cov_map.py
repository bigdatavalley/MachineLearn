# 基于pyechart1.7.1建立
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pyecharts.charts import Map, Geo
from pyecharts import options as opts

html = urlopen(
    "https://3g.dxy.cn/newh5/view/pneumonia_peopleapp").read().decode('utf-8')
# 获取html网页的源代码
bs = BeautifulSoup(html, "html.parser")

str1 = bs.body.text
# 查找字符串中指定国内省份对应数据的关键字，进行截取
str1 = str1[str1.find('window.getAreaStat = '):] 
data = str1[str1.find('[{'):str1.find('}catch')]
# 字符串转字典数组
data_list = eval(data)
# 省份现存确诊数
new_dict = {}
# 省份累计确诊数
new_dict1 = {}

#循环遍历data_list取数据{省份：确诊数}
for province in data_list:
    #将省份现存确诊数放入new_dict字典中，处理不合格的省份名称replace
    new_dict[province['provinceName'].replace('自治区', '').replace(
        '回族', '').replace('维吾尔', '').replace('省', '').replace('市', '').replace(
            '壮族', '')] = province['currentConfirmedCount']
    #省份累计确诊数
    new_dict1[province['provinceName'].replace('自治区', '').replace(
        '回族', '').replace('维吾尔', '').replace('省', '').replace('市', '').replace(
            '壮族', '')] = province['confirmedCount']

# print(new_dict)
# print(new_dict1)



#将字典中的省份key以列表的形式取出来
province = list(new_dict.keys())
#将字典中确诊数values以列表形式取出来
values = list(new_dict.values())

c = (
    Map(init_opts=opts.InitOpts(
        width='1600px', height='800px', bg_color="white"))
    .add(
            series_name="现存确诊",
            data_pair=[list(z) for z in zip(province, values)],
            maptype='china')
    .set_global_opts(
                title_opts=opts.TitleOpts(title="中国现存确诊病例地图"),
                visualmap_opts=opts.VisualMapOpts(
                    pieces=[{
                        "max": 0,
                        "label": "0人",
                        "color": "#FFFFFF"
                    }, {
                        "min": 1,
                        "max": 9,
                        "label": "1-10人",
                        "color": "#FFEBCD"
                    }, {
                        "min": 10,
                        "max": 99,
                        "label": "10-99人",
                        "color": "#FFA07A"
                    }, {
                        "min": 100,
                        "max": 499,
                        "label": "100-499人",
                        "color": "#FF4040"
                    }, {
                        "min": 500,
                        "max": 999,
                        "label": "500-999人",
                        "color": "#CD2626"
                    }, {
                        "min": 1000,
                        "max": 10000,
                        "label": "1000-10000人",
                        "color": "#B22222"
                    }, {
                        'min': 10000,
                        "label": ">10000人",
                        "color": "#8B1A1A"
                    }],
                    # 颜色是否分段显示（False为渐变，True为分段）
                    is_piecewise=True,
                ))
    .render("疫情地图.html"))
    


province1 = list(new_dict1.keys())
values1 = list(new_dict1.values())

c = (
    Map(init_opts=opts.InitOpts(
        width='1600px', height='800px', bg_color="white"))
    .add(
            series_name="累计确诊",
            data_pair=[list(z) for z in zip(province1, values1)],
            maptype='china')
    .set_global_opts(
                title_opts=opts.TitleOpts(title="中国累计确诊病例地图"),
                visualmap_opts=opts.VisualMapOpts(
                    pieces=[{
                        "max": 0,
                        "label": "0人",
                        "color": "#FFFFFF"
                    }, {
                        "min": 1,
                        "max": 9,
                        "label": "1-10人",
                        "color": "#FFEBCD"
                    }, {
                        "min": 10,
                        "max": 99,
                        "label": "10-99人",
                        "color": "#FFA07A"
                    }, {
                        "min": 100,
                        "max": 499,
                        "label": "100-499人",
                        "color": "#FF4040"
                    }, {
                        "min": 500,
                        "max": 999,
                        "label": "500-999人",
                        "color": "#CD2626"
                    }, {
                        "min": 1000,
                        "max": 10000,
                        "label": "1000-10000人",
                        "color": "#B22222"
                    }, {
                        'min': 10000,
                        "label": ">10000人",
                        "color": "#8B1A1A"
                    }],
                    # 颜色是否分段显示（False为渐变，True为分段）
                    is_piecewise=True,
                ))
    .render("累计疫情地图.html"))
    
    
    
str2 = bs.body.text
str2 = str2[str2.find('window.getListByCountryTypeService2true = '):]
data2 = str2[str2.find('[{'):str2.find('}catch')]
data2 = data2.replace('true', 'True')
data2 = data2.replace('false', 'False')
data_list2 = eval(data2)  # 字符串转换成字典数组
# print(data_list2)
world_confirmedCount = {}


import pandas as pd
for province2 in data_list2:
    #对特殊字符串做处理
    world_confirmedCount[province2['provinceName'].replace(
        '钻石公主号邮轮', '').replace('其他', '')] = province2['confirmedCount']
    world_confirmedCount[
        province2['provinceName']] = province2['confirmedCount']

country = pd.read_csv("国家对照表.csv")
dict_country = country.set_index('中文').T.to_dict('list')
new_world_count = {}
for k, v in world_confirmedCount.items():
    try:
        key = dict_country.get(k)[0]
        new_world_count[key] = v
    except Exception as e:
        pass
        
        
 # 把中国的确诊人数加入
ChinaCount = re.search(
    r'"countRemark":"","currentConfirmedCount":(\-?)\d*,"confirmedCount":(\-?)\d*',
    bs.body.text)
zs_dict = eval('{' + ChinaCount.group().replace('"countRemark":"",', '') + '}')
del zs_dict['currentConfirmedCount']
zs_dict['china'] = zs_dict.pop('confirmedCount')
# 将中国累计确诊数据添加到world_dict
new_world_count.update(zs_dict)




province = list(new_world_count.keys())  #将字典中的省份key以列表的形式取出来
values = list(new_world_count.values())  #将字典中确诊数values以列表形式取出来

c = (
    Map(init_opts=opts.InitOpts(
        width='1600px', height='800px', bg_color="white"))
    .add(
            series_name="累计确诊",
            data_pair=[list(z) for z in zip(province, values)],
            maptype='world',
            label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
                title_opts=opts.TitleOpts(title="世界现存确诊病例地图"),
                visualmap_opts=opts.VisualMapOpts(
                    pieces=[{
                        "max": 0,
                        "label": "0人",
                        "color": "#FFFFFF"
                    }, {
                        "min": 1,
                        "max": 9,
                        "label": "1-10人",
                        "color": "#FFEBCD"
                    }, {
                        "min": 10,
                        "max": 99,
                        "label": "10-99人",
                        "color": "#FFA07A"
                    }, {
                        "min": 100,
                        "max": 499,
                        "label": "100-499人",
                        "color": "#FF4040"
                    }, {
                        "min": 500,
                        "max": 999,
                        "label": "500-999人",
                        "color": "#CD2626"
                    }, {
                        "min": 1000,
                        "max": 10000,
                        "label": "1000-10000人",
                        "color": "#B22222"
                    }, {
                        'min': 10000,
                        "label": ">10000人",
                        "color": "#8B1A1A"
                    }],
                    # 颜色是否分段显示（False为渐变，True为分段）
                    is_piecewise=True
                ))
    .render("世界疫情地图.html"))
