# ---------------getting data form amazon by given link---------------

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.amazon.in/s?k=tablet+under+10000&crid=2CSZLPDC4OT9J&sprefix=tablet%2Caps%2C296&ref=nb_sb_ss_ts-doa-p_1_6")
    
    await page.waitFor(4000)
    
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
asyncio.get_event_loop().run_until_complete(main())
print('end..........')