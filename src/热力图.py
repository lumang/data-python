
# coding: utf-8

# In[7]:


#coding=utf-8
import folium
import  time
import requests
from urllib.request import quote
import numpy as np
import pandas as pd
import seaborn as sns
import webbrowser
from folium.plugins import HeatMap
# 导入excel表举例

df = pd.read_csv(r'G:\0102.csv')
df = df.replace(' ',np.nan)
df = df.dropna()


# df['lat'] = df['lat'].apply(lambda x:x[:5])
# df['lng'] = df['lng'].apply(lambda y:y[:6])

num = 164

lat = np.array(df["lat"][0:num])                        # 获取维度之维度值
lon = np.array(df["lng"][0:num])                        # 获取经度值
pop = np.array(df["lat_2"][0:num],dtype=float)    # 获取扫码数，转化为numpy浮点型


data1 = [[lat[i],lon[i],pop[i]] for i in range(num)]    #将数据制作成[lats,lons,weights]的形式

# map_osm = folium.Map(location=[45,125],title='heilongjiangutc',zoom_start=6.5)    #绘制Map，开始缩放程度是5倍
# map_osm = folium.Map([45., 130.], zoom_start=6,control_scale=True,no_touch='50%')
map_osm = folium.Map([45., 130.], zoom_start=6)    #绘制Map，开始缩放程度是5倍

#绘制Map，开始缩放程度是5倍

HeatMap(data1,"1900").add_to(map_osm)  # 将热力图添加到前面建立的map里

file_path = r"C:\Users\Administrator\Desktop\热力图0102.html"
map_osm.save(file_path)     # 保存为html文件

webbrowser.open(file_path)  # 默认浏览器打开


