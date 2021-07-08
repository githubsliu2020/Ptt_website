import requests
from bs4 import BeautifulSoup

r = requests.get('https://tw.stock.yahoo.com/q/q?s=2330')             #連接伺服器取得資料
if r.status_code == requests.codes.ok:                            #如果連線正確
	soup = BeautifulSoup(r.text, 'html.parser')                   ##用解析器html.parser找出上面網站連結下的文字存入soup
	#table = soup.find_all('table', attrs={'border': '2'})         #把表格屬性滿足border=2的找出來 
	table = soup.find_all('table')[2]                              #把撈到的表格資料第三個表格(建議用這種寫法)

	#print(table)
	price = table.find_all('td')[2]                          ##把標籤屬性為table下含有'td'屬性的第三號資料取出
	print (price.text)                                            ##印出表格中的文字部分

	#buy_price = table.find_all('td')[3]							#找到標籤屬性為table下含有'td'屬性的第四號資料取出
	buy_price = price.find_next('td')                           #從price直接找下一筆同樣屬性的資料 (會得到跟上面一樣的結果)
	sell_price = buy_price.find_next('td')                      #從buy_price直接找下一筆同樣屬性的資料 

	print (buy_price.text)
	print (sell_price.text)

