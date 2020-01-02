
# coding: utf-8

# In[5]:


#!usr/bin/env python
#encoding:utf-8
from __future__ import division
 
'''
__Author__:
功能： folium绘图模块学习实践
'''
 
import os
import json
import folium
import pandas as pd
from folium import plugins
 
 
 
# url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
url = 'G:/'

try:
    state_geo = url+'us-states.json'
    state_unemployment = url+'US_Unemployment_Oct2012.csv'
except:
    state_geo='us-states.json'
    state_unemployment='US_Unemployment_Oct2012.csv'
    
state_data = pd.read_csv(state_unemployment) # 读取文件
m = folium.Map(location=[48, -102],zoom_start=3,tiles='Stamen Toner')
folium.Choropleth(state_geo,data=state_data,columns=['State', 'Unemployment'],
                  key_on='feature.id',fill_color='YlGn',fill_opacity=0.7,
                  line_opacity=0.2,legend_name='Unemployment Rate (%)').add_to(m)
popup = 'Must be on top of the choropleth'
folium.CircleMarker(location=[48, -102],radius=10,fill=True,popup=popup,
                    weight=1,).add_to(m)
m.save(os.path.join(url, 'CheckZorder.html'))# 保存html文件

