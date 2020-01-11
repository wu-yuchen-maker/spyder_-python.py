# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:51:34 2019

@author: Admin
"""

import jieba
jieba.load_userdict("C:\\tools\\結巴.txt")
import json
def readJSON(str):
    with open('C:\\Users\\Admin\\Desktop\\法院判決書\\最高法院民事\\TPSV,85,台上,26,19960111.json', encoding="utf-8") as JS:
        reading = json.load(JS)
        c=json.dumps(reading["JFULL"],separators=(':','\r\n'),ensure_ascii=False)
        c=c.replace("\\","") 
        c=c.replace('r','')
        c=c.replace('n','')
        主文=c.find('主  文')
        理由=c.find('理  由')
        主文斷句=(c[(主文+4):(理由)])
        存主文斷詞 = jieba.cut(主文斷句,cut_all=False)
        for word in 存主文斷詞:
           print(word)
           
    print(reading[str])
    JS.close()

readJSON("JFULL")