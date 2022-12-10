# -----------------------------getting data from  https://blog.twitter.com/ ---------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

website='https://blog.twitter.com/'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
driver.get(website)
wait = WebDriverWait(driver, 10)



names=[]
links=[]
dates=[]
contents=[]
i=1

not_found_text='not found on page'
for j in range(5):
    data=driver.find_elements(By.XPATH,'//*[@id="component-wrapper"]/div/div/div/div/div/div/div/div/div')
    for d in data :
        try:
            title=d.find_element(By.XPATH,'./a')
            names.append(title.text)
        except:  
              names.append(not_found_text)
        try:
            link=d.find_element(By.XPATH,'./a')
            link=link.get_attribute('href')
            links.append(link)
        except:    
            links.append(not_found_text)
        try:
            date=d.find_element(By.XPATH,'//*[@id="component-wrapper"]/div/div/div/div/div/div/div/div/div/div/p/time')
            dates.append(date.text)
            
        except:    
            dates.append(not_found_text)     
        # print(title.text)
        # print(link)
        
    print('-'*100+"> Getting Link: Page --> "+str(i) )    
    i+=1
    seeMore_btn=driver.find_element(By.XPATH,'//*[@id="component-wrapper"]/div[3]/div/div/div[2]/div/div/div/a')
    seeMore_btn.click()
    time.sleep(0.2)    
print('-'*50+"> Totle Pages --> "+str(len(links)) +'-'*50 )    
  
i=1
for link in links:
    driver.get(link)
    try:
        content=wait.until(EC.presence_of_element_located((By.XPATH,"//html/body/div[4]/div[1]/div/div[1]")))
        contents.append(content.text)
    except:
        contents.append(not_found_text)    
    
    time.sleep(0.3)
    print('-'*100+' Getting Contents: Page---> '+str(i))   
    i+=1

driver.close()

df=pd.DataFrame({'Post Name':names,'Post Date':dates,'Links':links,'Data inside Links':contents})
df.to_csv('Twitter_blogContent.csv',index=False)
# print(df)