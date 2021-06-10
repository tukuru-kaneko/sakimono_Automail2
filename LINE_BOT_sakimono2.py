#!/usr/bin/env python
# coding: utf-8

# In[133]:


import json


# In[134]:


file = open('info.json', 'r')
info = json.load(file)


# In[135]:


# info['CHANNEl_ACCESS_TOKEN']


# In[136]:


from linebot import LineBotApi
from linebot.models import TextSendMessage
from time import sleep


# In[137]:


CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


# In[138]:


# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# ブラウザのオプションを格納する変数をもらってきます。
options = Options()

# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
options.set_headless(True)

# ブラウザを起動する
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# ブラウザでアクセスする
driver.get("https://nikkei225jp.com/")

# HTMLを文字コードをUTF-8に変換してから取得します。
html = driver.page_source.encode('utf-8')

# BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(html, "html.parser")


# In[139]:


contents = soup.find_all('div',class_='win')
content = contents[4]
content
raps = content.find_all('td',class_='rap')
rap = raps[1]
rap
valc0 = rap.find('div',class_='val2 sakiV').text
timc0 = rap.find('span',class_='scol').text
chgc0 = rap.find('span',class_='chng').text
valc0=valc0.replace(',', '')

print("日経MINI"+" "+valc0+" "+chgc0+" "+timc0)

rap=raps[7]
rap
valc2 = rap.find('div',class_='val2 sakiV').text
timc2 = rap.find('span',class_='scol').text
sac2 = rap.find('span',class_='chng').text
valc2=valc2.replace(',', '')
print("DOW先物"+" "+valc2+" "+sac2+" "+timc2)

content01 = contents[5]
content01
raps = content01.find_all('div',class_='tblL')
raps
rap = raps[5]
rap
highslides =rap.find_all('a',class_='highslide')
highslide = highslides[2]
highslide
sW01 = highslide.find('span',id='tV933').text
divT00 = rap.find('div',class_='divT').text
cang00 = rap.find('span',class_='chng').text
print("銅先物"+" "+sW01+" "+cang00+" "+divT00)


# In[140]:


# ブラウザでアクセスする
sleep(3)
driver.get("https://nikkei225jp.com/chart/")

# HTMLを文字コードをUTF-8に変換してから取得します。
html = driver.page_source.encode('utf-8')

# BeautifulSoupで扱えるようにパースします
soup2 = BeautifulSoup(html, "html.parser")


# In[141]:


contents = soup2.find_all('div',class_='win')
content = contents[4]
content
raps = content.find_all('td',class_='rap')
rap = raps[6]
rap
valsakiV01 = rap.find('div',class_='val2 sakiV').text
scol01 = rap.find('span',class_='scol').text
chng01 = rap.find('span',class_='chng').text
valsakiV01=valsakiV01.replace(',', '')
print("TOPIX先物"+" "+valsakiV01+" "+chng01+" "+scol01)

rap=raps[12]
rap
val02 = rap.find('div',class_='val2').text
scol02 = rap.find('span',class_='scol').text
chng02 = rap.find('span',class_='chng').text
print("日経VIX"+" "+val02+" "+chng02+" "+scol02)


# In[142]:


sleep(3)
# ブラウザでアクセスする
driver.get("https://nikkei225jp.com/nasdaq/")

# HTMLを文字コードをUTF-8に変換してから取得します。
html = driver.page_source.encode('utf-8')

# BeautifulSoupで扱えるようにパースします
soup3 = BeautifulSoup(html, "html.parser")


# In[143]:


contents = soup3.find_all('div',class_='win')
content = contents[4]
content
raps = content.find_all('td',class_='rap')
rap = raps[6]
rap
valsakiV03 = rap.find('div',class_='val2 sakiV').text
scol03 = rap.find('span',class_='scol').text
chng03 = rap.find('span',class_='chng').text
valsakiV03=valsakiV03.replace(',', '')

print("NASDAQ100先物"+" "+valsakiV03+" "+chng03+" "+scol03)

rap=raps[7]
rap
val04 = rap.find('div',class_='val2').text
scol04 = rap.find('span',class_='scol').text
chng04 = rap.find('span',class_='chng').text
val04=val04.replace(',', '')

print("S＆P500先物"+" "+val04+" "+chng04+" "+scol04)

rap=raps[11]
rap
val00 = rap.find('div',class_='val2').text
scol05 = rap.find('span',class_='scol').text
chng05 = rap.find('span',class_='chng').text
val05=val04.replace(',', '')

print("ﾄﾞﾙｲﾝﾃﾞｯｸｽ"+" "+val00+" "+chng05+" "+scol05)


# In[144]:


sleep(3)
driver.get("https://ch225.com/")

# HTMLを文字コードをUTF-8に変換してから取得します。
html = driver.page_source.encode('utf-8')

# BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(html, "html.parser")

contents = soup.find_all('div',class_='item_div')

content=contents[3]
ajaxtex3 = content.find('div',class_='ajaxtex colN').text
valc3 = content.find('div',class_='valC').text
timc3 = content.find('div',class_='timC').text
chgc3 = content.find('div',class_='chgC').text

content=contents[4]
ajaxtex4 = content.find('div',class_='ajaxtex colN').text
valc4 = content.find('div',class_='valC').text
timc4 = content.find('div',class_='timC').text
sac4 = content.find('div',class_='saC').text

content=contents[6]
ajaxtex6 = content.find('div',class_='ajaxtex').text
valc6 = content.find('div',class_='valC').text
timc6 = content.find('div',class_='timC').text
chgc6 = content.find('div',class_='chgC').text

content=contents[7]
ajaxtex7 = content.find('div',class_='ajaxtex').text
valc7 = content.find('div',class_='valC').text
timc7 = content.find('div',class_='timC').text
chgc7 = content.find('div',class_='chgC').text

content=contents[9]
ajaxtex9 = content.find('div',class_='ajaxtex colN').text
valc9 = content.find('div',class_='valC').text
timc9 = content.find('div',class_='timC').text
chgc9 = content.find('div',class_='chgC').text

content=contents[10]
ajaxtex10 = content.find('div',class_='ajaxtex colN').text
valc10 = content.find('div',class_='valC').text
timc10 = content.find('div',class_='timC').text
chgc10 = content.find('div',class_='chgC').text

content=contents[11]
ajaxtex11 = content.find('div',class_='ajaxtex colK').text
valc11 = content.find('div',class_='valC').text
timc11 = content.find('div',class_='timC').text
chgc11 = content.find('div',class_='chgC').text

# print(ajaxtex0+" "+valc0+" "+chgc0+" "+timc0)
# print(ajaxtex2+" "+valc2+"\n"+sac2+" "+timc2)
print(ajaxtex3+" "+valc3+" "+chgc3+" "+timc3)
print(ajaxtex4+" "+valc4+"\n"+sac4+" "+timc4)
print(ajaxtex6+" "+valc6+" "+chgc6+" "+timc6)
print(ajaxtex7+" "+valc7+" "+chgc7+" "+timc7)
print(ajaxtex9+" "+valc9+" "+chgc9+" "+timc9)
print(ajaxtex10+" "+valc10+" "+chgc10+" "+timc10)
print(ajaxtex11+" "+valc11+" "+chgc11+" "+timc11)

contents = soup.find_all('div',id='tblWLD')
content=contents[0]
tblL = content.find('div',class_='tblL')

highslide = tblL.find('a',id='aIF212')
highslide

sw2 = highslide.find('span',id='tV212').text
chng2 = highslide.find('span',class_='chng').text
divt2 = highslide.find('div',class_='divT').text

print("米国 NASDAQ"+" "+sw2+" "+chng2+" "+divt2)

highslide = tblL.find('a',id='aIF213')
highslide

sw3 = highslide.find('span',id='tV213').text
chng3 = highslide.find('span',class_='chng').text
divt3 = highslide.find('div',class_='divT').text

print("米国 S&P500"+" "+sw3+" "+chng3+" "+divt3)

highslide = tblL.find('a',id='aIF611')
highslide

sw4 = highslide.find('span',id='tV611').text
chng4 = highslide.find('span',class_='chng').text
divt4 = highslide.find('div',class_='divT').text

print("米国 ﾌｨﾗﾃﾞﾙﾌｨｱ半導体"+" "+sw4+" "+chng4+" "+divt4)

tblLs = content.find_all('div',class_='tblL')
tblL=tblLs[3]

highslide = tblL.find('a',id='aIF112')
highslide

sw5 = highslide.find('span',id='tV112').text
chng5 = highslide.find('span',class_='chng').text
divt5 = highslide.find('div',class_='divT').text

print("日本 TOPIX"+" "+sw5+" "+chng5+" "+divt5)

content = soup.find_all('div',id='tblCX')
content = content[0]

tblLs = content.find_all('div',class_='tblL')
tblL=tblLs[1]

highslide = tblL.find('a',class_='highslide')
highslide

sw6 = highslide.find('span',id='tV931').text
chng6 = highslide.find('span',class_='chng').text
divt6 = highslide.find('div',class_='divT').text

print("金先物"+" "+sw6+" "+chng6+" "+divt6)


# In[145]:


# # rap=raps[3]
# # ajaxtex3 = content.find('div',class_='ajaxtex colN').text
# # valc3 = content.find('div',class_='valC').text
# # timc3 = content.find('div',class_='timC').text
# # chgc3 = content.find('div',class_='chgC').text

# # content=contents[4]
# # ajaxtex4 = content.find('div',class_='ajaxtex colN').text
# # valc4 = content.find('div',class_='valC').text
# # timc4 = content.find('div',class_='timC').text
# # sac4 = content.find('div',class_='saC').text

# content=contents[6]
# ajaxtex6 = content.find('div',class_='ajaxtex').text
# valc6 = content.find('div',class_='valC').text
# timc6 = content.find('div',class_='timC').text
# chgc6 = content.find('div',class_='chgC').text

# content=contents[7]
# ajaxtex7 = content.find('div',class_='ajaxtex').text
# valc7 = content.find('div',class_='valC').text
# timc7 = content.find('div',class_='timC').text
# chgc7 = content.find('div',class_='chgC').text

# content=contents[9]
# ajaxtex9 = content.find('div',class_='ajaxtex colN').text
# valc9 = content.find('div',class_='valC').text
# timc9 = content.find('div',class_='timC').text
# chgc9 = content.find('div',class_='chgC').text

# content=contents[10]
# ajaxtex10 = content.find('div',class_='ajaxtex colN').text
# valc10 = content.find('div',class_='valC').text
# timc10 = content.find('div',class_='timC').text
# chgc10 = content.find('div',class_='chgC').text

# content=contents[11]
# ajaxtex11 = content.find('div',class_='ajaxtex colK').text
# valc11 = content.find('div',class_='valC').text
# timc11 = content.find('div',class_='timC').text
# chgc11 = content.find('div',class_='chgC').text

# print(ajaxtex0+" "+valc0+" "+chgc0+" "+timc0)
# print(ajaxtex2+" "+valc2+"\n"+sac2+" "+timc2)
# print(ajaxtex3+" "+valc3+" "+chgc3+" "+timc3)
# print(ajaxtex4+" "+valc4+"\n"+sac4+" "+timc4)
# print(ajaxtex6+" "+valc6+" "+chgc6+" "+timc6)
# print(ajaxtex7+" "+valc7+" "+chgc7+" "+timc7)
# print(ajaxtex9+" "+valc9+" "+chgc9+" "+timc9)
# print(ajaxtex10+" "+valc10+" "+chgc10+" "+timc10)
# print(ajaxtex11+" "+valc11+" "+chgc11+" "+timc11)

# contents = soup.find_all('div',id='tblWLD')
# content=contents[0]
# tblL = content.find('div',class_='tblL')

# highslide = tblL.find('a',id='aIF212')
# highslide

# sw2 = highslide.find('span',id='tV212').text
# chng2 = highslide.find('span',class_='chng').text
# divt2 = highslide.find('div',class_='divT').text

# print("米国 NASDAQ"+" "+sw2+" "+chng2+" "+divt2)

# highslide = tblL.find('a',id='aIF213')
# highslide

# sw3 = highslide.find('span',id='tV213').text
# chng3 = highslide.find('span',class_='chng').text
# divt3 = highslide.find('div',class_='divT').text

# print("米国 S&P500"+" "+sw3+" "+chng3+" "+divt3)

# highslide = tblL.find('a',id='aIF611')
# highslide

# sw4 = highslide.find('span',id='tV611').text
# chng4 = highslide.find('span',class_='chng').text
# divt4 = highslide.find('div',class_='divT').text

# print("米国 ﾌｨﾗﾃﾞﾙﾌｨｱ半導体"+" "+sw4+" "+chng4+" "+divt4)

# tblLs = content.find_all('div',class_='tblL')
# tblL=tblLs[3]

# highslide = tblL.find('a',id='aIF112')
# highslide

# sw5 = highslide.find('span',id='tV112').text
# chng5 = highslide.find('span',class_='chng').text
# divt5 = highslide.find('div',class_='divT').text

# print("日本 TOPIX"+" "+sw5+" "+chng5+" "+divt5)

# content = soup.find_all('div',id='tblCX')
# content = content[0]

# tblLs = content.find_all('div',class_='tblL')
# tblL=tblLs[1]

# highslide = tblL.find('a',class_='highslide')
# highslide

# sw6 = highslide.find('span',id='tV931').text
# chng6 = highslide.find('span',class_='chng').text
# divt6 = highslide.find('div',class_='divT').text

# print("金先物"+" "+sw6+" "+chng6+" "+divt6)


# In[146]:


days = soup.find('span',class_='TmCol').text
days

#divt5 = highslide.find('div',class_='divT').text


# In[147]:



# print(ajaxtex0+" "+valc0+" "+chgc0+" "+timc0)
# print(ajaxtex2+" "+valc2+"\n"+sac2+" "+timc2)
# print("日本 TOPIX"+" "+sw5+" "+chng5+" "+divt5)
print(ajaxtex3+" "+valc3+" "+chgc3+" "+timc3)
print(ajaxtex4+" "+valc4+"\n"+sac4+" "+timc4)
print("米国 NASDAQ"+" "+sw2+" "+chng2+" "+divt2)
print("米国 S&P500"+" "+sw3+" "+chng3+" "+divt3)
print("米国 半導体"+" "+sw4+" "+chng4+" "+divt4)
print(ajaxtex10+" "+valc10+" "+chgc10+" "+timc10)
print(ajaxtex7+" "+valc7+" "+chgc7+" "+timc7)
print(ajaxtex9+" "+valc9+" "+chgc9+" "+timc9)
print("金先物"+" "+sw6+" "+chng6+" "+divt6)
print(ajaxtex6+" "+valc6+" "+chgc6+" "+timc6)
print(ajaxtex11+" "+valc11+" "+chgc11+" "+timc11)


# In[148]:

message1=days+"\n\n"+"日経先物"+" "+valc0+" "+chgc0+"\n"+"TOPIX先物"+" "+valsakiV01+" "+chng01+"\n"+"ﾀﾞｳ先物"+" "+valc2+" "+sac2+"\n"+"NASDAQ100先物"+" "+valsakiV03+" "+chng03+"\n"+"S＆P500先物"+" "+val04+" "+chng04
message2="半導体"+" "+sw4+" "+chng4+"\n"+"米債10年利回り"+" "+valc10+" "+chgc10+"\n"+"原油"+" "+valc7+" "+chgc7+"\n"+"米VIX"+" "+valc9+" "+chgc9+"\n"+"日経VIX"+" "+val02+" "+chng02+"\n"+"金先物"+" "+sw6+" "+chng6+"\n"+"銅先物"+" "+sW01+" "+cang00+"\n"+ajaxtex6+" "+valc6+" "+chgc6+"\n"+"ﾄﾞﾙｲﾝﾃﾞｯｸｽ"+" "+val00+" "+chng05+"\n"+ajaxtex11+" "+valc11+" "+chgc11


# In[149]:


def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text=message1)
    line_bot_api.push_message(USER_ID,messages=messages)
    
if __name__ == "__main__":
    main()


# In[150]:


def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text=message2)
    line_bot_api.push_message(USER_ID,messages=messages)
    
if __name__ == "__main__":
    main()


# In[ ]:


#h80tTdXHEBGDP7yvSkFZAw44LXEBLR9w6RPZeLvAP1A　ラインノーティストークン、テスト


# In[ ]:


driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:




