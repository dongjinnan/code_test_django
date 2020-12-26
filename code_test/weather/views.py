import os
import time
import json
import platform
import requests
import urllib.request as r
from django.http import HttpResponse
from django.shortcuts import render

URL = 'http://api.openweathermap.org/data/2.5/weather?q=%s&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'

def index(request):
    city_list = get_city_list()
    city = city_list[0] if len(city_list) > 0 else 'Dalian'
    url= URL % city
    try:
        data = r.urlopen(url).read().decode('utf-8')
        json_data = json.loads(data)
        if json_data['cod'] == 200:
            result = parse_res_data(json_data)
            return render(request, 'index.html',{'city_list': city_list, 'city_weather': result})
        else:
            return render(request, 'index.html', {'city_list': city_list, 'city_weather': {}, 'errmsg': 'city不存在'})
    except Exception as e:
        print(e)
        return render(request, 'index.html',{'city_list': city_list, 'city_weather': {}, 'errmsg': 'city不存在'})

def get_weather(request):
    city = request.GET.get("city")
    url = URL % city
    try:
        data = r.urlopen(url).read().decode('utf-8')
        json_data = json.loads(data)
        if json_data['cod'] == 200:
            result = parse_res_data(json_data)
        else:
            result = {'errmsg': 'city不存在'}
    except Exception as e:
        print(e)
        result = {'errmsg': 'city不存在'}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 组装返回前台数据	
def parse_res_data(data):
    result = {}
    result['city'] = data['name']
    result['weather'] = data['weather'][0]['description']
    result['tem'] = data['main']['temp']
    result['win'] = data['wind']['speed']

    timeArray = time.localtime(data['dt'])
    result['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return result

# 获取城市列表	
def get_city_list():
    city_file = os.getcwd() + '/weather/conf/city.txt'
    city_list = []
    with open(city_file, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            city_list.append(line)

    return city_list