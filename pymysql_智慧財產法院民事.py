# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:54:26 2019

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymysql
import json
def readJSON(str):
    with open("C:\\Users\\Admin\\Desktop\\法院判決書\\智慧財產法院民事\\IPCV,104,民著訴,32,20180914,1.json", encoding="utf-8") as JS:
        reading = json.load(JS)
        #將json轉成string型態
        a=json.dumps(reading["JID"],ensure_ascii=False)
        b=json.dumps(reading["JYEAR"])
        c=json.dumps(reading["JCASE"],ensure_ascii=False)
        d=json.dumps(reading["JNO"])
        e=json.dumps(reading["JDATE"])
        f=json.dumps(reading["JTITLE"],ensure_ascii=False)
        g=json.dumps(reading["JFULL"],ensure_ascii=False)
        #轉成str後，資料清理
        a=a.replace('"','')
        b=b.replace('"','')
        c=c.replace('"','')
        d=d.replace('"','')
        e=e.replace('"','')
        f=f.replace('"','')
        g=g.replace('"','')
        
        db = pymysql.connect(host='localhost' ,port=3306, user='root', passwd='', db='智慧財產法院', charset='utf8')
        cursor = db.cursor()
        #sql語法，執行插入
        sql = "INSERT INTO 智慧財產民事(jid,jyear, jcase, jno,jdate,jtitle,jfull) VALUES ('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"')"
#執行語法   ，
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
readJSON("JID")





