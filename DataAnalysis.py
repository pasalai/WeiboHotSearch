#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午 10:25
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : DataAnalysis.py
# @Software: PyCharm

from snownlp import SnowNLP
import visualization

# 初始化数组
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
        # 情感分析，通过更换微博预料训练生成的.model.3模型可提高分析的精确度
        Affective_value = SnowNLP(keywords)
        # 计算消息的正负面情绪值，并写入Getvalue.xlsx中
        Affective_value_good = Affective_value.sentiments
        Affective_value_bad = 1 - Affective_value_good
        List = [keywords, Affective_value_good, Affective_value_bad]
        print(List[0], List[1], List[2])
        if Affective_value.sentiments < 0.1:
            temp0.append(keywords)
        elif Affective_value.sentiments >= 0.1 and Affective_value.sentiments < 0.2:
            temp1.append(keywords)
        elif Affective_value.sentiments >= 0.2 and Affective_value.sentiments < 0.3:
            temp2.append(keywords)
        elif Affective_value.sentiments >= 0.3 and Affective_value.sentiments < 0.4:
            temp3.append(keywords)
        elif Affective_value.sentiments >= 0.4 and Affective_value.sentiments < 0.5:
            temp4.append(keywords)
        elif Affective_value.sentiments >= 0.5 and Affective_value.sentiments < 0.6:
            temp5.append(keywords)
        elif Affective_value.sentiments >= 0.6 and Affective_value.sentiments < 0.7:
            temp6.append(keywords)
        elif Affective_value.sentiments >= 0.7 and Affective_value.sentiments < 0.8:
            temp7.append(keywords)
        elif Affective_value.sentiments >= 0.8 and Affective_value.sentiments < 0.9:
            temp8.append(keywords)
        elif Affective_value.sentiments >= 0.9:
            temp9.append(keywords)
        else:
            return "err"
        return List
    elif endmark == "1":
        # final = []
        # final.append(temp0)
        # final.append(temp1)
        # final.append(temp2)
        # final.append(temp3)
        # final.append(temp4)
        # final.append(temp5)
        # final.append(temp6)
        # final.append(temp7)
        # final.append(temp8)
        # final.append(temp9)
        # # print(final)
        # list_len = [len(final[0]), len(final[1]), len(final[2]), len(final[3]), len(final[4]), len(final[5]),
        #             len(final[6]),
        #             len(final[7]), len(final[8]), len(final[9])]
        list_len = [len(temp0), len(temp1), len(temp2), len(temp3), len(temp4), len(temp5),
                    len(temp6), len(temp7), len(temp8), len(temp9)]
        print(list_len)
        visualization.visualization(list_len)
