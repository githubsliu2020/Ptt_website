import requests                     ##導入requests模組
from bs4 import BeautifulSoup       ##從bs4 導入BeautifulSoup模組
root_url = 'http://disp.cc/b/'      ##設置網站根目錄(路徑)

r = requests.get('https://disp.cc/b/PttHot')  ##連線伺服器網站取得資料
soup = BeautifulSoup(r.text, 'html.parser')   ##用解析器html.parser找出上面網站連結下的文字存入soup

for span in soup.select('#list span.listTitle'):  #用css selector的寫法篩選資料
	href = span.find('a').get('href')
	if href == '796-59l9':
		break

	url = root_url + href
	title = span.text

	print(f'{title}\n{url}')       #列印篩選後的資料標題與連結

