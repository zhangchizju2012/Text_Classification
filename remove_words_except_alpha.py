# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:03:28 2016

@author: zhangchi
"""

import codecs
import re

#file = codecs.open('lol.txt','r','utf-8')
file = codecs.open('/Users/zhangchi/Desktop/summary.txt','r','utf-8')

#file = open("test_1.txt", "r");
BeforeReplace=file.read();
#a = open("test_1.txt").read()  
#BeforeReplace=a.decode("utf-8");

#BeforeReplace=''.join([x for x in BeforeReplace if (x.isalpha() or x == "\n")])
rule=re.compile(r'[^a-zA-z\\\n]')
BeforeReplace=rule.sub('',BeforeReplace);
#intab = "0123456789()（）【】:：--.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
#outab = "                                                                         ";
#str_trantab = str.maketrans(intab,outab);
#BeforeReplace=BeforeReplace.translate(str_trantab);
BeforeReplace=BeforeReplace.replace(' ','');
#BeforeReplace=BeforeReplace.replace(' ','');
#BeforeReplace=BeforeReplace.replace(" ","");
AfterReplace=BeforeReplace.replace("\n"," ");
#AfterReplace=BeforeReplace.replace("\n"," ").replace("-"," ").replace("("," ").replace(")"," ").replace("【"," ").replace("】"," ").replace(":"," ");
AllWords=AfterReplace.split()
print(AllWords)
dictionary={}
for item in AllWords:
    if item in dictionary:
        dictionary[item]=dictionary[item]+1
    else:
        dictionary[item]=1

#dic = sorted(dictionary.items(),key=lambda d:d[1],reverse=True) 
#print(dictionary) 
#print(dic)

#f=open('out.txt','w')

need={}
for item in dictionary:
    if(dictionary[item]>30):
        need[item]=dictionary[item]
        #f.write(item)
        #f.write(dictionary[item])
        
#f.close()        
dic = sorted(need.items(),key=lambda d:d[1],reverse=True) 
#print(dictionary) 
print(dic)
f=open('out4.txt','w')
for item in dic:
    #print(item[0])
    f.write(item[0])
    f.write(":")
    f.write(str(item[1]))
    f.write("\n")
    
        
f.close() 

