# ---------------------------------getting news tile and data inside it from hindustanTimes --------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

website='https://www.hindustantimes.com/india-news'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
driver.get(website)
wait = WebDriverWait(driver, 10)

newsTitle=[]
links=[]
contents=[]

data=driver.find_elements(By.XPATH ,"//section/div/h3")
for d in data :
    link=d.find_element(By.XPATH,'./a')
    link=link.get_attribute('href')
    links.append(link)
    # print(link)

print('-'*50+'Totle Pages-->'+str(len(links))+'-'*50)
i=1
for link in links:
    driver.get(link)
    title=wait.until(EC.presence_of_element_located((By.XPATH,"//section/div/div/h1")))
    newsTitle.append(title.text)
    # print(title.text)
    
    content=wait.until(EC.presence_of_element_located((By.XPATH,"//section/div/div/div[4]/div[1]")))
    contents.append(content.text)

    time.sleep(2)
    print('-'*100+' Page---> "'+str(i)+'"')   
    i+=1
         
driver.close()

df=pd.DataFrame({'News Title':newsTitle,'News Links':links,'Content inside the News':contents})
df.to_csv('News_Title&Contents.csv',index=False)
# print(df)