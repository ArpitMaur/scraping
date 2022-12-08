# ------------------getting all data from https://datatables.net/       --------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

website='https://datatables.net/'
driver = webdriver.Chrome('C:/Users/Arpit Maurya/Desktop/Programs/Internship/chromedriver_win32/chromedriver.exe')
# options = webdriver.ChromeOptions()
driver.get(website)
names=[]
positions=[]
offices=[]
ages=[]
start_dates=[]
for i in range(6):
    rows=driver.find_elements(By.XPATH,'//*[@id="example"]/tbody/tr')
    for d in rows:
        name=d.find_element(By.XPATH,'./td[1]')
        position=d.find_element(By.XPATH,'./td[2]')
        office=d.find_element(By.XPATH,'./td[3]')
        age=d.find_element(By.XPATH,'./td[4]')
        start_date=d.find_element(By.XPATH,'//*[@id="example"]/tbody/tr/td[5]')
        
        names.append(name.text)
        positions.append(position.text)
        offices.append(office.text)
        ages.append(age.text)
        start_dates.append(start_date.get_attribute("textContent"))

    print(f'getting data from {i+1}th page.')
    next_btn=driver.find_element(By.XPATH,"//a[@data-dt-idx='next']")
    next_btn.click()
driver.close()


df=pd.DataFrame({'Names':names,'Positions':positions,'Offices':offices,'Ages':ages,'Start_dates':start_dates})
df.to_csv('data_dataTables.csv',index=False)
# print(df)