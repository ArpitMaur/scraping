# ---------------------------------getting data from https://androidos.in/ ---------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website='https://androidos.in/'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
# options = webdriver.ChromeOptions()
driver.get(website)

india_btn=driver.find_element(By.XPATH,'//*[@id="menu-item-102513"]/a')

india_btn.click()
names=[]
links=[]
i=1
while(driver.find_element(By.XPATH,'//*[@id="infinite-handle"]/span/button').text=='Older posts'):
    data=driver.find_elements(By.XPATH,"//section/main/div/article/header")
    for d in data :
        title=d.find_element(By.XPATH,'./h2')
        names.append(title.text)
        link=d.find_element(By.XPATH,'./h2/a')
        link=link.get_attribute('href')
        links.append(link)
        # print(title.text)
        # print(link)
    print('-'*100+"> Page --> "+str(i) )    
    i+=1
    olderPost_btn=driver.find_element(By.XPATH,'//*[@id="infinite-handle"]/span/button')
    olderPost_btn.click()
    time.sleep(1)    
    
driver.close()

df=pd.DataFrame({'Blogs Name':names,'Links':links,})
df.to_csv('data_AndroidoOsBlog.csv',index=False)
# print(df)