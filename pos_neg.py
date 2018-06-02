from natto import MeCab
import os
import csv 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

fp = open("sakaguchi_sakura.txt.txt",encoding="utf-8_sig") 
doc = fp.read()

nm = MeCab("-Ochasen") #茶筅形式に出力フォーマットを変更。

list_keitaiso = [i.split() for i in nm.parse(doc).splitlines()]

fp2= open('sakaguchi_sakura.txt.csv', 'ab') 
 
with open('sakaguchi_sakura.txt.csv','a') as fp2:
    writer = csv.writer((fp2), lineterminator="\n")
    for i in range(0,len(list_keitaiso)):
        writer.writerow(list_keitaiso[i]) #CSVファイルに書き出し

# 単語感情極性対応表<http://www.lr.pi.titech.ac.jp/~takamura/pndic_ja.html>
panfile = "pn_ja.dic" 

def readpandic(file):
    with open(file,"r",encoding="utf-8_sig") as dicfile:
        items = dicfile.read().splitlines()
    return {u.split(':')[0]: float(u.split(':')[3]) for u in items}

pandic = readpandic(panfile)

df = pd.read_csv('sakura_keitaiso.csv',names=('a','b','c','d','e','f'))
meishi = list(df[df['d']=='名詞-一般']['a'])

#名詞を抽出
pn =[]
for sentence in meishi:
    for i in sentence:
        pn.append(pandic.get(i))

#Noneの文字を消す
pn2 = [ i for i in pn if not str(i) == "None"]

#表を作成
x1 = pn2
plt.hist(x1, bins=50)
plt.title('P/N Frequency of text')
plt.xlabel("P/N value")
plt.ylabel("Frequency")
plt.legend()
plt.show 
