
# --------------------------------getting news from nytimes.com------------------------
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

website='https://www.nytimes.com/international/section/business'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')


driver.get(website)


titles=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/h2")
descs=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/p")
links=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a")
dates=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/span")
arthurs=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/div/p/span")
Titles=[]
Descs=[]
Links=[]
Dates=[]
Arthurs=[]
for i in range(len(titles)):
    Titles.append(titles[i].text)
    Descs.append(descs[i].text)
    Links.append(links[i].get_attribute('href'))
    Dates.append(dates[i].text)
    Arthurs.append(arthurs[i].text)

driver.quit()
df=pd.DataFrame({'Titles':Titles,'Descriptions':Descs,'Links':Links,'Dates':Dates,'Arthurs':Arthurs})
df.to_csv('news_data.csv',index=False)
print(df)
