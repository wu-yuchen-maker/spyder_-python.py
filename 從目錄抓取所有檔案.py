# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:14:16 2019

@author: Admin
"""
#import json

from os import walk
#存放檔案的list
檔=[]

# 指定要列出所有檔案的目錄
mypath = "C:\\Users\\Admin\\Desktop\\法院判決書\\最高法院刑事"

# 遞迴列出所有子目錄與檔案
for root, dirs, files in walk(mypath):
  #print("路徑：", root)
  #print("  目錄：", dirs)
  #print("  檔案：", files)
  檔.append(files)

cc=str(檔).strip('[]')
print(cc)

for i in cc:
 #將每一個檔案print出來  
    print(i,end='')  
  
  
"""
if i==',':
      print(" ",end='')
   else:

 def readJSON(str):
      with open("C:\\Users\\Admin\\Desktop\\法院判決書\\最高法院刑事\\'"+"'", encoding="utf-8") as JS:
          reading = json.load(JS)
      print(reading[str])
      JS.close()
  readJSON("JID")  
""" 