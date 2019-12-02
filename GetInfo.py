#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午 09:59
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : getInfo.py
# @Software: PyCharm
import requests
import urllib.parse


def GetInfoFromDate(searchDate):
    url = "https://www.enlightent.cn/research/top/getWeiboHotSearchDayAggs.do?date=" + searchDate + "&type=realTimeHotSearchList&t=1566711807"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    res = requests.get(url=url, headers=headers)
    return res.text


def GetInfoFromKeywords(keywords, page):
    url = "https://www.enlightent.cn/research/top/getWeiboRankSearch.do?keyword=" + urllib.parse.quote(
        keywords) + "&from={}&t=1566711807".format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    res = requests.get(url=url, headers=headers)
    print(url)
    return res.text
    # with open("temp.txt", "a", encoding="utf-8") as fp:
    #     fp.write(res.text)
    # # print(url)
    # with open("temp.txt", "r", encoding="utf-8") as readfile:
    #     return readfile.readlines()
