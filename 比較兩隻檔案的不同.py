# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:54:18 2019

@author: Admin
"""

file1 = "C:\\Users\\Admin\\Desktop\\predict_web\\new_jieba.txt"

file2 = "C:\\Users\\Admin\\Desktop\\predict_web\\text_for.txt"
f_diff = "C:\\Users\\Admin\\Desktop\\predict_web\\diff.txt"

# ---------- 对比文件内容，输出差异
f1 = open(file1, "r",encoding="utf-8")
f2 = open(file2, "r",encoding="utf-8")
file1 = f1.readlines()
file2 = f2.readlines()
f1.close()
f2.close()
outfile = open(f_diff, "w",encoding="utf-8")

for i in file1:
    if i not in file2:
        outfile.write(i)
     
