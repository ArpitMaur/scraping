# ---------------getting data form amazon by searching it---------------
import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.amazon.in/")
    
    await page.type('[id=twotabsearchtextbox]',keyword)
    # await page.screenshot({"path": "main_page.png"})
    
    await page.keyboard.press('Enter')
    await page.waitForNavigation()
    # await page.screenshot({"path": "result.png"})
    
    data= await page.evaluate('''
        ()=>  {                    
            contents=document.querySelectorAll('.a-section')
            ps=Array.from(contents).map((para)=>para.innerHTML)
            return ps
        }
    ''')
    allData=''.join(data)
    
    soup=BeautifulSoup(allData,'html.parser')
    # print(soup.prettify())
    for d in soup.find_all('div',class_='a-section a-spacing-small a-spacing-top-small'):
        titel=d.find('span',class_='a-size-medium a-color-base a-text-normal')
        print(titel.string)
        
        price=d.find('span',class_='a-price-whole')
        print(price.string)
        
    await browser.close()

print('searching.............')
item=input('Enter the item Name: ')
asyncio.get_event_loop().run_until_complete(main('laptop'))
print('end..........')