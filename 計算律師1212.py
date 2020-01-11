# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:27:17 2019

@author: Admin
"""
import json
import os 

           
dirPath = r"D:\\test_taipei\\taipei"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]

for j in result:
  with open((dirPath+"\\"+j),mode='r', encoding='utf-8') as f:
    def readJSON(str):
      with open("D:\\test_taipei\\taipei\\"+j+"", encoding="utf-8") as JS:
        reading = json.load(JS)
        json.dumps(reading["group"],ensure_ascii=False)
        print(reading[str])
        JS.close()
    readJSON("lawyer")