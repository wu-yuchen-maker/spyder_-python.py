# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:27:34 2019

@author: user

import pymysql
import json   

python2json = {}
#構造list
listData = [19960126]
listData1 = ["偽造有價證券"]
listData2 = ["按住居所及所在地不明者"]
python2json["listData"] = listData
python2json["listData1"] = listData1
python2json["listData2"] = listData2
#轉換成json字串
json_str = json.dumps(python2json["listData"],ensure_ascii=False)
json_str2 = json.dumps(python2json["listData1"],ensure_ascii=False)
json_str3 = json.dumps(python2json["listData2"],ensure_ascii=False)


db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='stest', charset='utf8')
#建立操作游標
cursor = db.cursor()
#SQL語法
sql = "INSERT INTO stestforp(jyear,jtitle,jfull) VALUES ('"+json_str+"','"+json_str2.encode("utf8").decode("cp950", "ignore")+"','"+json_str3+"')"
#執行語法  ,jyear,jcase,jno,jdate,jtitle,jfull

try:
  cursor.execute(sql)
  #提交修改
  db.commit()
  print('success')
except:
  #發生錯誤時停止執行SQL
  db.rollback()
  print('error')

#關閉連線
db.close()
"""
import jieba
import json
#--------------------------------
# 存停用詞, 分詞, 過濾後分詞的list
#--------------------------------
stopWords=[]
segments=[]
remainderWords=[]
#--------------------------------
# 讀入停用詞檔
#--------------------------------
jieba.load_userdict("E:\Tools\結巴python語庫\\結巴.txt")
def readJSON(str):
    with open("E:\Tools\判決書json\\TPSV,85,台上,1,19960105.json", encoding="utf-8") as JS:
        reading = json.load(JS)
        c=json.dumps(reading["JFULL"],separators=(':','\r\n'),ensure_ascii=False)
        c=c.replace("\\","") 
        c=c.replace('r','')
        c=c.replace('n','')
      
        words = jieba.cut(c,cut_all=False)
        
        f = open('E:\Tools\結巴python語庫\\存jfull的.txt','w', encoding='UTF-8')
        f.write(c)
        f.close()
        
        ff = open('E:\Tools\結巴python語庫\\停用詞.txt','w', encoding='UTF-8')
        for word in words:
           ff.write(word)
           ff.write("\n")
        
        ff.close()
        
    print(reading[str])
    JS.close()

readJSON("JFULL")

with open('E:\Tools\結巴python語庫\\停用詞.txt', 'r', encoding='UTF-8') as file:
    for data in file.readlines():
        data = data.strip()
        stopWords.append(data)
        
#--------------------------------
# 讀入文件檔, 進行中文斷詞
#--------------------------------
with open('E:\Tools\結巴python語庫\\存jfull的.txt', 'r', encoding='UTF-8') as file:
    #讀入文檔
    text = file.read()
    #結巴中文斷詞
    segments = jieba.cut(text, cut_all=False)
#------------------------------
# 移除停用詞及跳行符號
#------------------------------
remainderWords = list(filter(lambda a: a not in stopWords and a != '\n', segments))

#------------------------------
# 印出過濾後的分詞
#------------------------------
for k in remainderWords:
    print(k,end='')
