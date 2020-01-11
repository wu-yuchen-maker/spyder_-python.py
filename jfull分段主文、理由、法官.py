# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:59:02 2019

@author: user

"""

import json
c=""
def readJSON(str):
    with open("C:\\Users\\Admin\\Desktop\\法院判決書\\最高法院民事\\TPSV,85,台上,19,19960111.json", encoding="utf-8") as JS:
        reading = json.load(JS)
        c=json.dumps(reading["JFULL"],separators=(':','\r\n'),ensure_ascii=False)
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
        
        
        
        print(c[(主文+4):(理由)])
        print(c[(理由+4):(理由結束)])
        print(c[(審判長法官+7):(審判長法官+14)])
        print(c[(法官2+4):(法官2+14)])
        print(c[(法官3+4):(法官3+14)])
        print(c[(法官4+4):(法官4+14)])
        print(c[(法官5+4):(法官5+14)])
        
        
        """
        最高法院=c.find('最高法院民事第三庭')
        print(c[(主文+4):(理由)])
        print(c[(理由+4):(理由結束)])
        print(c[(審判長法官+7):(審判長法官+14)])
        print(c[(理由+4):(最高法院)])
        print(c[(審判長法官+7):(審判長法官+14)])
        """
    print(reading[str])
    JS.close()

readJSON("JFULL")


"""
print(c)
f = open('E:\Tools\結巴python語庫\\存jfull的.txt', 'w+')
f.write(c)
f.close()

c='審判長法官  范  秉  閣'
"""