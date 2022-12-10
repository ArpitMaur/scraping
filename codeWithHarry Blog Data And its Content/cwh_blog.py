# -----------------------------getting blog data from  https://www.codewithharry.com/blog/---------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

website='https://www.codewithharry.com/blog/'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')

driver.get(website)
wait = WebDriverWait(driver, 10)

names=[]
links=[]
dates=[]
contents=[]

y=3000
i=1

for j in range(10):
    
    data=driver.find_elements(By.XPATH,'//html/body/div/div/div/div/div/div/div/div/div')
    for d in data :
        if i==9:
            title=d.find_element(By.XPATH,'./div[2]/span/a')
            names.append(title.text)
            link=d.find_element(By.XPATH,'./div[2]/span/a')
            link=link.get_attribute('href')
            links.append(link)
            # print(link)
            date=d.find_element(By.XPATH,'./div[1]/span')
            dates.append(date.text)
            # print(date.text)
            
    print('Finding link.... wait!!')  
    i+=1
    driver.execute_script((f"window.scrollTo(0, {y})") )
    time.sleep(4)    
    y=y+1500
    
print('-'*50+"> Totle Pages --> "+str(len(links))+" " +'-'*50 )    
  
i=1
for link in links:
    driver.get(link)
    
    content=wait.until(EC.presence_of_element_located((By.XPATH,"//html/body/div/div/div[4]/div/div/div[1]")))
    contents.append(content.text)
    
    time.sleep(0.5)
    print('-'*100+' Getting Contents: Page---> '+str(i))   
    i+=1
    
driver.close()

df=pd.DataFrame({'Post Name':names,'Post Date':dates,'Links':links,'Data inside Links':contents})
df.to_csv('cwh_blog_data.csv',index=False)
# print(df)