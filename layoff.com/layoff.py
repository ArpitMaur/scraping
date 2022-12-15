# -----------------------------getting data from  https://blog.twitter.com/ ---------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

website='https://www.thelayoff.com/twitter'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
driver.get(website)

not_found_text='Not Found'

Titels=[]
links=[]
summary=[]
i=1
# while(driver.find_element(By.XPATH,'//*[@id="component-wrapper"]/div[3]/div/div/div[2]/div/div/div/a').text=='See more'):
for j in range(5):
    data=driver.find_elements(By.XPATH,'//article')
    for d in data :
        try:
            title=d.find_element(By.XPATH,'./header/h2')
            print(title.text)
            Titels.append(title.text)
        except:
            Titels.append(not_found_text)
        
        try:    
            link=d.find_element(By.XPATH,'./header/h2/a')
            link=link.get_attribute('href')
            links.append(link)
            # print(link)
        except:
            links.append(not_found_text)
                
        try:
            data=d.find_element(By.XPATH,'./div/p')
            # print(data.text)
            summary.append(data.text)
        except:
            summary.append(not_found_text)
            
    print('-'*100+"> Page --> "+str(i) )    
    i+=1
    
    temp=True
    try:
        olderTopic_btn=driver.find_element(By.XPATH,'//main/div[3]/ul[2]/li[2]/a')
        olderTopic_btn.click()
        time.sleep(2)  
        temp=False
    except:    
         print('btn not found') 
    
    if temp:    
        try:
            olderTopic_btn=driver.find_element(By.XPATH,'//main/div/ul[2]/li/a')
            olderTopic_btn.click()
            time.sleep(2)  
        except:
            print('btn2 not found')
    
    
driver.close()

df=pd.DataFrame({'Titles':Titels,'Links':links,'Contents':summary})
df.to_csv('layoff.csv',index=False)
print(df)