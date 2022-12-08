# ---------------------------------getting news title from indiatoday.in ---------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website='https://www.indiatoday.in/news.html'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
driver.get(website)


names=[]
links=[]
data=driver.find_elements(By.XPATH ,"//div[@class='NewsList_newslist__1Bh2x NewsList_liststyle__dY1Kl']/ul/li")
for d in data :
    title=d.find_element(By.XPATH,'./h3')
    names.append(title.text)
    link=d.find_element(By.XPATH,'./h3/a')
    link=link.get_attribute('href')
    links.append(link)
    # print(title.text)
    # print(link)
print('-'*100)    
    
driver.close()

df=pd.DataFrame({'Blogs Name':names,'Links':links,})
df.to_csv('News_data.csv',index=False)
# print(df)