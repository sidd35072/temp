import urllib.request
response=urllib.request.urlopen("http://php.net")
html=response.read()
print(html)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "htmlSlib")
text=soup.get_txt(strip=True)
print(text)

tokens=[t for t in text.split()]
