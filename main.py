#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午 09:53
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : main.py
# @Software: PyCharm
import os
import run

if __name__ == '__main__':
    choose_num = str(input("[1]直接爬取热搜\n[2]按搜索词爬取热搜\n[!]选择爬取模式:"))
    os.system("cls")
    if choose_num == "1":
        search_date = str(input("[!]请输入日期，如2019/01/02："))
        os.system("cls")
        run.runDate(search_date)
    elif choose_num == "2":
        search_keywords = str(input("[!]请输入关键词："))
        os.system("cls")
        run.runKeywords(search_keywords)
    else:
        breakpoint()