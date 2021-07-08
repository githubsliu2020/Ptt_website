import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
r = requests.get('https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')             #連接伺服器取得資料
if r.status_code == requests.codes.ok:                            #如果連線正確
	# soup = BeautifulSoup(r.text, 'html.parser')                   ##用解析器html.parser找出上面網站連結下的文字存入soup
	# print(soup.prettify())                                        #用prettyfy來確定抓回來的資料有我們在網頁裡看到的資訊
	soup = BeautifulSoup(r.text, 'lxml')                          #如果有問題就改用lxml來重新解析
	#print(soup.prettify())
	
	tables = soup.find_all('table', attrs={'cellpadding': '2'})    #把撈到的表格資料屬性cellpadding = 2的表格取出
	#print(tables[0])
	for table in tables:                                           #找出所有table標籤們
		trs = table.find_all('tr')                                  #找出table裡的tr標籤們
		for tr in trs:                                              #把每個tr中的td找出來
			date, value, price = [td.text for td in tr.find_all('td')]      #將tr內的資料讀出並分別寫入於date, value, price 三個分類
			
			if date == '日期':                                               #跳過含有日期這個文字的列     
				continue
			data.append([date, value, price])

df = pd.DataFrame(data, columns=['日期', '買賣超金額', '台指期'])     #用pandas模組寫入標題
df.to_csv('big_eight.csv', encoding='utf-8-sig')                    #寫入CSV 並以正確的編碼方式寫入
print(data)                                                         #印出找到的td們
			#raise SystemExit                                        #印完第一個tds就終止程式



