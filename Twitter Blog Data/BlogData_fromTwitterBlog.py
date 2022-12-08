# -----------------------------getting data from  https://blog.twitter.com/ ---------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website='https://blog.twitter.com/'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
# options = webdriver.ChromeOptions()
driver.get(website)


names=[]
links=[]
dates=[]
i=1
# while(driver.find_element(By.XPATH,'//*[@id="component-wrapper"]/div[3]/div/div/div[2]/div/div/div/a').text=='See more'):
for j in range(45):
    data=driver.find_elements(By.XPATH,'//*[@id="component-wrapper"]/div/div/div/div/div/div/div/div/div')
    for d in data :
        title=d.find_element(By.XPATH,'./a')
        names.append(title.text)
        link=d.find_element(By.XPATH,'./a')
        link=link.get_attribute('href')
        links.append(link)
        date=d.find_element(By.XPATH,'//*[@id="component-wrapper"]/div/div/div/div/div/div/div/div/div/div/p/time')
        # print(title.text)
        # print(link)
        dates.append(date.text)
    print('-'*100+"> Page --> "+str(i) )    
    i+=1
    seeMore_btn=driver.find_element(By.XPATH,'//*[@id="component-wrapper"]/div[3]/div/div/div[2]/div/div/div/a')
    seeMore_btn.click()
    time.sleep(0.2)    
    
driver.close()

df=pd.DataFrame({'Blogs Name':names,'Links':links,'Post Date':dates})
df.to_csv('data_TwitterBlog.csv',index=False)
# print(df)