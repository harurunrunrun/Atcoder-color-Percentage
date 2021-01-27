import requests
import datetime

str="https://atcoder.jp/users/harurun?graph=dist"
site=requests.get(str)
doc=site.text
s=""
for i in range(len(doc)):
  if doc[i:i+8]=="var data":
    for j in range(i+11,len(doc)):
      s+=doc[j]
      if doc[j]=="]":
        break
    break
JST=datetime.timezone(datetime.timedelta(hours=+9),"JST")
now_date=datetime.datetime.now(JST)
day=now_date.strftime("%Y年%m月%d日 %H:%M:%S")
rate_list=eval(s)
user_all=sum(rate_list)
pat_sum=user_all
var=[0,1,2,3,4,5,7,9,12,15,19,25,32,42,54,69,89,114,147,188,242,311,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
red=sum(rate_list[46:])
orange=sum(rate_list[42:46])+red
yellow=sum(rate_list[38:42])+orange
blue=sum(rate_list[34:38])+yellow
sky=sum(rate_list[30:34])+blue
green=sum(rate_list[26:30])+sky
brown=sum(rate_list[22:26])+green
gray=sum(rate_list[:22])+brown


htmlcode=f'''
<html>
<head>
<title>atcoder color percentages</title>
<meta http-equiv="content-type" charset="Shift_JIS">
</head>
<body>
<h1>AtCoder color Percentage</h1>
<p>最終更新日時: {day} (JST)</p>
<p><font color="red">赤: 上位 {100*red/user_all}%</font></p>
<p><font color="#FF9900">橙: 上位 {100*orange/user_all}%</font></p>
<p><font color="#CCCC00">黄: 上位 {100*yellow/user_all}%</font></p>
<p><font color="blue">青: 上位 {100*blue/user_all}%</font></p>
<p><font color="aqua">水: 上位 {100*sky/user_all}%</font></p>
<p><font color="green">緑: 上位 {100*green/user_all}%</font></p>
<p><font color="brown">茶: 上位 {100*brown/user_all}%</font></p>
<p><font color="gray">灰: 上位 {100*gray/user_all}%</font></p>
<br><br><br>
<p>このページは手動更新です。</p>
<p>更新されていないとき、あるいは詳しい分布を知りたいときはREADMEを読んでください。</p>
<a href="https://github.com/harurunrunrun/Atcoder-color-Percentage">github</a>
</body>
</html>
'''
with open("index.html",mode="w")as file:
  file.write(htmlcode)
