from bs4 import BeautifulSoup
import requests

query = input(': ')
url = 'https://www.dictionary.com/browse/' + query

html_text = requests.get(url).text
soup = BeautifulSoup(html_text,'lxml')

means = soup.find('span',class_='one-click-content css-nnyc96 e1q3nk1v1').text
print(means)
