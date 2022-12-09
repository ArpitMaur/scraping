# https://pinchofyum.com/blog

# ---------------------------------getting BLog data from  https://pinchofyum.com/blog---------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
import time


website='https://www.igadgetsworld.com/technology/'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
driver.get(website)

wait = WebDriverWait(driver, 10)

blogTitle=[]
links=[]
contents=[]
i=1
# while(driver.find_element(By.XPATH,"//main/div/div/div/div/div/div").text=='Load More'):
# data=driver.find_element(By.XPATH,"//a[@class='next page-numbers']")
# print(data.text)
for j in range(11):
    data=driver.find_elements(By.XPATH,"//article/div/div/h2")

    for d in data :
        title=d.find_element(By.XPATH,'./a')
        blogTitle.append(title.text)
        link=d.find_element(By.XPATH,'./a')
        link=link.get_attribute('href')
        links.append(link)
        print(title.text)
        print(link)
    
    print('-'*100+"> Page --> "+str(i) )    
    i+=1
    lodeMore_btn=wait.until(EC.presence_of_element_located((By.XPATH,"//main/div/div/div/div/div/div/button")))
    lodeMore_btn.click()
    time.sleep(4)

    
    
# for link in links:
#     driver.get(link)
#     title=wait.until(EC.presence_of_element_located((By.XPATH,"//main/div/div[2]/div[1]/div/div[1]/div/div/h1")))
#     blogTitle.append(title.text)
#     # print(title.text)
    
#     content=wait.until(EC.presence_of_element_located((By.XPATH,"//main/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]")))
#     contents.append(content.text)
#     # print(content.text)

#     time.sleep(3)
#     print('-'*100+' Page---> "'+str(i)+'"')   
#     i+=1    
    
driver.close()

df=pd.DataFrame({'Blogs Name':blogTitle,'Links':links})
df.to_csv('blogData_iGadgetsWorld.csv',index=False)
print(df)