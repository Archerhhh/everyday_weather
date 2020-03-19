# coding: utf-8
# author: hmk

import requests
import json
import yaml
from everyday_wether.utils.get_path import get_path
from everyday_wether.utils.logger import logger

class QueryWeather:
    def __init__(self):

        with open(get_path()+"/data/weather_api.yaml", "r", encoding="utf-8") as self.weather_api_file:
            """读取天气接口配置文件"""
            self.weather_api = yaml.load(self.weather_api_file, Loader=yaml.FullLoader)  # self.config_data表示配置文件的数据
        # print(self.weather_api)
        # print(type(self.weather_api))

        with open(get_path()+"/data/city.json", "r", encoding="utf-8") as self.city_file:
            """读取城市数据文件"""
            self.city_data = json.load(self.city_file)
        # print(self.city_data)
        # print(type(self.city_data))

        # 调用实况天气的请求信息
        self.live_dates_weather_url = self.weather_api["live_dates_weather"]["url"]
        self.live_dates_weather_payload = self.weather_api["live_dates_weather"]["payload"]


    def live_dates_weather(self, city_id=None, city=None):
        """查询实况天气（1天）"""

        payload = self.live_dates_weather_payload
        payload["cityid"] = city_id
        payload["city"] = city

        response = requests.get(self.live_dates_weather_url, params=payload)

        if response.status_code == 200:
            data = response.json()
            try:
                print(data)
                logger.debug(data)  # 调用日志模块
            except Exception as e:
                print("请求失败，错误信息为 %d", e)

    def main(self):
        self.live_dates_weather(city="广州")



if __name__ == '__main__':
    t = QueryWeather()
    t.main()