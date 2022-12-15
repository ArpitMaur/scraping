# -----------------------------getting blog data from  https://www.codewithharry.com/blog/---------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

website='https://medium.com/'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')

driver.get(website)

titles=[]
links=[]
authors=[]
dates=[]
contents=[]

y=3000
for j in range(1):     
    data=driver.find_elements(By.XPATH,'//section/div/div/div[1]/div')
    for d in data :
            try:
                link=d.find_element(By.XPATH,'./div/div/a')
                link=link.get_attribute('href')
                links.append(link)
                print(link)
            except:
                print('Link not found...')    
      
    print(f'Finding link.... wait!! ---> {j+1}')  
    driver.execute_script((f"window.scrollTo(0, {y})") )
    time.sleep(2)    
    y=y+2000   
    
print('-'*50+"> Totle Pages --> "+str(len(set(links)))+" " +'-'*50 )    

i=1
for link in set(links):
    driver.get(link)
    time.sleep(0.5)   
    driver.execute_script(("window.scrollTo(0, 2500)") )
    try:
        title=driver.find_element(By.XPATH,'//section/div/div/div/h1')
        titles.append(title.text)
        # print(title.text)
    except Exception as e:
        titles.append('Not found.')
        print(e)          
    try:
        author=driver.find_element(By.XPATH,'//header/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/a')
        authors.append(author.text)
        # print(author.text)
    except Exception as e:
        authors.append('Not found.')
        print(e) 
           
    try:
        date=driver.find_element(By.XPATH,'//header/div[1]/div[1]/div[2]/div[2]/p/span')
        dates.append(date.text)
    except Exception as e:
        dates.append('Not found.')
        print(e)
    try:
        content=driver.find_elements(By.XPATH,"//section/div/div/p")
        temp=''
        for _ in content:
            temp+=_.text  
        # print(temp) 
        contents.append(temp)
    except Exception as e:
        contents.append('Not found.')
        print(e)    
    
    print('-'*100+' Getting Contents: Page---> '+str(i))   
    i+=1
driver.close()

df=pd.DataFrame({'Titles':titles,'Authors':authors,'Dates':dates,'Links':list(set(links)),'Contents':contents})
df.to_csv('medium_Data.csv',index=False)
# print(df)