# WeiboHotSearch （数据源网站改版，需账号积分，此项目已失效）
微博热搜情绪挖掘分析可视化    
    
项目使用Pycharm编写，python版本为python3.7    
数据分析使用的是python的SnowNLP库，可自行使用相关语料进行训练，通过更换model.3文件提高情感分析精确度    
> 微博语料：[500W微博语料.sql](https://pan.baidu.com/s/1eSeXh5K)密码：tvdo    
> 数据来源：[热搜神器](http://www.enlightent.cn/research/rank/weiboSearchRank)    
## 运行前注意！    
* 开始前请先下载安装用到的库<code>pip install -r requirements.txt</code>    
* 在当前目录打开终端，输入python ./main.py 开始运行    
* 注意输入数据的格式    
* **url中的t值为每天变化的，所以我上传的肯定失效了，t值从[热搜神器](http://www.enlightent.cn/research/rank/weiboSearchRank)找**    
    
![t值获取](https://github.com/lsc183754539/WeiboHotSearch/blob/master/img/t_value_get.png)    
    
更换下面框出：    
    
![更换到这里](https://github.com/lsc183754539/WeiboHotSearch/blob/master/img/t_change.jpg)    
    
    
    
## 运行过程预览    
    
    
![运行过程1](https://github.com/lsc183754539/WeiboHotSearch/blob/master/img/1.jpg)    
![运行过程2](https://github.com/lsc183754539/WeiboHotSearch/blob/master/img/2.jpg)    
![运行过程3](https://github.com/lsc183754539/WeiboHotSearch/blob/master/img/3.jpg)    
    
    
## 函数组成    
├─ main.py    
│  └─ main()    
├─ run.py    
│  ├─ runDate()    
│  └─ runKeywords()    
├─ GetInfo.py    
│  ├─ GetInfoFromDate()    
│  └─ GetInfoFromKeywords()    
├─ DataAnalysis.py    
│  └─ DataAnalysis()       
├─ visualization.py    
│  ├─ pycharts_visit()    
│  └─ visualization()    
    
# 2019年12月3日更新    
* 完善了关键词搜索分析功能
* 添加了散点图可视化（未完成）
* 更新了项目失效说明
