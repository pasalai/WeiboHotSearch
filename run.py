#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午 10:14
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : run.py
# @Software: PyCharm

import json
import jieba
import pandas as pd
import GetInfo as GetInfo
import DataAnalysis as analysis


def runDate(searchDate):
    key_value = []
    getinfo = GetInfo.GetInfoFromDate(searchDate)
    print(getinfo)
    if "Apache Tomcat" not in getinfo:
        infoJson = json.loads(getinfo)
        for i in range(len(infoJson)):
            marktarg = "0"
            if i == len(infoJson) - 1:
                marktarg = "1"
            list = analysis.DataAnalysis("".join(jieba.cut(infoJson[i]['keywords'])), marktarg)
            key_value.append(list)
            # result = \
            #     "Keywords:" + infoJson[i]['keyword'] \
            #     + "\tAddress:" + infoJson[i]['url'] \
            #     + "\tCount:" + str(infoJson[i]['count']) \
            #     + "\tSearchCount:" + str(infoJson[i]['searchCount']) \
            #     + "\tRank:" + str(infoJson[i]['rank'])
            # with open("./outPut/getInfoDate.txt", "w", encoding="utf-8") as addtofile:
            #     addtofile.write(result)
    else:
        return 0
    print(key_value)
    pdData = pd.DataFrame(data=key_value, columns=["事件", "正面", "负面"])
    pdData.to_excel("./outPut/hotSearch.xlsx")


def runKeywords(Keywords):
    key_value = []
    for page in range(1, 45):
        getinfo = GetInfo.GetInfoFromKeywords(Keywords, page)
        # 判断服务器是否能正常回复信息，报错时返回ApacheTomcat 404/402/500等，取共同值
        if "Apache Tomcat" not in getinfo:
            # 格式化数据
            infoJson = json.loads(getinfo)
            marktarg = "0"
            # 如果获取完90页信息，将endmark标记置为"1"
            if page == 90:
                marktarg = "1"
            # 格式化得到的数据分析并保存
            for i in range(len(infoJson["rows"])):
                # 调用keywords分析函数,传递keywords值和endmark标记
                list = analysis.DataAnalysis("".join(jieba.cut(infoJson["rows"][i]['keywords'])), marktarg)
                key_value.append(list)
                # result = "duration:" + str(infoJson["rows"][i]['duration']) \
                #          + "\t标题：" + str(infoJson["rows"][i]['keywords']) \
                #          + "\tupdateTime:" + str(infoJson["rows"][i]['updateTime']) \
                #          + "\t数据源平台:" + str(infoJson["rows"][i]['type']) \
                #          + "\ttopRanking:" + str(infoJson["rows"][i]['topRanking']) \
                #          + "\t数据源地址:" + str(infoJson["rows"][i]['url']) \
                #          + "\tfirstRankingTime:" + str(infoJson["rows"][i]['firstRankingTime'])
                # with open("getInfoKeywords.txt", "a", encoding="utf-8") as addtofile:
                #     addtofile.write(result)
        else:
            return 0
    print(key_value)
    pdData = pd.DataFrame(data=key_value, columns=["事件", "正面", "负面"])
    pdData.to_excel("./outPut/keywordSearch.xlsx")
