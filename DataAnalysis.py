#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午 10:25
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : DataAnalysis.py
# @Software: PyCharm

from snownlp import SnowNLP
import visualization as visit
# import pandas as pd

temp0 = []
temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []
temp7 = []
temp8 = []
temp9 = []


def DataAnalysis(keywords, endmark):
    if endmark != "1":  # 根据标记确定是否结束
        # 情感分析，通过更换微博预料训练生成的.model.3模型进行分析
        print(keywords)
        Affective_value = SnowNLP(keywords)
        # 计算消息的正负面情绪值，并写入Getvalue.xlsx中
        Affective_value_good = Affective_value.sentiments
        Affective_value_bad = 1- Affective_value_good
        list = [keywords, Affective_value_good, Affective_value_bad]
        print(list)
        # pddata = pd.DataFrame(data=list, columns=["关键词", "正面值", "负面值"])
        # pddata.to_excel(mode="a", sheet_name="Getvalue.xlsx")
        if Affective_value.sentiments < 0.1:
            temp0.append(keywords)
            # print(temp0)
        elif Affective_value.sentiments >= 0.1 and Affective_value.sentiments < 0.2:
            temp1.append(keywords)
            # print(temp1)
        elif Affective_value.sentiments >= 0.2 and Affective_value.sentiments < 0.3:
            temp2.append(keywords)
            # print(temp2)
        elif Affective_value.sentiments >= 0.3 and Affective_value.sentiments < 0.4:
            temp3.append(keywords)
            # print(temp3)
        elif Affective_value.sentiments >= 0.4 and Affective_value.sentiments < 0.5:
            temp4.append(keywords)
            # print(temp4)
        elif Affective_value.sentiments >= 0.5 and Affective_value.sentiments < 0.6:
            temp5.append(keywords)
            # print(temp5)
        elif Affective_value.sentiments >= 0.6 and Affective_value.sentiments < 0.7:
            temp6.append(keywords)
            # print(temp6)
        elif Affective_value.sentiments >= 0.7 and Affective_value.sentiments < 0.8:
            temp7.append(keywords)
            # print(temp7)
        elif Affective_value.sentiments >= 0.8 and Affective_value.sentiments < 0.9:
            temp8.append(keywords)
            # print(temp8)
        elif Affective_value.sentiments >= 0.9:
            temp9.append(keywords)
            # print(temp9)
        else:
            return "err"
        return 0
    elif endmark == "1":
        final = []
        final.append(temp0)
        final.append(temp1)
        final.append(temp2)
        final.append(temp3)
        final.append(temp4)
        final.append(temp5)
        final.append(temp6)
        final.append(temp7)
        final.append(temp8)
        final.append(temp9)
        # print(final)
        list = [len(final[0]), len(final[1]), len(final[2]), len(final[3]), len(final[4]), len(final[5]), len(final[6]),
                len(final[7]), len(final[8]), len(final[9])]
        print(list)
        visit.visualization(list)
