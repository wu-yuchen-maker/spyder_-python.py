# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:05:52 2019

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:31:41 2019

@author: user


\最高法院刑事-20190517T053459Z-001\最高法院刑事
"TPSM,85,台上,67,19960104.json"餵過

"""

import pymysql
import json   
             
def readJSON(str):
    with open("C:\\Users\\Admin\\Desktop\\法院判決書\\最高法院刑事\\TPSM,85,台上,11,19960104.json", encoding="utf-8") as JS:
        reading = json.load(JS)
        a=json.dumps(reading["JDATE"])
        b=json.dumps(reading["JTITLE"],ensure_ascii=False)
        c=json.dumps(reading["JFULL"],ensure_ascii=False)
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='最高法院', charset='utf8')
        a=a.replace('"',"")
        b=b.replace('"',"")
        c=c.replace("\\","") 
        c=c.replace('r','')
        c=c.replace('n','')
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
#建立操作游標
        cursor = db.cursor()
#SQL語法
        sql = "INSERT INTO 最高法院刑事(jdate,jtitle,主文,理由,審判長法官,法官1,法官2,法官3,法官4) VALUES ('"+a+"','"+b+"','"+j主+"','"+j理+"','"+j審+"','"+j官1+"','"+j官2+"','"+j官3+"','"+j官4+"')"
        
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
readJSON("JFULL")

