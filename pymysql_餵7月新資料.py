# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:31:41 2019

@author: user


dirPath = r"E:\\Download\\20190701法律科技開放法學資料\\python測試\\福建連江地方法院"
"""

import pymysql
import json
import os 
           
dirPath = r"E:\\Download\\20190701法律科技開放法學資料\\python測試\\智慧財產法院"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]

for j in result:
 with open((dirPath+"\\"+j),mode='r', encoding='UTF-8') as f:
   def readJSON(str):
      with open("E:\\Download\\20190701法律科技開放法學資料\\python測試\\智慧財產法院\\"+j+"", encoding="utf-8") as JS:
        reading = json.load(JS)
        a=json.dumps(reading["court"],ensure_ascii=False)
        b=json.dumps(reading["date"],ensure_ascii=False)
        c=json.dumps(reading["no"],ensure_ascii=False)
        d=json.dumps(reading["sys"],ensure_ascii=False)
        e=json.dumps(reading["reason"],ensure_ascii=False)
        f=json.dumps(reading["judgement"],ensure_ascii=False)
        db = pymysql.connect(host='localhost', port=3307, user='Flash', passwd='THE_FLASH', db='7月新的資料', charset='utf8')
        
        a=a.replace('"',"")
        b=b.replace('"',"")
        c=c.replace('"',"")
        d=d.replace('"',"")
        e=e.replace('"',"")
        f=f.replace('"',"")
        f=f.replace("\\","") 
        f=f.replace('r','')
        f=f.replace('n','')
        """
        主文=c.find('主  文')
        理由=c.find('理  由')
        理由結束=c.find('中      華      民      國')
        審判長法官=c.find('審判長法官')
        法官2=c.find('法官',(審判長法官+14))
        法官3=c.find('法官',(法官2+14))
        法官4=c.find('法官',(法官3+14))
        法官5=c.find('法官',(法官4+14))
        j主=c[(主文+4):(理由)]
        j理=c[(理由+4):(理由結束)]
        j審=c[(審判長法官+7):(審判長法官+14)]
        j官1=c[(法官2+4):(法官2+14)]
        j官2= c[(法官3+4):(法官3+14)]
        j官3= c[(法官4+4):(法官4+14)]
        j官4=c[(法官5+4):(法官5+14)]
"""
#建立操作游標
        cursor = db.cursor()
#SQL語法
        sql = "INSERT INTO 智慧財產法院(jcourt,jdate,jno,jsys,jreason,jjudegement) VALUES ('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')"    
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
      print(reading[str])
      JS.close()
   readJSON("no")