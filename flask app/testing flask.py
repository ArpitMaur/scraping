# flask app implemented without scheduler.
# scrapping function for websites:- alphv,bianlian,daixin,omega,snatch,suncrypt,unsafe blog,Vice_society,vsop

from flask import Flask,render_template
import pymongo
import threading
from tbselenium.tbdriver import TorBrowserDriver
import pandas as pd
from datetime import date
from selenium.webdriver.common.by import By
import pandas as pd
import time

app = Flask(__name__)

def alphv_scrap():
    try:
        today = date.today()
        Today_date = today.strftime("%d/%m/%Y")



        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion/')
            time.sleep(300)

            companyNames=[]
            descriptions=[]
            dates=[]
            links=[]
            createdDate=[]
            createdBy=[]

            
            for i in range(1,26):
                driver.get(f'http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion/?page={i}')
                time.sleep(2)
                datas=driver.find_elements(By.CSS_SELECTOR,".posts > div")
                for data in datas:
                    temp=''
                    try:
                        company_name=data.find_element(By.CSS_SELECTOR,".posts > div> div> div.post-header")
                        companyNames.append(company_name.text)
                        temp+=company_name.text
                    except:
                        companyNames.append('Not found')

                    try:
                        desc=data.find_element(By.CSS_SELECTOR,".posts > div> div> div.post-description")
                        temp=temp+' '+desc.text
                        descriptions.append(temp)
                    except:    
                        descriptions.append('Not found')

                    try:
                        date=data.find_element(By.CSS_SELECTOR,".posts > div> div> div.post-subheader.small")
                        dates.append(date.text)
                    except:
                        dates.append('Not found')

                    try:
                        link=data.find_element(By.CSS_SELECTOR,".posts > div > div> div > a")
                        link=link.get_attribute('href')
                        links.append(link)
                    except:
                        links.append('Not found')

            

            for _ in range(len(companyNames)):
                createdDate.append(Today_date)  
                createdBy.append('Arpit') 
                
            driver.close()

            df = pd.DataFrame({'Title': companyNames, 'Body': descriptions,'Date': dates,'Url':links,'createdAt':createdDate,'createdBy':createdBy})
            df.to_csv('/home/user/Desktop/Arpit/Alphv_Data.csv',index=False)

    except:
        print('some problem in scrapping function...')   


def bianlian_scrap():
    try:
        today = date.today()
        date = today.strftime("%d/%m/%Y")


        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion/')

            links=[]
            i=1
            try:
                while(driver.find_element(By.XPATH,"//a[@aria-label='Next']").text=='Next →'):
                    lnks=driver.find_elements(By.CLASS_NAME,'readmore')
                    for lnk in lnks:
                        link=lnk.get_attribute('href')
                        links.append(link)

                    next_btn=driver.find_element(By.XPATH,"//a[@aria-label='Next']")
                    next_btn.click()  
                    time.sleep(2)
                    print('Page  No: ' +str(i))
                    i+=1
            except:
                pass

            print('-'*50+'Total links:--> '+str(len(links))+'  '+'-'*50)

            companyNames=[]
            companyLinks=[]
            body=[]
            createdDate=[]
            createdBy=[]

            for link in links:
                driver.get(link)
                temp=''
                try:
                    companyName=driver.find_element(By.CSS_SELECTOR,"h1.title")
                    companyNames.append(companyName.text)
                    temp+=' '
                    temp+=companyName.text
                except:
                    companyNames.append('Not found')


                try:
                    link=driver.find_element(By.CSS_SELECTOR,".body > p:nth-child(1) > a:nth-child(1)")
                    companyLinks.append(link.text)  
                    temp+=' '
                    temp+=link.text
                except:
                    companyLinks.append('Not found') 

                
                try:
                    paras=driver.find_elements(By.CSS_SELECTOR,'.body > p')    
                    for para in paras:
                        if ('zip' not in para.text) and ('7z' not in para.text):
                            temp+=' '
                            temp+=para.text
                except:
                    pass

                try:
                    datas=driver.find_elements(By.CSS_SELECTOR,'.body > ul > li')
                    for data in datas:
                        temp+=' '
                        temp+=data.text
                    body.append(temp)   
                except:
                    body.append('Not found')

            for i in range(len(companyNames)):
                createdDate.append(date)  
                createdBy.append('Arpit')           

            driver.close()


            df = pd.DataFrame({'Title': companyNames,'Body': body,  'Url': links,'createdAt': createdDate,'createdBy':createdBy})
            df.to_csv('/home/user/Desktop/Arpit/Bianlian_Data.csv',index=False)

    except:
        print('some problem in scrapping function...')   


def daixin():
    try:
        today = date.today()
        date = today.strftime("%d/%m/%Y")

        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://7ukmkdtyxdkdivtjad57klqnd3kdsmq6tp45rrsxqnu76zzv3jvitlqd.onion/')
            # time.sleep(1)

            company_names=[]
            company_Links=[]
            body=[]
            createdDate=[]
            createdBy=[]
            datas=driver.find_elements(By.CSS_SELECTOR,'div.border')
            for data in datas:
                temp=''
                try:
                    company_name=data.find_element(By.CSS_SELECTOR,"div.border> h4")
                    company_names.append(company_name.text)
                    temp+=' '
                    temp+=company_name.text

                except:
                    company_names.append('Not Found')

                try:
                    links=data.find_elements(By.CSS_SELECTOR,"div.border> h6")
                    company_link=''
                    for link in links:
                        if 'Web Site:' in link.text:
                            link=driver.find_element(By.CSS_SELECTOR,"div.border>h6> a")
                            company_link=company_link+','+link.text     
                    company_Links.append(company_link)
                except:
                    company_Links.append('Not Found')

                try:
                    paras=data.find_elements(By.CSS_SELECTOR,"div.border > p")
                    for p in paras:
                        temp+=p.text
                    body.append(temp)
                except:
                    body.append('Not Found')

            driver.close()
            for i in range(len(company_names)):
                createdDate.append(date)
                createdBy.append('Arpit')


            df = pd.DataFrame({'Title': company_names, 'Body': body, 'Url': company_Links,'Created_Date': createdDate,'Created By':createdBy})

            df.to_csv('/home/user/Desktop/Arpit/Daixin_Data.csv',index=False)

    except:
        print('some problem in scrapping function...')    



def omega():
    try:
        today = date.today()
        date = today.strftime("%d/%m/%Y")





        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion/')
            # time.sleep(1)

            company_names=[]
            data_sizes=[]
            tags=[]
            dates=[]
            downlode_links=[]

            

            data=driver.find_elements(By.XPATH,"//tr[@class='trow']")
            for d in data:
                temp=''
                
                company_name=d.find_element(By.XPATH,"./td[1]")
                company_names.append(company_name.text)

                tag=d.find_element(By.XPATH,"./td[3]")
                tags.append(tag.text)

                data_size=d.find_element(By.XPATH,"./td[4]")
                data_sizes.append(data_size.text)

                last_updated=d.find_element(By.XPATH,"./td[5]")
                dates.append(last_updated.text)

                downlode_link=d.find_element(By.XPATH,"./td[6]/a")
                downlode_link=downlode_link.get_attribute('href')
                downlode_links.append(downlode_link)

            # print(company_names,data_sizes,dates,tags,downlode_links)
            driver.close()

            df = pd.DataFrame({'Company Name': company_names, 'Data Size': data_sizes, 'Last Update': dates, 'Tags': tags, 'Data Downlode Link': downlode_links})
            df.to_csv('/home/user/Desktop/Arpit/omega_data.csv',index=False)
    except:
        print('some problem in scrapping function...')    



def snatch():
    try:
        today = date.today()
        Today_date = today.strftime("%d/%m/%Y")



        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:




            links=[]
            for i in range(1,5):
                driver.get(f'http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion/index.php?page={i}')


                post_links=driver.find_elements(By.XPATH,"//a[@class='a-b-b-r-link']")
                for data in post_links:
                    try:
                        lnk=data.find_element(By.XPATH,"./button")
                        lnk=lnk.get_attribute('onclick')
                        lnk=lnk.replace("window.location='",'')
                        lnk=lnk.replace("'","")
                        lnk="http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion/"+lnk
                        links.append(lnk)
                        # print(lnk)
                    except:
                        print('not found')

            organization_name=[]
            organization_websites=[]
            Descriptions=[]
            dates=[]
            createdDate=[]
            createdBy=[]
            for link in links:
                driver.get(link)

                datas=driver.find_elements(By.XPATH,"//div[@class='n-n-c-end']")
                for data in datas:
                    temp=""

                    try:
                        company_name=data.find_element(By.XPATH,"./div[2]/h2")
                        organization_name.append(company_name.text)
                        temp+=' '+company_name.text
                    except:
                        organization_name.append('Not found')

                    try:
                        company_link=data.find_element(By.XPATH,"./div[2]/div/span")
                        # organization_websites.append(company_link.text)  
                        temp+=' '+company_link.text
                    except:
                        organization_websites.append('Not found')    

                    try:
                        d=data.find_element(By.XPATH,"./div[3]/p")
                        temp+=' '+d.text
                        Descriptions.append(temp)

                    except:
                        Descriptions.append('Not found')

                    try:
                        Date=data.find_element(By.XPATH,"./div[1]/div[1]")
                        dates.append(Date.text)
                    except:
                        dates.append('Not found')


            driver.close()

            for _ in range(len(organization_name)):
                createdDate.append(Today_date)  
                createdBy.append('Arpit') 

            df = pd.DataFrame({'Title': organization_name, 'Body': Descriptions,'Url': links, 'Date':dates,'createdAt': createdDate,'createdBy': createdBy})
            df.to_csv('/home/user/Desktop/Arpit/SNATCH_Data.csv',index=False)

    except:
        print('some problem in scrapping function...')    



def suncrypt():
    try:
        today = date.today()
        Today_date = today.strftime("%d/%m/%Y")



        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:




            links=[]
            for i in range(1,5):
                driver.get(f'http://x2miyuiwpib2imjr5ykyjngdu7v6vprkkhjltrk4qafymtawey4qzwid.onion/clients?p={i}')


                post_links=driver.find_elements(By.XPATH,"//p[@class='title is-5 mt-5']")
                for data in post_links:
                    try:
                        lnk=data.find_element(By.XPATH,"./a")
                        lnk=lnk.get_attribute('href')
                        links.append(lnk)
                    except:
                        print('not found')

            organization_name=[]
            organization_websites=[]
            info=[]
            dates=[]
            phones=[]
            address=[]
            createdDate=[]
            createdBy=[]
            for link in links:
                driver.get(link)

                datas=driver.find_elements(By.XPATH,"//div[@class='column']")

                for data in datas:
                    temp=""

                    try:
                        company_name=data.find_element(By.XPATH,"./div[1]/div/div/div")
                        organization_name.append(company_name.text)
                        temp+=' '+company_name.text
                    except:
                        organization_name.append('Not found')

                    try:
                        company_link=data.find_element(By.XPATH,"./div[1]/div/div/div[2]/a")
                        company_link=company_link.get_attribute('href')
                        # organization_websites.append(company_link)  
                        temp+=' '+company_link.text  
                    except:
                        organization_websites.append('Not found')    


                    try:
                        date=data.find_element(By.XPATH,"./div[2]/div[2]/div/table/tbody/tr[1]/td[2]")
                        dates.append(date.text)
                    except:
                        dates.append('Not found')

                    try:
                        phone=data.find_element(By.XPATH,"./div[2]/div[2]/div/table/tbody/tr[2]/td[2]")
                        # phones.append(phone.text)
                        temp+=' '+phone.text
                    except:
                        phones.append('Not found')

                    try:
                        add=data.find_element(By.XPATH,"./div[2]/div[2]/div/table/tbody/tr[3]/td[2]")
                        # address.append(add.text)
                        temp+=' '+add.text
                    except:
                        address.append('Not found')

                    try:
                        paras=data.find_elements(By.XPATH,"./div[3]/div[2]/div/p")
                        t=''
                        for para in paras:
                            t+=para.text
                        temp+=' '+t
                        info.append(temp)
                    except:
                        info.append('Not found')

            driver.close()

            for _ in range(len(organization_name)):
                createdDate.append(Today_date)  
                createdBy.append('Arpit') 

            df = pd.DataFrame({'Title': organization_name, 'body': info,'Date': dates,'Url': links, 'createdAt': createdDate,'createdBy': createdBy})
            df.to_csv('/home/user/Desktop/Arpit/SUNCRYPT_Data.csv',index=False)
            print(df)  
    except:
        print('some problem in scrapping function...')   


def unsafe_Blog():
    try:
        today = date.today()
        Today_date = today.strftime("%d/%m/%Y")



        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://unsafeipw6wbkzzmj7yqp7bz6j7ivzynggmwxsm6u2wwfmfqrxqrrhyd.onion')
            time.sleep(15)


            organization_name=[]
            body=[]
            dates=[]
            tor_link=[]
            createdDate=[]
            createdBy=[]

            datas=driver.find_elements(By.CSS_SELECTOR,"div.blog-card")
            for data in datas:
                temp=''    
                try:
                    company_name=data.find_element(By.CSS_SELECTOR,"div.blog-card > div > h4")
                    organization_name.append(company_name.text)
                    temp+=company_name.text
                except:
                    organization_name.append('Not found')

                try:
                    data=data.find_elements(By.CSS_SELECTOR,"div.blog-card > div > h6") 
                    for d in data:
                        temp+=' '+d.text
                    body.append(temp)    
                except:
                    body.append('Not found')

                try:
                    date=data.find_element(By.CSS_SELECTOR,"div.blog-card > div > h6:nth-child(2)")
                    dates.append(date.text) 
                except:
                    dates.append('Not found')

            driver.close()
            for _ in range(len(organization_name)):
                tor_link.append('http://unsafeipw6wbkzzmj7yqp7bz6j7ivzynggmwxsm6u2wwfmfqrxqrrhyd.onion/')
                createdDate.append(Today_date)  
                createdBy.append('Arpit') 

            df = pd.DataFrame({'Title': organization_name,'body': body, 'Date': dates,'Url': tor_link, 'createdAt': createdDate,'createdBy': createdBy})
            df.to_csv('/home/user/Desktop/Arpit/unsafeBlog_Data.csv',index=False)
    except:
        print('some problem in scrapping function...')       


def Vice_society():
    try:
        today = date.today()
        Today_date = today.strftime("%d/%m/%Y")


        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://ssq4zimieeanazkzc5ld4v5hdibi2nzwzdibfh5n5w4pw5mcik76lzyd.onion/')
            


            ViewAllPartners_btn=driver.find_element(By.XPATH,"//a[@href='partners.html']")
            ViewAllPartners_btn.click()

            organization_name=[]
            descriptions=[]
            links=[]
            createdDate=[]
            createdBy=[]


            
            i=1
            datas=driver.find_elements(By.XPATH,"//table[2]/tbody/tr/td[@valign='top']")
            for data in datas:
                if i!=1:
                    temp=''
                    try:
                        company_name=data.find_element(By.XPATH,"./font[1]/b")
                        organization_name.append(company_name.text)
                        temp+=' '+company_name.text
                    except:
                        organization_name.append('Not found')

                    try:
                        company_link=data.find_element(By.XPATH,"./a")
                        company_link=company_link.get_attribute('href') 
                        temp+=' '+company_link
                    except:
                        pass  

                    try:
                        location=data.find_element(By.XPATH,"./font[2]")
                        temp+=' '+location.text
                    except:
                        pass

                    try:
                        desc=data.find_element(By.XPATH,"./font[3]/b")
                        temp+=' '+desc.text
                        descriptions.append(temp)
                    except:    
                        descriptions.append('Not found')



                i+=1

            driver.close()
            for _ in range(len(organization_name)):
                createdDate.append(Today_date)  
                createdBy.append('Arpit') 
                links.append('http://ssq4zimieeanazkzc5ld4v5hdibi2nzwzdibfh5n5w4pw5mcik76lzyd.onion/')
                

            df = pd.DataFrame({'Title': organization_name, 'body': descriptions, 'Url': links, 'createdAt': createdDate,'createdBy': createdBy})



            df.to_csv('/home/user/Desktop/Arpit/Vice_Society_Data.csv',index=False)
        
 
    except:
        print('some problem in scrapping function...')      



def vsop():
    try:
        
        today = date.today()
        Today_date = today.strftime("%d/%m/%Y")



        with TorBrowserDriver("/home/user/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://mrdxtxy6vqeqbmb4rvbvueh2kukb3e3mhu3wdothqn7242gztxyzycid.onion/')
            # time.sleep(330)

            organization_name=[]
            tor_links=[]
            descriptions=[]
            createdDate=[]
            createdBy=[]

            
            

            datas=driver.find_elements(By.CSS_SELECTOR,"div.excerpt")
            for data in datas:
                try:
                    company_name=data.find_element(By.CSS_SELECTOR,"div.excerpt >h6")
                    organization_name.append(company_name.text)
                except:
                    organization_name.append('Not found')


                try:
                    paras=data.find_elements(By.CSS_SELECTOR,"div.excerpt >p")
                    temp=""
                    for para in paras:
                        temp+=para.text
                    descriptions.append(temp)
                except:    
                    descriptions.append('Not found')


            driver.close()
            for _ in range(len(organization_name)):
                tor_links.append('http://mrdxtxy6vqeqbmb4rvbvueh2kukb3e3mhu3wdothqn7242gztxyzycid.onion/')
                createdDate.append(Today_date)  
                createdBy.append('Arpit') 


            df = pd.DataFrame({'Title': organization_name, 'body': descriptions,'Url': tor_links, 'createdAt': createdDate,'createdBy': createdBy})
            df.to_csv('/home/user/Desktop/Arpit/VSOP_Data.csv',index=False)

    except:
        print('some problem in scrapping function...')   

def scrapSite(sitename,status):
    if status=='null':
        if sitename=='alphv':
            alphv_scrap()  
            collection.update_one({'name':'alphv'},{'$set':{'isUrgent':False,'status':'done'}})  
            
         
        elif sitename=='bianlian':
            bianlian_scrap()  
            collection.update_one({'name':'bianlian'},{'$set':{'isUrgent':False,'status':'done'}}) 

        elif sitename=='daixin':
            daixin()  
            collection.update_one({'name':'daixin'},{'$set':{'isUrgent':False,'status':'done'}}) 

        elif sitename=='snatch':
            snatch()  
            collection.update_one({'name':'snatch'},{'$set':{'isUrgent':False,'status':'done'}})  
            
        elif sitename=='suncrypt':
            suncrypt()
            collection.update_one({'name':'suncrypt'},{'$set':{'isUrgent':False,'status':'done'}})  

        elif sitename=='unsafe blog':
            unsafe_Blog()
            collection.update_one({'name':'unsafe blog'},{'$set':{'isUrgent':False,'status':'done'}})  
            
        elif sitename=='vice society':
            Vice_society()
            collection.update_one({'name':'vice society'},{'$set':{'isUrgent':False,'status':'done'}})  
            
        elif sitename=='vsop':
            vsop()
            collection.update_one({'name':'vsop'},{'$set':{'isUrgent':False,'status':'done'}})  
            
         
        elif sitename=='omega':
            omega()
            collection.update_one({'name':'omega'},{'$set':{'isUrgent':False,'status':'done'}})  
            
         
            

# for connecting to mongodb 
client=pymongo.MongoClient('mongodb://localhost:27017/')
print(client)
db=client['darkweb']
collection=db['sites']


# getting site form database :- one by one
def siteFromDatabase():
    while True:     
        if(collection.count_documents({'isUrgent':True})>0):
            urgent=collection.find({'isUrgent':True},{"_id":0,'name':1,'status':1,'isUrgent':1})
            for u in urgent:
                site=[]
                for i,j in u.items():
                    if i=='name':
                        site.append(j) 
                print('currently scrapping site:-  '+site[0])       
                scrapSite(site[0],'null')       
        else:
            item=(collection.find_one({'status':'null'},{"_id":0,'name':1,'status':1,'isUrgent':1}))
            if str(item)!='None': 
                site=[]
                status=[]
                for i,j in item.items():
                    if i=='name':
                        site.append(j) 
                    elif i=='status':
                        status.append(j) 
                print('currently scrapping site:-  '+site[0])     
                scrapSite(site[0],status[0])     


# running a new thread for scrapping website
t1 = threading.Thread(target=siteFromDatabase, args=())
t1.start()



@app.route('/')
def hello_world():
    return 'Hello, World!!!, Welcome to home page of this site'
    
@app.route('/product')
def product():
    return 'this is products listed on this page..'

@app.route('/site')
def site():
    return 'this is other site of this page..'

if __name__=="__main__":
    app.run(debug=True,port=8000)
            
