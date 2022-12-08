# --------------------------------getting news from nytimes.com------------------------
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
driver.get("https://www.nytimes.com/international/section/science")

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')
Titles=[]
Descs=[]
Links=[]
Dates=[]
Arthurs=[]
for d in soup.find_all('li',class_='css-112uytv'):
    
    title=d.find('h2',class_='css-1kv6qi e15t083i0')   
    desc=d.find('p',class_='css-1pga48a e15t083i1')   
    link=d.find('a',href=True) 
    link=link['href']  
    link='https://www.nytimes.com/'+link
    date=d.find('span',{'data-testid':'todays-date'}) 
    arthur=d.find('span',class_='css-1n7hynb')   
     
    Titles.append(title.string)
    Descs.append(desc.string)
    Links.append(link)
    Dates.append(date.string)
    Arthurs.append(arthur.string)
    
        
    
driver.quit()
df=pd.DataFrame({'Titles':Titles,'Descriptions':Descs,'Links':Links,'Dates':Dates,'Arthurs':Arthurs})
df.to_csv('news_data.csv',index=False)
print(df)   
