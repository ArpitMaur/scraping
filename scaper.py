import requests
from bs4 import BeautifulSoup

url='https://www.codewithharry.com/'
res=requests.get(url)
# print(res)
htmlContent=res.content
# print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
para=soup.find_all('p',class_='md:text-base')
# for i in para:
#     print(i.string)
# print(soup.find('p').get_text()) 

# for link in soup.find_all('a'):
#     print(link.get('href'))

