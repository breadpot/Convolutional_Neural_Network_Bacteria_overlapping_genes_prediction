#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
import subprocess
import re
import os
import string
import sys

FASTA= sys.argv[1]
NETvocab= sys.argv[2]
region= sys.argv[3]
label_dic= sys.argv[4]
predictmodel= sys.argv[5]

string="cat ? | grep -v \">\" > seq.test.txt"
print type(string)
string2 = string.replace("?",FASTA)
val = os.system(string2)
#将fasta文件的DNA序列部分提取出来

#subprocess.call("cat seq.test.txt | tr A-Z a-z > lowcase.test.txt ", shell = True)
with open(r'seq.test.txt') as o:
    lineo=o.readlines()
with open(r'lowcase.test.txt',"w+") as k:
    for line0 in lineo:
        line1 = line0.lower()
        print >> k, line1,
#如果fasta文件是大写的碱基，则将其转换为小写

f = open(r'./lowcase.test.txt','r')
d = open('./test.txt.tok','w')
for line2 in f.readlines():
    line3 = re.sub(r"(?<=\w)(?=(?:\w\w\w\w\w\w)+$)", " ", line2) #进行分组
    print >> d, line3,
#将分组后的数据写入文件


subprocess.call("cut -b 1 seq.test.txt > temp.test.cat ", shell = True)

with open(r'temp.test.cat') as r:
    line4=r.readlines()
with open(r'test.cat',"w+") as w:
    for l in line4:
        line5 = re.sub(r"\w", "0", l)
        print >> w, line5,
        #生成一个label文件，是模型应用所必须的，标签需要在字典里有对应的存在才可以，在这里标签的对错不会对预测结果不会产生影响，因为模型之前已经建立好了这里只计算概率值
pass
f.close()
d.close()
o.close()
k.close()
#务必保证所有打开的文件已经被正确关闭
#在此之前请确认神经网络的训练程序已经被正确安装并且已经添加入系统环境变量

string3="prepText gen_regions input_fn=test vocab_fn=? region_fn_stem=test label_dic_fn=& patch_size=#"

print type(string3)
string4 = string3.replace("?",NETvocab)
string5 = string4.replace("#",region)
string6 = string5.replace("&",label_dic)

print(string6)
val = os.system(string6)
#使用字典生成向量用于计算，一个模型对应的训练与测试向量必须一致，不然后面的模型将无法起始

string7="reNet 0:1 predict model_fn=# prediction_fn=result.prediction tstname=test datatype=sparse data_dir=./ WriteText"
print type(string7)
string8 = string7.replace("#",predictmodel)
print(string8)
val = os.system(string8)
#确保环境变量被正确配置才能正常运行上面的代码
#subprocess.call(["prepText","gen_regions","input_fn=test","vocab_fn=1.vocab","region_fn_stem=test","label_dic_fn=s-cat.dic","patch_size=3"])
#subprocess.call(["reNet","0:1","predict","model_fn=predict.Net","prediction_fn=result.prediction","tstname=test","datatype=sparse","data_dir=./","WriteText"])
