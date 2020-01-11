# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:27:26 2019

@author: Admin
"""
import jieba
import pymysql
jieba.load_userdict("C:\\tools\\結巴.txt")
db = pymysql.connect(host='localhost' ,port=3306, user='root', passwd='', db='最高法院', charset='utf8')

cursor = db.cursor()
sql = "SELECT 主文,理由 FROM 最高法院刑事 "

try:
 cursor.execute(sql)
  #提交修改
 db.commit()
 print('success')
 result = cursor.fetchone()
 row = cursor.fetchone()
 f=open("C:\\Users\\Admin\\Desktop\\專題\\spyder_練習python.py","r")
 while result is not None:
   存主文結巴 = jieba.cut(result[0],cut_all=False)
   for word in 存主文結巴:
     if word[0]==" "or  word[0]=='　': 
       print("",end="")
     elif word[0]=='。' or word[0]=='，':  
       print("",end="")
     else:  
       print(word,end=" / ")
   print("\n")
       
   存理由結巴 = jieba.cut(result[1],cut_all=False)
   with open('output.txt', 'w', encoding='UTF-8') as outfile:
    for word in 存理由結巴:
     if word[0]==" ": 
       print("",end="")
     elif word[0]=="　"or word[0]=='  ': 
       print("",end="")
     elif word[0]=="  ": 
       print("",end="")
     elif word[0]=="…": 
       print("",end="")
     elif word[0]=="，": 
       print("",end="")
     elif word[0]=="。": 
       print("",end="")
     elif word[0]=="；": 
       print("",end="")
     elif word[0]=="、": 
       print("",end="") 
     elif word[0]=="："or word[0]=="「"or word[0]=="」"or word[0]=="○" or word[0]=="": 
       print("",end="")
     elif word[0]=="(" or word[0]=="（"or word[0]=="?": 
       print("",end="")  
     elif word[0]==")" or word[0]=="）": 
       print("",end="") 
     elif word[0]=="1" or word[0]=="2" or word[0]=="3"or word[0]=="4"or word[0]=="5"or word[0]=="6"or word[0]=="7"or word[0]=="8"or word[0]=="9"or word[0]=="0":
       print(word,end="") 
     elif word[0]=="第": 
       print(word,end="")
     elif word[0]=="條": 
       print(word,end="")
     else:  
       outfile.write(word)
       outfile.write(" / ")
   #print(result[0])
   #print(result[1])
   result = cursor.fetchone()
   print("\n")
  # print(type(result))
except:
  #發生錯誤時停止執行SQL
 db.rollback()
 print('error')
#關閉連線
db.close()