# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:52:18 2016

@author: zhangchi
"""



import codecs

#file = codecs.open('lol.txt','r','utf-8')
file = codecs.open('/Users/zhangchi/Desktop/summary_monty.txt','r','utf-8')

#file = open("test_1.txt", "r");
BeforeReplace=file.read();
#a = open("test_1.txt").read()  
#BeforeReplace=a.decode("utf-8");
intab = "~@&，,+#*/\[]0123456789()（）【】:：--.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
outab = "                                                                                     ";
str_trantab = str.maketrans(intab,outab);
BeforeReplace=BeforeReplace.translate(str_trantab);
BeforeReplace=BeforeReplace.replace(' ','');
#BeforeReplace=BeforeReplace.replace(' ','');
BeforeReplace=BeforeReplace.replace("支付宝","");
BeforeReplace=BeforeReplace.replace("百度钱包","");
BeforeReplace=BeforeReplace.replace("微信支付","");
BeforeReplace=BeforeReplace.replace("网上消费-","");
BeforeReplace=BeforeReplace.replace("网上消费","");
AfterReplace=BeforeReplace.replace("\n"," ");
#AfterReplace=BeforeReplace.replace("\n"," ").replace("-"," ").replace("("," ").replace(")"," ").replace("【"," ").replace("】"," ").replace(":"," ");
AllWords=AfterReplace.split()
#print(AllWords)
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
a = 0 
b = 0
for item in dictionary:
    if(dictionary[item]>50):
        need[item]=dictionary[item]
        a = a + dictionary[item]
    b = b + dictionary[item]
        #f.write(item)
        #f.write(dictionary[item])

print(a/b)        
#f.close()        
dic = sorted(need.items(),key=lambda d:d[1],reverse=True) 
#print(dictionary) 
#print(dic)
f=open('out20_50.csv','w')
for item in dic:
    #print(item[0])
    if item[0].find("消费－") == 0:
        s=item[0].replace("消费－","");
    elif item[0].find("消费") == 0:
        s=item[0].replace("消费","");
    elif item[0].find("支付") == 0:
        s=item[0].replace("支付","");
    else:
        s=item[0];

    if item[0].find("公司") != -1:
        f.write("2")
    elif item[0].find("有限") != -1:
        f.write("2")
    elif item[0].find("移动") != -1:
        f.write("2")
    elif item[0].find("联通") != -1:
        f.write("2")
    elif item[0].find("苹果") != -1:
        f.write("2")
    elif item[0].find("网易") != -1:
        f.write("2")
    elif item[0].find("饿了么") != -1:
        f.write("2")
    elif item[0].find("外卖") != -1:
        f.write("2")
    elif item[0].find("订单") != -1:
        f.write("2")
    elif item[0].find("游戏") != -1:
        f.write("2")
    elif item[0].find("手机") != -1:
        f.write("2")
    elif item[0].find("棋牌") != -1:
        f.write("2")
    elif item[0].find("饮") != -1:
        f.write("2")
    elif item[0].find("饮") != -1:
        f.write("2")
    elif item[0].find("机票") != -1:
        f.write("2")
    elif item[0].find("医院") != -1:
        f.write("2")
    elif item[0].find("便利") != -1:
        f.write("2")
    elif item[0].find("年费") != -1:
        f.write("2")
    elif item[0].find("购物") != -1:
        f.write("2")
    elif item[0].find("团购") != -1:
        f.write("2")
    elif item[0].find("生活") != -1:
        f.write("2")
    elif item[0].find("红包") != -1:
        f.write("2")
    elif item[0].find("咖啡") != -1:
        f.write("2")
    elif item[0].find("食品") != -1:
        f.write("2")
    elif item[0].find("衣") != -1:
        f.write("2")
    elif item[0].find("旅") != -1:
        f.write("2")
    elif item[0].find("车") != -1:
        f.write("2")
    elif item[0].find("医") != -1:
        f.write("2")
    elif item[0].find("店") != -1:
        f.write("2")
    elif item[0].find("百货") != -1:
        f.write("2")
    elif item[0].find("商场") != -1:
        f.write("2")
    elif item[0].find("超市") != -1:
        f.write("2")
    elif item[0].find("星巴克") != -1:
        f.write("2")
    elif item[0].find("会员") != -1:
        f.write("2")
    elif item[0].find("优惠") != -1:
        f.write("2")
    elif item[0].find("服") != -1:
        f.write("2")
    elif item[0].find("体育") != -1:
        f.write("2")
    elif item[0].find("饭") != -1:
        f.write("2")
    elif item[0].find("亚马逊") != -1:
        f.write("2")
    elif item[0].find("彩票") != -1:
        f.write("2")
    elif item[0].find("保险") != -1:
        f.write("2")
    elif item[0].find("话费") != -1:
        f.write("2")
    elif item[0].find("加油站") != -1:
        f.write("2")
    elif item[0].find("电影") != -1:
        f.write("2")
    elif item[0].find("服") != -1:
        f.write("2")
    elif item[0].find("麦当劳") != -1:
        f.write("2")
    elif item[0].find("财付通") != -1:
        f.write("1")
    #elif item[0].find("支付宝") != -1:
     #   f.write("1")
    elif item[0].find("银") != -1:
        f.write("1")
    elif item[0].find("行") != -1:
        f.write("1")
    elif item[0].find("付") != -1:
        f.write("1")
    elif item[0].find("款") != -1:
        f.write("1")
    elif item[0].find("业务") != -1:
        f.write("1")
    elif item[0].find("分期") != -1:
        f.write("1")
    elif item[0].find("汇") != -1:
        f.write("1")
    elif item[0].find("现") != -1:
        f.write("1")
    elif item[0].find("金") != -1:
        f.write("1")
    elif item[0].find("额") != -1:
        f.write("1")
    elif item[0].find("宝") != -1:
        f.write("1")
    elif item[0].find("贷") != -1:
        f.write("1")
    elif item[0].find("金") != -1:
        f.write("1")
    elif item[0].find("账") != -1:
        f.write("1")
    elif item[0].find("利息") != -1:
        f.write("1")
    elif item[0].find("手续") != -1:
        f.write("1")
    elif item[0].find("信用卡") != -1:
        f.write("1")
    elif item[0].find("还款") != -1:
        f.write("1")
    elif item[0].find("银联") != -1:
        f.write("1")
    elif item[0].find("跨行") != -1:
        f.write("1")
    elif item[0].find("现金") != -1:
        f.write("1")
    elif item[0].find("基金") != -1:
        f.write("1")
    elif item[0].find("京东") != -1:
        f.write("1")
    elif item[0].find("存") != -1:
        f.write("1")
    elif item[0].find("局") != -1:
        f.write("2")
    elif item[0].find("费") != -1:
        f.write("2")
    elif item[0].find("馆") != -1:
        f.write("2")
    elif item[0].find("警") != -1:
        f.write("2")
    elif item[0].find("险") != -1:
        f.write("2")
    elif item[0].find("信息") != -1:
        f.write("2")
    elif item[0].find("网络") != -1:
        f.write("2")
    elif item[0].find("人寿") != -1:
        f.write("2")
    elif item[0].find("厅") != -1:
        f.write("2")
    elif item[0].find("电器") != -1:
        f.write("2")
    elif item[0].find("电子商务") != -1:
        f.write("2")
    elif item[0].find("税") != -1:
        f.write("2")
    elif item[0].find("商") != -1:
        f.write("2")
    elif item[0].find("餐") != -1:
        f.write("2")
    elif item[0].find("航") != -1:
        f.write("2")
    elif item[0].find("科技") != -1:
        f.write("2")
    elif item[0].find("电力") != -1:
        f.write("2")        
    else: 
        f.write("0")
    f.write(",")
    f.write(s)
    f.write(",")
    f.write(str(item[1]))
    f.write("\n")
    
        
f.close() 

print(1)