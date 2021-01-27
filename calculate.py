#atcoderを直接たたいているので過度な使用はご遠慮ください
import requests
from bs4 import BeautifulSoup

name=input("type AtCoder ID:")
str=f"https://atcoder.jp/users/{name}?graph=dist"
site=requests.get(str)
data=BeautifulSoup(site.text,'html.parser')
doc=site.text
start=0
usr_rank=""
doc_len=len(doc)
rank_bool=True
for i in range(doc_len-8):
  if rank_bool and doc[i:i+38]=='<tr><th class="no-break">Rank</th><td>':
    for j in range(i+38,i+49):
      if doc[j]=="t":
        rank_bool=False
        usr_rank=int(usr_rank)
        break
      usr_rank+=doc[j]
  if doc[i:i+8]=="var data":
    start=i+11
    break
s=""
for i in range(start,doc_len):
  s+=doc[i]
  if doc[i]=="]":
    break

var=[0,1,2,3,4,5,7,9,12,15,19,25,32,42,54,69,89,114,147,188,242,311,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000]
l=eval(s)
user_all=sum(l)
su=user_all
print(l)
print(f"全ての参加者: {user_all}人")
print(f"{name} : {usr_rank}位")
print(f"{name} : 上位{usr_rank*100/user_all}% ")
for i in range(len(var)-1):
  st=f"{var[i]}"
  en=f"{var[i+1]}"
  print(f"{st.rjust(4)}～{en.rjust(4)}: 上位{su*100/user_all}%")
  su-=l[i]
print(f"{var[-1]}以上: 上位{su*100/user_all}%")
