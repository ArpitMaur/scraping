# -----------------------------getting news from https://scroll.in/latest ---------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


website='https://scroll.in/latest'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')

driver.get(website)
wait = WebDriverWait(driver, 10)

news_titles=[]
links=set()
dates=[]
image_links=[]
contents=[]

y=3000
i=1
for j in range(30):
    
    data=driver.find_elements(By.XPATH,'//html/body/div[8]/div/div/div[1]/ul/li')
    for d in data :
        
        link=d.find_element(By.XPATH,'./a')
    
        link=link.get_attribute('href')
        links.add(link)
            
    print('wait!!!... Finding link....'+'-'*80+' '+str(i))  
    i+=1
    driver.execute_script((f"window.scrollTo(0, {y})") )
    time.sleep(0.8)    
    y=y+2000
    
print('-'*50+"> Totle Pages --> "+str(len((links)))+" " +'-'*50 )    

i=1

for link in links:
    driver.get(link)
    
    try:
        if driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/header/h1").is_displayed():
            title=driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/header/h1")
            news_titles.append(title.text)
    except:
            title_text='News title not found in Page.'    
            news_titles.append(title_text)    
     
    try:
        if driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/header/div/div/div/time[1]").is_displayed():   
            date=driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/header/div/div/div/time[1]")
            dates.append(date.text)
    except:
            time_text='Date & time not found in Page.'        
            dates.append(time_text)

    try:
        if driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/figure/picture/img").is_displayed():
            img_link=driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/figure/picture/img")
            img_link=img_link.get_attribute('src')
            image_links.append(img_link)
    except:        
            img_text='Image link not found in Page.'    
            image_links.append(img_text)   
         
    try:    
        if driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/div[1]").is_displayed():
            content=driver.find_element(By.XPATH,"//html/body/div[8]/div[2]/article/div/section/div[1]")
            contents.append(content.text)
    except:
            content_text='Content not found in Page.'    
            contents.append(content_text)

    print('-'*100+' Getting Contents: Page---> '+str(i))   
    i+=1
    time.sleep(0.2)

driver.close()
if (len(news_titles)!=len(image_links)):
    print(len(image_links))
    for i  in range(len(news_titles)-len(image_links)):
        image_links.append('not found')
    
# print(len(news_titles))
# print(len(dates))
# print(len(links))
# print(len(contents))
# print(len(image_links))

df=pd.DataFrame({'News Name':news_titles,'Post Date':dates,'Post Links':list(links),'Data inside Links':contents,'Image Link':image_links})
df.to_csv('newsDataFrom_scrollIn.csv',index=False)
# # print(df)