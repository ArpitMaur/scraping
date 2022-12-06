# ----------------------scrapping news titles from inextlive.com by given links---------------------------

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.inextlive.com/national?itm_medium=national&itm_source=dsktp&itm_campaign=navigation")
    
    await page.waitFor(4000)
    
    data= await page.evaluate('''
        ()=>  {                    
            contents=document.querySelectorAll('.newsFJagran')
            ps=Array.from(contents).map((para)=>para.innerHTML)
            return ps
        }
    ''')
    allData=''.join(data)
    
    soup=BeautifulSoup(allData,'html.parser')
    for d in soup.find_all('div',class_='protxt fr'):
        title=d.find('div',class_='h3')
        print(title.string)
    await browser.close()

print('searching.............')
asyncio.get_event_loop().run_until_complete(main())
print('end..........')