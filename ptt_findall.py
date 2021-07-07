import requests                     ##導入requests模組
from bs4 import BeautifulSoup       ##從bs4 導入BeautifulSoup模組
root_url = 'http://disp.cc/b/'      ##設置網站根目錄(路徑)

r = requests.get('https://disp.cc/b/PttHot')  ##取得網站資料
soup = BeautifulSoup(r.text, 'html.parser')   ##用解析器html.parser找出上面網站連結下的文字存入soup
spans = soup.find_all('span', class_='listTitle') #找出所有class類別在listTitle的資料
for span in spans:                                 #在滿足以上類別的資料中
	
	href = span.find('a').get('href')               #如果連結的id為796-59l9則剔除不列印
	if href == '796-59l9':
		break
	url = root_url + href  #定義整個link的連結文字字串
	title = span.text      #取出標題

	#print (url)
	print (f'{title}\n{url}') #印出標題,換行符號,接著顯示連結完整字串

#print([s.text for s in spans])

